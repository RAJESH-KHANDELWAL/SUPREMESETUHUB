# Microsoft Product Ecosystem Standard

- Preserve all existing Microsoft product-family IDs and folder paths.
- Keep provider-level catalog, domain taxonomy, orchestration, policy, service, and manager at the Microsoft Core root.
- Reuse the existing Microsoft API ecosystem for transport; do not create duplicate API clients.
- Use `manager.py:get_manager()` as the canonical Python entry point.
- Keep PHP as a thin metadata facade; no direct provider API or database access.
- Do not store credentials, tokens, secrets, or tenant data in catalogs.
- Catalog metadata must never be presented as proof of live connectivity or entitlement.
- Add only necessary source, contract, documentation, and tests; avoid placeholders and duplicate registries.
