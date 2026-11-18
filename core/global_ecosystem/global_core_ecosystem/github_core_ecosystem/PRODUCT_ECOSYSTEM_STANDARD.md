# GitHub Product CORE Ecosystem Standard

Each of the 12 family packages contains exactly ten folders: authentication/, capabilities/, docs/, events/, lifecycle/, models/, schemas/, security/, services/ and tests/. Each package also contains README.md, __init__.py, contracts.py, service.py and ecosystem_manifest.json.

Folder ownership: authentication defines caller-context contracts only; capabilities defines metadata; docs records boundaries; events defines event contracts; lifecycle defines states; models defines safe descriptors; schemas exposes request validation; security defines guardrails; services exposes Core validation; tests verifies contracts.

Provider root owns catalog.py, contracts.py, request_contracts.py, policy.py, module_service.py, service.py, orchestrator.py, product_catalog.py and manifests. API transport/authentication, secret resolution, persistence, job execution and UI must not be duplicated in CORE.
