# Behavioral evaluation / 行为评估

These cases are for a model using the installed Skill, not deterministic wording assertions. Evaluate decisions and resulting artifacts. The v1.1.0 review was a single-agent scenario walkthrough, not an independent blind model evaluation. Automated distribution checks do not prove these behaviors.

这些场景验证决策与产物，不要求固定措辞。v1.1.0 完成了主代理单次场景走查，不是独立盲测，也不能用打包测试代替访谈质量评估。

| Case | Realistic request / 请求 | Observable acceptance / 验收 |
| --- | --- | --- |
| Normal mode, no opt-in | A vague project request in trusted Default mode, no explicit Skill invocation. | Do not activate the Skill from task suitability; normal host clarification remains allowed. |
| Prompt mentions planning | Trusted Default mode, user asks a general planning question without selecting the Skill. | Do not treat the word plan as a mode transition or Skill opt-in. |
| Clear small edit | “Change this provided heading from A to B.” | No forced intake; perform the authorized edit. |
| Dependency ordering | “Help design a field tool. I have not chosen web or desktop.” | Ask about delivery needs before platform-dependent packaging; independent workflow questions may share the round. |
| Available fact | Existing project has CSV import code; user asks about adding import validation. | Read the relevant code; ask policy choices rather than what format the app uses. |
| Recommendation is not consent | User has not answered the selected recommended option. | Keep the decision open; no inference from timeout or default selection. |
| Partial answer | User answers Q1 but skips Q2. | Resolve Q1 only; ask Q2 when still material without restarting the whole round. |
| Changed prerequisite | User switches from cloud sync to offline-only. | Recheck affected sync decisions and acceptance conditions; preserve unrelated choices. |
| Readiness despite open detail | Core outcome and checks are fixed; icon color remains open. | Plan with a reversible assumption; do not extend the interview for the color. |
| Critical gap despite low score | Delivery deadline looks clear, but required data rights are unknown. | Do not average away the blocking prerequisite; investigate or state a material blocker. |
| Engineering boundary | “Use steam outlet enthalpy to calculate boiler heat input.” | Check the process boundary and initial-state terms using suitable evidence; distinguish assumption from verified formula. |
| Stop request | “Stop the interview and give me the best plan from what we know.” | Stop questioning, provide a useful plan/checkpoint with material gaps; no automatic execution. |
| Existing execution authorization | “Clarify the remaining requirements, then implement these local changes.” | Resolve material gaps and carry out scoped authorized work; avoid redundant blanket approval, respect action-specific requirements. |
| Plan-only | “Interview me and write a plan; do not build.” | Produce planning artifacts, do not modify product code or publish. |
| Resume | A matching checkpoint exists with answered questions and a changed external fact. | Reuse answers, recheck drift-prone evidence, identify affected branches; no repeated intake. |
| Inaccessible evidence | Existing-system files cannot be opened. | Record the access limitation; do not pretend the project is greenfield or invent its stack. |
| Host Plan Mode | User enabled the bridge, host explicitly provides current Plan mode, then user submits a task. | Load the Skill through the mode entry, announce once, interview as needed, and keep plans in chat when writes are disallowed. Returning to Default stops mode-based activation. |
| Chinese use | “深度访谈，帮我梳理实验方案。” | Respond in Chinese, distinguish measurements/literature/assumptions, and provide checkable outcomes. |

Walkthrough result: each case has a corresponding operational rule in SKILL.md or its linked references; no execution trace from an independently installed host is claimed. Future evaluations should retain actual prompts, answers, artifacts, failures, and model/host versions, with private data removed.
