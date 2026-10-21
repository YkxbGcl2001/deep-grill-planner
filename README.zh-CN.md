# 深问规划 · Deep Grill Planner

**简体中文** · [English](README.md) · [安装说明](docs/installation.zh-CN.md) · [版本下载](https://github.com/YkxbGcl2001/deep-grill-planner/releases)

**问清真正会改变方案的问题，再形成可以执行的计划。**

这是一个独立的深度需求访谈与规划 Agent Skill，结合 Grilling 的决策树分轮提问，以及 Deep Interview 的假设挑战和就绪检查。访谈使用智能体已有能力，不依赖 OMC、API 密钥、服务器或 Python。

## 主要能力

- 先阅读上下文，区分可以自行查明的事实和需要用户选择的决策。
- 同轮询问互不依赖的问题，提供推荐与理由；有前置条件的问题留到后续。
- 支持 Quick、Standard、Deep 三档深度，按任务调整，不凑题数。
- 复用已有答案；前置决策改变时复核受影响的后续决定。
- 检查重要假设、矛盾和验收条件。
- 剩余不确定性不再实质影响实施时结束访谈。
- 输出需求、决策记录、假设与待确认事项，以及实施计划。
- 支持中文、英文、可选进度记录和可选启发式评分。
- 尊重已有授权；仅要求访谈或规划时不自动开始执行。

它不会修改原生 Plan Mode 或提问上限。Skill 没有自动执行的安装钩子、遥测或后台服务；可选工具只复制本地文件或修改明确指定的规则文件；执行用户任务时，宿主智能体可以使用原有工具。

## 安装

在支持本地 Skill 的 Codex 环境中，克隆后运行可选安装工具（Python 3.9 及以上，仅用标准库）：

```sh
git clone https://github.com/YkxbGcl2001/deep-grill-planner.git
cd deep-grill-planner
python3 scripts/install.py
```

默认安装至 `~/.agents/skills/deep-grill-planner`，已有目录不会被覆盖。Windows 可用 `py -3 scripts/install.py`。也支持手动复制及指定其他目录。安装后新建聊天，未识别时再重启宿主。

作为 ChatGPT Work / Codex 桌面插件使用时，在支持该功能的 CLI 中添加仓库来源：

```sh
codex plugin marketplace add YkxbGcl2001/deep-grill-planner --ref v1.1.0
```

随后在桌面 Plugins Directory 选择该来源，安装 Deep Grill Planner 并新建聊天。这是通过 GitHub 分发的插件，尚未上架 OpenAI 通用公共插件目录；可用性取决于宿主和账号。完整步骤及验证范围见[中文安装说明](docs/installation.zh-CN.md)。

也可以从 [v1.1.0](https://github.com/YkxbGcl2001/deep-grill-planner/releases/tag/v1.1.0) 下载独立 Skill ZIP、插件 ZIP 和校验清单。安装独立 Skill 时，只复制 Skill 文件夹，不要安装整个仓库。

## 手动开启与计划模式联动

**已关闭根据任务描述自动启用。** 普通模式下，只有明确选择「深问规划」或调用 `$deep-grill-planner`，才进入该流程。

安装 Skill 后，可以主动启用可选的 **Plan 模式桥接**：

```sh
python3 scripts/plan_bridge.py
```

它会向 Codex 的 `AGENTS.md` 添加一小段可移除的条件规则，保留原有内容。新建 Codex 会话后，**手动打开计划模式并发送任务**，只要宿主明确提供当前为 Plan 模式，该规则就会引导智能体加载深问规划。回到普通模式后，不再自动进入。不会根据任务措辞、历史记录或钩子权限字段猜测模式。

这是指令层联动，不是监听按钮的原生事件接口，也不是二进制强制执行。它依赖宿主加载规则及模型遵循规则，尚未完成真实界面开关的端到端验证。安装、撤销和调研依据见 [Plan 模式桥接说明](docs/plan-mode.md)。

中文名用于展示，内部标识仍为 `deep-grill-planner`，原调用方式与仓库链接继续有效。

## 使用示例

```text
使用 $deep-grill-planner（深问规划），帮我澄清离线现场数据采集工具的需求。
先阅读已有资料，每轮只问真正影响方案的问题，提供推荐和理由，最后形成计划，暂不实施。
```

```text
用 $deep-grill-planner 的 Deep 模式检查这份实验方案。
区分实测数据、文献参数和假设，重点检查物理边界与验收条件。
```

```text
用 $deep-grill-planner 的 Quick 模式比较两个方案。
能查到的事实请先查证，不要重复询问已有信息。
```

`$skill-name` 是 Codex 的调用形式，其他宿主以实际支持的选择器、插件提及或自然语言方式为准。

例如，讨论一个模糊的现场工具时，先确定核心工作流程和离线需求。只有同步需求成立后，再询问同步冲突策略，避免提前抛出用户尚无法判断的问题。

## 文件与开发

- [完整 Skill](skills/deep-grill-planner/SKILL.md)：规则正文采用英文，要求按用户语言响应。
- [设计说明](docs/architecture.md)
- [验证说明](docs/verification.md)
- [行为场景](tests/scenarios.md)
- [固定版本来源记录](docs/provenance.json)

```sh
python3 -m unittest discover -s tests -v
python3 scripts/build.py
```

辅助工具只用 Python 标准库，生成包和校验值位于 `dist/`，Skill 没有必须执行的辅助程序。

## 许可与致谢

MIT 许可。改编自 [Matt Pocock 的 Grilling](https://github.com/mattpocock/skills) 和 [Yeachan Heo 的 Deep Interview](https://github.com/Yeachan-Heo/oh-my-claudecode)，在[第三方许可](THIRD_PARTY_NOTICES.md)和安装包中保留版权与许可原文。原作者未对本项目作出背书。

欢迎中英文贡献，请提供具体访谈问题及期望行为，不要发布私人聊天或密钥。参见 [CONTRIBUTING.md](CONTRIBUTING.md)。
