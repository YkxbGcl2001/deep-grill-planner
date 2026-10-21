# Focused challenge review

Review the current scope, evidence, and decisions. Choose the checks relevant to the task:

| Check | Useful question | Resolve by |
| --- | --- | --- |
| Consistency | Do two confirmed requirements conflict? | Explain the conflict and obtain the material trade-off |
| Boundary | What inputs, outputs, operating conditions, or exclusions change the result? | Inspect artifacts, define the boundary, then ask only for missing decisions |
| Assumptions | Is scale, accuracy, audience, budget, or a causal relationship assumed? | Verify evidence or label the assumption and its impact |
| Simplicity | Could fewer parts achieve the accepted outcome? | Compare a concrete simpler alternative and its limitations |
| Concepts | Are different names being used for the same thing, or one name for different things? | Define the core entities in ordinary domain language |
| Acceptance | Could another person check whether this is done? | Pair each material outcome with observable evidence |
| Feasibility | Does the plan require an unavailable capability or unverified data? | Verify the capability or make the gap explicit |

Return only material findings, with evidence, effect on the plan, and resolution. “No unresolved material blocker found in the reviewed scope” is a valid outcome; it is not a certification of safety or completeness.

For engineering or research tasks, distinguish measured data, model assumptions, literature-derived values, and proposed experiments. Check units, physical boundaries, and what the available evidence can actually establish. For example, calculating a heat requirement from a final-state enthalpy alone may omit the initial-state enthalpy and other terms. Identify the actual process boundary before choosing a formula. Use the host's research workflow when precise or high-stakes facts require verification.

Keep review proportional. Do not force a dissent round or a fixed number of objections. A settled user preference does not need a scientific justification; a claim about the world does need appropriate evidence.
