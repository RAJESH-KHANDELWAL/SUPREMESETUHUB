# GITHUB APPS CORE ECOSYSTEM

**Scope:** GitHub Apps, installations, app permissions and installation access tokens.

CORE owns family identity, capability metadata, caller-context contracts, lifecycle, policy classification and readiness. API authentication and transport remain in `backend/integration/provider/github.py` and `backend/api/connectors.py`. Persistence, queues and UI remain in their own layers.

API family catalog: `backend/api/global_ecosystem/global_api_ecosystem/github_api_ecosystem/github_apps_api_ecosystem`.

This package is a control-plane contract. It does not claim every family endpoint is implemented or that a live connection is verified.
