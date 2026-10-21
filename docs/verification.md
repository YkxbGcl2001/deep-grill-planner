# Verification / 验证

Version: 1.0.0. Review date: 2026-10-21.

## Executable checks / 可执行检查

`python3 -m unittest discover -s tests -v` checks complete offline copying, non-overwrite behavior, symlink destination handling, invalid-source handling, recursive destination rejection, byte-reproducible packages, ZIP content integrity, license inclusion, checksums, marketplace/Skill resolution, version alignment, and relative documentation links.

标准库测试检查离线完整复制、不覆盖已有安装、符号链接目标处理、无效来源、递归目标拒绝、可复现打包、ZIP 完整性、许可、校验值、插件路径、版本一致性及文档相对链接。

The bundled OpenAI Skill Creator `quick_validate.py` is also used during release preparation. It checks the Skill structure/frontmatter and unfinished scaffold markers; it does not assess model judgment.

发布准备还使用 OpenAI Skill Creator 的基础检查器，检查 Skill 结构、元数据及未完成占位，不能据此证明模型判断质量。

## Behavior review / 行为审阅

The 15 cases in [scenarios.md](../tests/scenarios.md) were walked through by the authoring agent against the completed instructions. This is a review of expected routing, decision updates, stopping, language, and consent behavior. It is not an independent blind evaluation or proof that every host/model follows the workflow.

主代理对 15 个场景进行规则走查，检查路由、决策更新、结束条件、语言和授权处理；这不是独立盲测，不保证所有宿主或模型的行为。

## Platform limits / 平台边界

Local installation copies and package round trips are tested in temporary directories. The plugin manifest and marketplace paths are checked against the official packaging documentation. End-to-end ChatGPT Work UI installation and cross-platform Windows execution are not yet verified. The workflow requires a capable host model and its available tools; it does not enforce behavior itself.

已在临时目录验证本地复制与包内容，按官方说明检查插件清单及来源路径。尚未完成 ChatGPT Work 界面端到端安装及 Windows 实机运行验证，文本流程本身不强制约束宿主模型。

## Source retention / 来源保留

Pinned upstream versions, source-file hashes, original archive hashes, and retrieval URLs are retained in [provenance.json](provenance.json); both original MIT notices are bundled. Full upstream repository snapshots and duplicate archives used for research are intentionally excluded from the release and removed from the local project after adaptation. No private source conversation or machine-specific path is required to build or install this project.

保留固定版本、来源及原始压缩包校验值和完整 MIT 许可；研究时下载的两个完整上游仓库及重复压缩包已在改编完成后清理，不进入发布包。构建和安装不依赖私人对话或本机路径。
