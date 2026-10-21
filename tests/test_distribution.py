"""Executable checks of install/package behavior; not claims about model judgment."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


installer = load("install")
builder = load("build")


class DistributionTests(unittest.TestCase):
    def test_installed_tree_is_complete(self):
        source = ROOT / "skills" / installer.NAME
        with tempfile.TemporaryDirectory() as directory:
            target = installer.install(directory)
            expected = {p.relative_to(source).as_posix(): p.read_bytes()
                        for p in source.rglob("*") if p.is_file()}
            actual = {p.relative_to(target).as_posix(): p.read_bytes()
                      for p in target.rglob("*") if p.is_file()}
            self.assertEqual(expected, actual)
            self.assertIn("LICENSE", actual)
            self.assertIn("THIRD_PARTY_NOTICES.md", actual)

    def test_existing_install_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            target = installer.install(directory)
            marker = target / "local-customization.md"
            marker.write_text("keep me", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                installer.install(directory)
            self.assertEqual(marker.read_text(encoding="utf-8"), "keep me")

    def test_symlink_destination_is_not_followed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            outside = root / "outside"
            outside.mkdir()
            (root / installer.NAME).symlink_to(outside, target_is_directory=True)
            with self.assertRaises(FileExistsError):
                installer.install(root)
            self.assertEqual(list(outside.iterdir()), [])

    def test_invalid_source_does_not_create_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "invalid"
            source.mkdir()
            with self.assertRaises(ValueError):
                installer.install(root / "dest", source)
            self.assertFalse((root / "dest").exists())

    def test_install_rejects_recursive_destination(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source"
            source.mkdir()
            (source / "SKILL.md").write_text("test", encoding="utf-8")
            with self.assertRaises(ValueError):
                installer.install(source / "nested", source)

    def test_packages_are_complete_clean_and_reproducible(self):
        with tempfile.TemporaryDirectory() as a, tempfile.TemporaryDirectory() as b:
            first, second = builder.build(a), builder.build(b)
            for x, y in zip(first, second):
                self.assertEqual(x.read_bytes(), y.read_bytes())
                with zipfile.ZipFile(x) as archive:
                    self.assertIsNone(archive.testzip())
                    names = archive.namelist()
                    self.assertTrue(all(not n.startswith("/") and ".." not in Path(n).parts for n in names))
                    self.assertFalse(any("__pycache__" in n or "/upstream/" in n or "/.git/" in n for n in names))
            with zipfile.ZipFile(first[0]) as archive:
                prefix = installer.NAME + "/"
                for path in (ROOT / "skills" / installer.NAME).rglob("*"):
                    if path.is_file():
                        relative = path.relative_to(ROOT / "skills" / installer.NAME).as_posix()
                        self.assertEqual(archive.read(prefix + relative), path.read_bytes())
            with zipfile.ZipFile(first[1]) as archive:
                prefix = installer.NAME + "-plugin/"
                self.assertIn(prefix + "plugin.json", archive.namelist())
                self.assertIn(prefix + ".agents/plugins/marketplace.json", archive.namelist())
                self.assertIn(prefix + "README.zh-CN.md", archive.namelist())
            for line in (Path(a) / "SHA256SUMS.txt").read_text().splitlines():
                digest, filename = line.split("  ")
                self.assertEqual(hashlib.sha256((Path(a) / filename).read_bytes()).hexdigest(), digest)

    def test_marketplace_resolves_plugin_and_skill(self):
        market = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
        entry = market["plugins"][0]
        plugin_root = ROOT / entry["source"]["path"]
        plugin = json.loads((plugin_root / "plugin.json").read_text())
        self.assertEqual(plugin["name"], entry["name"])
        skill = plugin_root / "skills" / entry["name"] / "SKILL.md"
        text = skill.read_text()
        self.assertTrue(text.startswith("---\n"))
        self.assertIn(f'name: {entry["name"]}', text)
        self.assertIn(f'version: "{plugin["version"]}"', text)

    def test_all_relative_markdown_links_resolve(self):
        errors = []
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", "dist", "upstream"} for part in path.relative_to(ROOT).parts):
                continue
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                if not (path.parent / target.split("#")[0]).exists():
                    errors.append((str(path.relative_to(ROOT)), target))
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
