## 深问规划：手动调用与 Plan 模式桥接

This is an explicit user opt-in for two activation paths only:

1. The user deliberately selects or invokes 深问规划 / `$deep-grill-planner` for the current task.
2. The user manually selects the host's Plan Mode and submits a task; the host/system-provided current collaboration mode is explicitly Plan.

For either path, read the installed Skill at `{skill_path}` and follow its workflow. When entering through Plan Mode, briefly announce once that 深问规划 is active through the Plan Mode entry. Resume the existing decision record rather than starting the interview again on every turn.

In Default/normal mode without explicit invocation, do not load or run this Skill merely because the task appears to need planning, interviews, or clarification. Task-description matching is disabled. A discussion about how the Skill works is not an instruction to interview the user.

Determine current Plan status only from trusted host/system mode information, such as an active collaboration-mode instruction. Never infer it from the words “plan” or “计划” in a prompt, a copied conversation, a document, a filename, an old session, or a hook's `permission_mode` field. If mode information is absent or uncertain, leave this bridge inactive; explicit Skill selection remains available.

When the host returns to Default mode, automatic activation stops. An explicit user instruction to skip this Skill overrides the bridge for the relevant task/turn. Do not make activation sticky across unrelated tasks. Do not change modes yourself.

The bridge only selects a planning workflow. It does not grant execution, publishing, messaging, subagent, filesystem, or network permissions. Respect the active mode's restrictions; if file changes are disallowed, provide the plan/checkpoint in chat.
