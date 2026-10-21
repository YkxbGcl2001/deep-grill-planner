#!/usr/bin/env python3
"""Build deterministic Skill and plugin ZIPs with SHA-256 checksums."""

import argparse
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
NAME = "deep-grill-planner"
PUBLIC_PATHS = [".agents", ".github", ".gitignore", "plugin.json", "skills", "README.md",
                "README.zh-CN.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "CONTRIBUTING.md",
                "docs", "scripts", "tests"]


def files_in(path):
    candidates = [path] if path.is_file() else sorted(path.rglob("*"))
    for candidate in candidates:
        if candidate.is_symlink():
            raise ValueError(f"Refusing symbolic link: {candidate}")
        if "__pycache__" in candidate.parts or candidate.suffix in {".pyc", ".pyo"}:
            continue
        if candidate.is_file() and candidate.name != ".DS_Store":
            yield candidate


def write_zip(output, entries):
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative, path in sorted(entries):
            info = zipfile.ZipInfo(relative, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def build(output, root=ROOT):
    root = Path(root)
    version = json.loads((root / "plugin.json").read_text(encoding="utf-8"))["version"]
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    skill = root / "skills" / NAME
    standalone = [(f"{NAME}/{p.relative_to(skill).as_posix()}", p) for p in files_in(skill)]
    plugin = []
    for relative in PUBLIC_PATHS:
        path = root / relative
        if path.exists():
            plugin.extend((f"{NAME}-plugin/{p.relative_to(root).as_posix()}", p) for p in files_in(path))
    outputs = [output / f"{NAME}-skill-v{version}.zip", output / f"{NAME}-plugin-v{version}.zip"]
    write_zip(outputs[0], standalone)
    write_zip(outputs[1], plugin)
    checksums = "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in outputs)
    (output / "SHA256SUMS.txt").write_text(checksums, encoding="utf-8")
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    for path in build(args.output):
        print(f"Built: {path.name} ({path.stat().st_size} bytes)")
    print("Checksums: SHA256SUMS.txt")


if __name__ == "__main__":
    main()
