# GITHUB AUTHENTICATION CORE ECOSYSTEM

**Scope:** Fine-grained personal access tokens, OAuth flows, GitHub App authentication and token handling.

CORE owns family identity, capability metadata, caller-context contracts, lifecycle, policy classification and readiness. API authentication and transport remain in `backend/integration/provider/github.py` and `backend/api/connectors.py`. Persistence, queues and UI remain in their own layers.

API family catalog: `backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_authentication_api_ecosystem`.

This package is a control-plane contract. It does not claim every family endpoint is implemented or that a live connection is verified.
