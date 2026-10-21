#!/usr/bin/env python3
"""Explicit opt-in/out for a conditional Plan Mode rule in Codex AGENTS.md."""

import argparse
import os
from pathlib import Path
import stat
import tempfile

ROOT = Path(__file__).resolve().parents[1]
START = "\n<!-- deep-grill-planner:plan-bridge:start -->\n"
END = "<!-- deep-grill-planner:plan-bridge:end -->\n"


def default_skill():
    for folder in [Path.home() / ".agents/skills/deep-grill-planner",
                   Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "skills/deep-grill-planner"]:
        if (folder / "SKILL.md").is_file():
            return folder
    raise ValueError("Install the Skill first, or specify --skill-path")


def managed_span(text):
    starts, ends = text.count(START), text.count(END)
    if starts == ends == 0:
        return None
    if starts != 1 or ends != 1:
        raise ValueError("Malformed or duplicate managed markers; no file changed")
    first = text.index(START)
    last = text.index(END)
    if last < first:
        raise ValueError("Managed markers are out of order; no file changed")
    return first, last + len(END)


def update(instructions, skill=None, remove=False, dry_run=False):
    target = Path(instructions).expanduser()
    if target.is_symlink():
        raise ValueError("Refusing a symbolic-link instructions file")
    original = target.read_bytes() if target.exists() else b""
    text = original.decode("utf-8")
    span = managed_span(text)
    if remove:
        updated = text if span is None else text[:span[0]] + text[span[1]:]
    else:
        folder = Path(skill).expanduser() if skill else default_skill()
        entry = folder if folder.name == "SKILL.md" else folder / "SKILL.md"
        if not entry.is_file():
            raise ValueError("Skill path must contain SKILL.md")
        path_text = str(entry.resolve())
        if any(char in path_text for char in ["\n", "\r", "`"]):
            raise ValueError("Unsupported characters in the Skill path")
        template = ROOT / "skills/deep-grill-planner/assets/plan-mode-bridge.md"
        block = START + template.read_text(encoding="utf-8").replace("{skill_path}", path_text).rstrip() + "\n" + END
        updated = text + block if span is None else text[:span[0]] + block + text[span[1]:]
    encoded = updated.encode("utf-8")
    if not dry_run and encoded != original:
        target.parent.mkdir(parents=True, exist_ok=True)
        mode = stat.S_IMODE(target.stat().st_mode) if target.exists() else 0o644
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=target.parent, prefix=".deep-grill-", delete=False) as stream:
                temporary = Path(stream.name)
                stream.write(encoded)
            temporary.chmod(mode)
            if target.is_symlink() or (target.read_bytes() if target.exists() else b"") != original:
                raise ValueError("Instructions changed concurrently; no replacement made")
            os.replace(temporary, target)
        finally:
            if temporary and temporary.exists():
                temporary.unlink()
    return updated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    codex_root = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    parser.add_argument("--instructions", type=Path, default=codex_root / "AGENTS.md")
    parser.add_argument("--skill-path", type=Path)
    parser.add_argument("--remove", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        result = update(args.instructions, args.skill_path, args.remove, args.dry_run)
    except (OSError, ValueError, UnicodeError) as error:
        parser.exit(1, f"Bridge update stopped: {error}\n")
    if args.dry_run:
        print(result)
    else:
        print(f"Plan Mode bridge {'removed' if args.remove else 'enabled'}: {args.instructions}")
        print("Start a new Codex session. Activation occurs after a task is submitted in trusted Plan Mode.")


if __name__ == "__main__":
    main()
