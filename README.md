# 深问规划 · Deep Grill Planner

[简体中文](README.zh-CN.md) · **English** · [Installation](docs/installation.md) · [Releases](https://github.com/YkxbGcl2001/deep-grill-planner/releases)

**Ask the questions that change the plan. Start manually, or through your enabled Plan Mode bridge.**

A standalone Agent Skill combining dependency-aware question rounds from Grilling with assumption challenges and readiness checks from Deep Interview. The interview uses the agent's existing tools: no OMC, API key, server, or Python runtime is required.

## Features

- Reads context first; separates facts the agent can investigate from decisions the user must make.
- Groups independent questions, leaves dependent ones for later, and explains recommendations and trade-offs.
- Offers Quick, Standard, and Deep scrutiny without forcing question counts.
- Reuses confirmed answers and revisits affected decisions when a prerequisite changes.
- Challenges material assumptions and checks acceptance conditions.
- Stops when remaining uncertainty no longer materially changes implementation.
- Produces requirements, decisions, assumptions/open items, and an implementation plan.
- Supports Chinese and English, optional checkpoints, and optional heuristic scoring.
- Preserves existing authorization; an interview-only request does not silently become execution.

This workflow does not modify native Plan Mode or its question limits. The Skill has no executable install hooks, telemetry, or background services. The optional utilities copy local files or edit the explicitly selected instruction file. The host agent may use its normal tools during a requested task.

## Install

For local Codex skills, clone and run the optional standard-library installer (Python 3.9+):

```sh
git clone https://github.com/YkxbGcl2001/deep-grill-planner.git
cd deep-grill-planner
python3 scripts/install.py
```

Default destination: `~/.agents/skills/deep-grill-planner`. Existing folders are never overwritten. Windows: `py -3 scripts/install.py`. Manual copying and custom destinations are supported. Start a new chat; restart the host if the skill is not discovered.

For the ChatGPT Work / Codex desktop plugin, add this repo marketplace with a supporting CLI:

```sh
codex plugin marketplace add YkxbGcl2001/deep-grill-planner --ref v1.1.0
```

Then select this marketplace in the desktop Plugins Directory, install Deep Grill Planner, and start a new chat. This GitHub-distributed plugin is not listed in OpenAI's universal public directory. Host/account availability varies. See [full installation instructions](docs/installation.md) and their verification limits.

Or download the Skill ZIP, plugin ZIP, and `SHA256SUMS.txt` from [v1.1.0](https://github.com/YkxbGcl2001/deep-grill-planner/releases/tag/v1.1.0). Install only the Skill folder when using standalone skill discovery.

## Manual activation and Plan Mode

Task-description-based activation is **disabled** (`allow_implicit_invocation: false`). In normal mode, choose 深问规划 or explicitly invoke `$deep-grill-planner` when wanted.

You can explicitly enable the optional **Plan Mode bridge** after installing the Skill:

```sh
python3 scripts/plan_bridge.py
```

It adds a small, removable managed section to your Codex `AGENTS.md`, preserving existing rules. After starting a new Codex session, manually select Plan Mode and submit your task: if the host provides a trusted current Plan state, that rule directs the agent to load the Skill. Returning to normal mode stops the automatic entry. It never infers Plan Mode from task wording or hook permission fields.

This is an instruction-level integration, not a native UI event callback or guaranteed binary enforcement. It depends on the host loading AGENTS.md and the model following the rule. No live UI toggle test is claimed. See [bridge design and setup](docs/plan-mode.md).

## Usage

```text
Use $deep-grill-planner to clarify my idea for an offline field-data tool.
Recommend practical options and prepare a plan. Do not implement it yet.
```

```text
Use $deep-grill-planner in Quick mode to challenge this migration plan.
Read the repository first. Only ask about decisions that change the approach.
```

The `$skill-name` syntax is for Codex. Other hosts may use a skill picker, plugin mention, or natural language; follow the host's supported syntax.

For a vague tool idea, an early round can establish the core workflow and offline needs. A sync-conflict policy should wait until the decisions that make synchronization necessary are settled.

## Source and development

- [Complete Skill](skills/deep-grill-planner/SKILL.md)
- [Design / 设计](docs/architecture.md)
- [Verification / 验证](docs/verification.md)
- [Behavior scenarios](tests/scenarios.md)
- [Pinned source provenance](docs/provenance.json)

```sh
python3 -m unittest discover -s tests -v
python3 scripts/build.py
```

The utilities use only the Python standard library. Rebuilt packages and checksums appear in `dist/`. The Skill has no required executable helper.

## License and credits

MIT. Adapted from [Matt Pocock's Grilling](https://github.com/mattpocock/skills) and [Yeachan Heo's Deep Interview](https://github.com/Yeachan-Heo/oh-my-claudecode). Their copyright and permission notices are preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and in the installable Skill. No upstream endorsement is implied.

Contributions in English or Chinese are welcome. Report realistic failing interviews and expected behavior; do not post private transcripts or credentials. See [CONTRIBUTING.md](CONTRIBUTING.md).
