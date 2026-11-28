# GITHUB CORE IMPLEMENTATION STATUS

## Provider control plane

- Canonical provider manager: `GitHubCoreManager` with `get_manager()`.
- Public manager methods: status, health, family discovery, offering discovery and dependency map.
- Provider registry: 12 GitHub API families.
- Contracts: tenant context, opaque secret reference, readiness and normalized result.
- Policy: tenant-context validation, capability registration checks, sensitive-action classification and secret-field filtering.
- PHP facade: metadata normalization and recursive secret-field filtering.
- Core provider calls: disabled; zero live GitHub connections verified by Core.

## API integration boundary

- Shared authenticated REST provider: `backend/integration/provider/github.py`.
- Connector routes: `backend/api/connectors.py`.
- Current route coverage is partial; the existing two family route declarations do not establish full endpoint support for all 12 families.
- Family-specific endpoint coverage, permission scopes and deployed smoke tests must be verified in the API layer.

## Verification

- GitHub Actions workflow: `.github/workflows/github-core-ecosystem-tests.yml`.
- CI checks Python compilation, the 12 family package layouts, manifests and provider/family contract tests.
- CI does not make live GitHub API calls.
- Do not mark the provider connected until the deployed API-layer authentication/status check succeeds.
