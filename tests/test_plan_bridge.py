"""Managed-file behavior checks; host/model mode routing is a separate live test."""

import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("plan_bridge", ROOT / "scripts/plan_bridge.py")
bridge = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bridge)
SKILL = ROOT / "skills/deep-grill-planner"


class PlanBridgeTests(unittest.TestCase):
    def test_enable_repeat_remove_preserves_original_bytes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "AGENTS.md"
            original = "原有字体要求\nExisting rules.  ".encode("utf-8")
            path.write_bytes(original)
            bridge.update(path, SKILL)
            first = path.read_bytes()
            bridge.update(path, SKILL)
            self.assertEqual(path.read_bytes(), first)
            bridge.update(path, remove=True)
            self.assertEqual(path.read_bytes(), original)

    def test_dry_run_does_not_write(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "AGENTS.md"
            rendered = bridge.update(path, SKILL, dry_run=True)
            self.assertIn(str((SKILL / "SKILL.md").resolve()), rendered)
            self.assertFalse(path.exists())

    def test_malformed_markers_are_not_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "AGENTS.md"
            text = "existing" + bridge.START + "interrupted block"
            path.write_text(text)
            with self.assertRaises(ValueError):
                bridge.update(path, SKILL)
            self.assertEqual(path.read_text(), text)

    def test_missing_skill_does_not_change_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "AGENTS.md"
            path.write_bytes(b"keep")
            with self.assertRaises(ValueError):
                bridge.update(path, Path(directory) / "missing")
            self.assertEqual(path.read_bytes(), b"keep")

    def test_symlink_file_is_not_followed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            outside = root / "outside.md"
            outside.write_bytes(b"keep")
            path = root / "AGENTS.md"
            path.symlink_to(outside)
            with self.assertRaises(ValueError):
                bridge.update(path, SKILL)
            self.assertEqual(outside.read_bytes(), b"keep")

    def test_rules_after_block_survive_replacement_and_removal(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "AGENTS.md"
            path.write_bytes(b"prefix")
            bridge.update(path, SKILL)
            with path.open("ab") as stream:
                stream.write(b"\nuser-added suffix\n")
            bridge.update(path, SKILL)
            bridge.update(path, remove=True)
            self.assertEqual(path.read_bytes(), b"prefix\nuser-added suffix\n")


if __name__ == "__main__":
    unittest.main()
