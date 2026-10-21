# Design / 设计

Context → shared evidence and decision record → available material questions → focused challenge → readiness → planning pack → authorized next action.

上下文 → 事实与决策共享记录 → 当前可回答的重要问题 → 反向审查 → 就绪检查 → 规划产物 → 已授权的下一步。

Dependencies determine question order. Materiality determines which branches need user attention. Review checks the premises. Readiness determines when enough is known. Authorization independently determines what may happen next.

依赖决定顺序，重要程度决定是否询问用户，审查检查前提，就绪条件决定何时结束，授权范围单独决定接下来允许做什么。

Activation is explicit-only. An optional, user-enabled AGENTS.md bridge routes the trusted current Plan Mode into this Skill; it never matches the task description to activate it. See [Plan Mode bridge](plan-mode.md) for the mechanism, research basis and limits.

默认仅手动调用；用户可主动配置规则桥接，让宿主真实 Plan 模式进入本 Skill，不按任务描述触发。机制、参考实现与边界见桥接说明。

## Upstream changes / 上游差异

The pinned Deep Interview already incorporates Grilling through `--frontier`. This project adapts that overlap rather than claiming a new fusion. It removes `.claude` settings requirements, OMC state calls, forced model choices, fixed challenge-round triggers, and mandatory OMC execution handoffs.

固定版本 Deep Interview 已通过 `--frontier` 吸收 Grilling，本项目基于已有融合改编，不把这点宣称为原创。移除 `.claude` 配置、OMC 状态工具、指定模型、固定轮次挑战及 OMC 专属执行衔接。

Scores are optional heuristics; averages cannot hide critical gaps. Existing execution authorization is retained; plan-only tasks stop at planning. Changed prerequisites require affected decisions to be rechecked. Inaccessible existing-system evidence remains uncertain rather than being relabeled as a new-system task.

评分可选，平均分不能掩盖关键缺口。复用已有执行授权，纯规划任务停在规划。前置条件改变时复核后续决策，无法获取既有系统信息时保留不确定性。

## Limits / 边界

This is a model-interpreted text workflow, not an enforcement engine. It cannot guarantee every model's judgment or factual correctness. Checkpoints are ordinary files, not automatic cross-device sync. Native planning internals remain controlled by the host. Office formatting follows the user's requirements and the appropriate document workflow.

这是由模型解释的文本流程，不能保证所有模型的判断和事实准确性。进度记录是普通文件，不是自动跨设备同步；不改变宿主原生计划逻辑。Office 格式按用户要求及对应文档流程处理。
