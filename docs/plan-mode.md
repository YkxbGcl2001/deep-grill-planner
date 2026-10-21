# Plan Mode bridge / 计划模式桥接

## The two deliberate entry points / 两个主动入口

1. Explicitly select 深问规划 or invoke `$deep-grill-planner` in any supported mode.
2. Opt into the bridge once, start a new Codex session, manually select Plan Mode, and submit a task. The host-provided current Plan state directs the agent to load the Skill.

1. 在支持的模式中主动选择深问规划，或调用 `$deep-grill-planner`。
2. 主动配置一次桥接，新建 Codex 会话，手动打开计划模式并发送任务；规则依据宿主当前 Plan 状态，引导智能体加载技能。

`allow_implicit_invocation: false` disables task-description matching. A complex task in normal mode does not automatically opt into this Skill. Merely saying “plan” or discussing the plugin is not a mode transition. Selecting Plan Mode is the explicit mode-based opt-in; the instruction bridge then removes the need to mention the Skill each time. No background work starts merely because a UI switch was clicked; it acts when the next task is submitted.

任务描述匹配已关闭。普通模式的复杂任务不构成启用；说到“计划”或讨论插件也不构成模式切换。手动打开计划模式是模式入口的主动选择，发送下一条任务时才开始工作，不是在点击开关后启动后台任务。

## Enable / 启用

First install the Skill normally. The bridge is optional and is never enabled by `scripts/install.py` alone.

先正常安装 Skill。桥接是可选项，仅运行安装工具不会修改全局规则。

```sh
python3 scripts/install.py
python3 scripts/plan_bridge.py --dry-run
python3 scripts/plan_bridge.py
```

The helper locates an installed Skill in `~/.agents/skills/` or the Codex home skills directory. By default it adds a managed section to `$CODEX_HOME/AGENTS.md` (normally `~/.codex/AGENTS.md`). It preserves the existing file content, including font rules or other personal instructions. Its explicit absolute Skill path is generated only on the local machine and is not committed to GitHub.

工具查找已安装的 Skill，默认向 Codex 全局 `AGENTS.md` 添加有起止标记的规则段，保留原有字体、写作和其他要求。本机绝对路径只在安装时生成，不提交 GitHub。

For a custom installation or project-only rule:

```sh
python3 scripts/plan_bridge.py --skill-path /absolute/path/to/deep-grill-planner --instructions /absolute/path/to/project/AGENTS.md
```

Start a new Codex session so the updated instruction chain is loaded. If an `AGENTS.override.md` takes precedence over your chosen file, or project rules override the section, resolve that explicitly; the helper does not edit those other files. A host that does not load local AGENTS.md cannot use this bridge.

新建会话加载更新后的规则。如果 `AGENTS.override.md` 优先于所选文件，或项目规则覆盖了该段，需要明确处理；工具不修改其他文件。不读取本地 AGENTS.md 的宿主无法使用该桥接。

## Disable / 关闭

```sh
python3 scripts/plan_bridge.py --remove
```

For a custom instructions file, pass the same `--instructions` path. Removal touches only the managed block. Skill selection remains available explicitly. Returning to normal mode already stops mode-based activation without removing the bridge. A direct instruction to skip the Skill is respected for that task/turn.

自定义文件使用同一个 `--instructions` 路径。撤销只移除标记段，仍可手动调用 Skill。单次退出计划模式即可停止模式触发，不必每次卸载；明确要求跳过时也应尊重。

## What is actually implemented / 实际实现层级

The integration is a conditional instruction in the normal Codex guidance chain. It uses the trusted host/system collaboration mode visible to the agent; it does not parse task wording, scrape the screen, inspect unstable transcript files, or guess from hook `permission_mode`. It cannot override higher-priority instructions or host permissions. It is not a native button event handler, a hard router, or proof that every model will comply.

这是正常规则链中的条件指令，使用智能体收到的真实宿主/系统协作模式，不分析任务措辞、不读屏、不解析不稳定聊天记录，也不使用钩子权限字段猜测。它不是原生按钮事件接口或硬路由，不能覆盖更高优先级要求和宿主权限，也不能保证每个模型遵循。

If the host mode is unknown, automatic entry remains off. In a restricted Plan Mode the plan and checkpoint stay in chat instead of writing files. Full UI toggle routing remains a live acceptance test to perform in the user's actual host after restarting the session.

模式无法确认时不自动启用；计划模式禁止写文件时在聊天中交付。真实界面开关到技能加载的完整链路，仍需在重启会话后于实际宿主中验收。

## Research basis / 调研依据

Checked on 2026-10-21:

- [Superpowers startup bootstrap](https://github.com/obra/superpowers/blob/main/hooks/session-start) injects workflow instructions at session startup; its [hook definition](https://github.com/obra/superpowers/blob/main/hooks/hooks.json) is SessionStart-based. This is a useful precedent for instruction injection, not proof of a Plan-toggle-specific integration.
- [Oh My Codex plan Skill](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/skills/plan/SKILL.md) supports explicit interview/direct/review workflows; its [hooks](https://github.com/Yeachan-Heo/oh-my-codex/blob/main/plugins/oh-my-codex/hooks/hooks.json) connect lifecycle events. The reviewed files did not establish that clicking native Plan Mode selects one chosen interview Skill.
- [Codex hook runtime at the reviewed commit](https://github.com/openai/codex/blob/af91f6ef2cd66ead278ebe7d5751973eef430aee/codex-rs/core/src/hook_runtime.rs) derives `hook_permission_mode` from approval policy. Therefore this implementation deliberately does not equate that field with the collaboration-mode switch. Main-branch code may differ from an installed release.
- Official [AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md) documents loading global/project rules; [Skill guidance](https://learn.chatgpt.com/docs/build-skills) documents explicit invocation and the implicit-invocation policy.

Superpowers 提供了会话初始化时注入流程规则的参考；Oh My Codex 提供访谈与规划衔接的参考，但检查到的文件不能证明二者已经实现用户要求的精确按钮联动。本项目采用官方支持的规则加载机制，另加明确的当前模式条件，避免安装整个框架或依赖不可靠的权限字段。
