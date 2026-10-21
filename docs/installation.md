# Installation

[中文](installation.zh-CN.md)

## Standalone Skill: Codex

Use a host that loads local Agent Skills. Git and Python 3.9+ are needed only for this optional route:

```sh
git clone --branch v1.0.1 --depth 1 https://github.com/YkxbGcl2001/deep-grill-planner.git
cd deep-grill-planner
python3 scripts/install.py
```

This copies only `skills/deep-grill-planner/` to `~/.agents/skills/deep-grill-planner`. It does not edit settings, install dependencies, contact servers, or overwrite existing folders. If your host scans a different location, set its parent:

```sh
python3 scripts/install.py --dest /absolute/path/to/skills
```

An environment using the legacy Codex location can select `~/.codex/skills`. Do not install identical copies in multiple discovery locations. The host determines which directories it scans.

Manual option: download the Skill ZIP from Releases, verify the checksum, and copy the `deep-grill-planner/` folder to a supported skills directory. The final path must contain `deep-grill-planner/SKILL.md`. Windows can use `py -3` instead of `python3` for the optional installer.

Start a new chat and invoke `$deep-grill-planner` or select it through the skill picker. If unavailable, check the path and restart the host. Ordinary ChatGPT web chats do not automatically scan local skill folders.

## ChatGPT Work / Codex desktop plugin

The root is a skills-only plugin with a portable manifest. Its repo marketplace is `.agents/plugins/marketplace.json`.

With a supporting Codex CLI:

```sh
codex plugin marketplace add YkxbGcl2001/deep-grill-planner --ref v1.0.1
```

Alternatively clone the repo and add the local absolute path:

```sh
codex plugin marketplace add /absolute/path/to/deep-grill-planner
```

Open the desktop Plugins Directory, select the Deep Grill Planner marketplace, install its plugin, and start a new chat with it enabled. Restart the desktop app if a new source is not visible. Invoke it using the host's plugin/skill picker; syntax may vary by surface.

No MCP connection, credential, hook, or service is requested. Adding a marketplace is separate from installing its plugin. GitHub publication is not publication to OpenAI's universal public directory. Packaging and paths have been checked; end-to-end ChatGPT Work UI installation is not yet verified. If the surface cannot load custom marketplaces, use a supported local Agent Skill host.

## Packages and verification

- `deep-grill-planner-skill-v1.0.1.zip`: standalone Skill, references, templates, licenses.
- `deep-grill-planner-plugin-v1.0.1.zip`: plugin, marketplace, bilingual docs, utilities, tests.
- `SHA256SUMS.txt`: SHA-256 for both packages.
- GitHub's automatic source archives: the complete versioned repository.

In the download directory:

```sh
# macOS
shasum -a 256 -c SHA256SUMS.txt
# Linux
sha256sum -c SHA256SUMS.txt
```

Windows: use `Get-FileHash <zip-file> -Algorithm SHA256` and compare the corresponding line. Checksums detect differing bytes; they are not a publisher signature.

## Updates and removal

Preserve local customizations, move/remove only the existing `deep-grill-planner` installation folder, then install the chosen version. There is deliberately no overwrite flag. Uninstall a standalone Skill by removing that folder; no background service or settings entry is created. Uninstall a plugin through its host, and remove its marketplace separately if desired.

Checkpoints are in task workspaces, not the installed Skill. They may contain private information; review them before sharing. Installation does not publish them.

Official references checked on 2026-10-21: [Build skills](https://learn.chatgpt.com/docs/build-skills), [Package your plugin](https://developers.openai.com/plugins/build/plugins). Host support can change; consult these pages when menus or commands differ.

## Invocation and Plan Mode

The display name is 深问规划; the identifier remains `$deep-grill-planner`. Normal mode is sufficient. Plan Mode and skill selection are independent: opening Plan Mode alone does not select this Skill. Select or invoke the Skill explicitly when wanted. It obeys host mode restrictions, including returning plans/checkpoints in chat when file writes are disallowed.
