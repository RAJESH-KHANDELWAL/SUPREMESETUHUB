# DeepSeek Ecosystem

Provider-scoped catalog, capability registry, safe request planning, configuration readiness, and validation for DeepSeek.

## Layer ownership

- Ecosystem: provider discovery, catalog metadata, request planning.
- API: transport, endpoint contracts, authentication middleware and response parsing.
- CORE: shared contracts and policies.
- ENGINE: execution orchestration and lifecycle.
- DATABASE: persistence and data access.
- Integration: provider adapter and configuration readiness.
- Security / Identity: authorization, secret storage and audit controls.

This package does not duplicate those layers and does not make live DeepSeek network calls.

## Included modules

- `constants.py`, `models.py`: provider identifiers and typed records.
- `catalog.py`, `registry.py`: models, products and capability registry.
- `validation.py`: operation validation, nested-secret rejection and safe summaries.
- `service.py`: catalog access and metadata-only request planning.
- `health.py`: key-presence readiness without exposing credential values.
- `tests/test_ecosystem.py`: unit tests.

Run tests from repository root:

```bash
python -m unittest backend.global_ecosystem.deepseek_ecosystem.tests.test_ecosystem -v
```

Configure `DEEPSEEK_API_KEY` only through a server-side secret manager. Never place credentials in payloads or source files. A request plan is not executed or sent to DeepSeek.
