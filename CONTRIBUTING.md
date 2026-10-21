# Contributing / 贡献

Report a concrete request, non-private context, actual behavior, and expected decision behavior. English and Chinese are welcome. Do not post credentials or private transcripts. For workflow changes, update a realistic case in `tests/scenarios.md`; avoid tests that require one generated phrase.

请提供具体请求、可公开的上下文、实际表现及期望的决策行为。中英文均可，请勿发布密钥或私人聊天。修改流程时补充真实场景，避免只检查固定措辞。

Run `python3 -m unittest discover -s tests -v` and `python3 scripts/build.py`. Inspect both ZIPs and retain bundled licenses. Keep versions aligned in the manifest, Skill, docs, and release. Do not commit generated `dist/`, session checkpoints, temporary dependencies, or caches.

验证并打包后检查两个 ZIP 和许可，版本号保持一致。不要提交打包产物、访谈记录、临时依赖或缓存。
