# 安装说明

[English](installation.md)

## Codex 独立 Skill

需要能加载本地 Agent Skills 的宿主。只有以下可选安装方式需要 Git 和 Python 3.9 及以上版本：

```sh
git clone --branch v1.1.0 --depth 1 https://github.com/YkxbGcl2001/deep-grill-planner.git
cd deep-grill-planner
python3 scripts/install.py
```

仅将 `skills/deep-grill-planner/` 复制到 `~/.agents/skills/deep-grill-planner`，不改配置、不装依赖、不联网、不覆盖已有目录。其他扫描位置可以指定父目录：

```sh
python3 scripts/install.py --dest /absolute/path/to/skills
```

使用旧 Codex 目录的环境可指定 `~/.codex/skills`，不要在多个位置重复安装同名副本。实际扫描目录由宿主决定。

手动方式：下载独立 Skill ZIP，核对校验值，将 `deep-grill-planner/` 复制到支持的技能目录，最终应存在 `deep-grill-planner/SKILL.md`。Windows 可用 `py -3` 运行可选工具。

安装后新建聊天，通过 `$deep-grill-planner` 或技能选择器调用。找不到时检查路径并重启宿主。普通 ChatGPT 网页聊天不会自动扫描电脑上的 Skill 文件夹。

## ChatGPT Work / Codex 桌面插件

仓库根目录采用仅含技能的可移植插件格式，插件来源目录位于 `.agents/plugins/marketplace.json`。

支持相应功能的 Codex CLI 可以运行：

```sh
codex plugin marketplace add YkxbGcl2001/deep-grill-planner --ref v1.1.0
```

或克隆仓库后添加本地绝对路径：

```sh
codex plugin marketplace add /absolute/path/to/deep-grill-planner
```

打开桌面 Plugins Directory，选择 Deep Grill Planner 来源，安装插件，并新建已启用插件的聊天。来源未出现时重启桌面应用。不同界面的调用语法可能不同，请使用宿主实际提供的选择器。

不需要 MCP 连接、密钥、钩子或后台服务。添加来源和安装插件是两个步骤。发布 GitHub 不代表上架 OpenAI 通用公共插件目录。本版本已检查包结构及路径，尚未完成 ChatGPT Work 界面的端到端安装验证。不支持自定义来源时，可改用支持本地 Agent Skills 的宿主。

## 下载和校验

- `deep-grill-planner-skill-v1.1.0.zip`：独立 Skill、参考资料、模板和许可。
- `deep-grill-planner-plugin-v1.1.0.zip`：插件、来源目录、中英说明、工具和测试。
- `SHA256SUMS.txt`：两个包的 SHA-256。
- GitHub 自动源码压缩包：完整版本化仓库。

在下载目录核验：

```sh
# macOS
shasum -a 256 -c SHA256SUMS.txt
# Linux
sha256sum -c SHA256SUMS.txt
```

Windows 使用 `Get-FileHash <zip-file> -Algorithm SHA256`，与清单对应行比较。校验值用于检查字节一致性，不是发布者数字签名。

## 更新和卸载

保留自己的修改后，只移走或删除原 `deep-grill-planner` 安装目录，再安装所选版本。工具不提供覆盖选项。卸载独立 Skill 时删除同一目录即可，不存在后台服务或配置项。插件通过宿主卸载，不再需要来源时再单独移除来源。

访谈记录在任务工作区中，可能包含私人信息；分享前应检查。安装不会发布这些记录。

本说明于 2026-10-21 对照官方 [Build skills](https://learn.chatgpt.com/docs/build-skills) 和 [Package your plugin](https://developers.openai.com/plugins/build/plugins) 编写，宿主支持变化时以官方说明为准。

## 手动开启与计划模式

显示名为「深问规划」，调用标识为 `$deep-grill-planner`。隐式匹配已关闭；普通模式只在你明确选择技能时启用。

安装后主动开启可选桥接：

```sh
python3 scripts/plan_bridge.py
```

默认只向 Codex 全局 `AGENTS.md` 添加受标记保护的规则段，保留已有要求。自定义路径、预览和撤销见 [Plan 桥接说明](plan-mode.md)。新建会话、手动打开计划模式并发送任务后，规则根据宿主真实模式引导加载技能。模式未知时不自动启用，退出计划模式后也不继续自动触发。

桥接不监听按钮、不修改产品内部、不放宽任何权限，且不是硬性行为保证。普通 ChatGPT 网页或未加载本地 AGENTS.md 的宿主不能依赖此方式。
