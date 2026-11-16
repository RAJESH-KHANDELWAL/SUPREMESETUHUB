# Global AI Product CORE Ecosystem Standard

Each AI provider facade has exactly ten folders: authentication/, capabilities/, docs/, events/, lifecycle/, models/, schemas/, security/, services/ and tests/. Each includes README.md; package root includes README.md, __init__.py, catalog.py, contracts.py, service.py and ecosystem_manifest.json.

Facade packages own identity and canonical CORE/API references only. Provider-specific CORE owns detailed product taxonomy. API owns auth/transport. ENGINE owns inference execution.

Adjacent non-AI partners must remain in ADJACENT_INTEGRATIONS and never be counted in AI_PROVIDERS. Their legacy folder names are retained until a separately reviewed migration.

Root modules: catalog.py, contracts.py, request_contracts.py, policy.py, provider_service.py, orchestrator.py, ecosystem_service.py, product_catalog.py and domain_catalog.py. Preserve the existing executor-injected service.py contract.
