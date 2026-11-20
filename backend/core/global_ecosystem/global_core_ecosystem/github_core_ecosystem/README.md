# GITHUB CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Root:** `backend/core/global_ecosystem/global_core_ecosystem/github_core_ecosystem/`

## Mission

GitHub Core is the provider-level control plane and canonical registry for GitHub's 12 API families. It owns provider and family identity, capability metadata, tenant and actor context contracts, policy classification, lifecycle/readiness metadata, discovery and cross-family dependency mapping.

## Canonical entry points

- `manager.py`: Google Core-style application entry point; exposes `GitHubCoreManager` and `get_manager()`.
- `manager.php`: metadata-only PHP interoperability facade with recursive secret-field filtering.
- `catalog.py`: canonical provider identity and the 12-family registry.
- `contracts.py`: tenant context, opaque secret references, readiness and result contracts.
- `request_contracts.py`: safe request-shape validation; rejects credential material.
- `policy.py`: tenant-context checks, capability registration checks and sensitivity classification.
- `module_service.py`: shared read-only service for family-level Core packages.
- `orchestrator.py`: family discovery, health, offerings and dependency mapping.
- `product_catalog.py`: unified family offering inventory.
- `service.py`: provider status and service-level discovery.
- `test_github_core_domains.py` and `tests/`: structural and contract tests.
- `github_*_core_ecosystem/`: the 12 provider-family Core packages.

## Registered families

1. Actions — workflows, runs, jobs, logs, artifacts and workflow permissions
2. Apps — GitHub Apps, installations and app permissions
3. Authentication — token/OAuth/GitHub App authentication boundaries
4. Checks — check runs, check suites and commit status
5. GraphQL — queries, mutations, schemas and API versioning
6. Issues — issues, labels, milestones, assignees and comments
7. Organizations — organizations, teams, members and roles
8. Pull Requests — pull requests, reviews, review requests and merge boundaries
9. Repositories — repositories, branches, commits, contents and releases
10. REST — REST resources, pagination, rate limits and endpoint metadata
11. Security — code scanning, secret scanning, Dependabot and advisories
12. Webhooks — subscriptions, deliveries, signatures, event processing and retries

## Layer ownership

| Layer | Responsibility |
|---|---|
| GitHub Core | provider/family identity, capability metadata, policy, lifecycle, readiness and orchestration |
| API / Integration | credential handling, REST/GraphQL transport, endpoint adapters and response normalization |
| ENGINE | jobs, retries, rate-limit scheduling and webhook execution |
| DATABASE / STORAGE | durable records, transactions, files and artifacts |
| Application | sessions, consent, user workflows and UI |

## Security and readiness rules

1. Tenant and actor identity must come from the authenticated application layer.
2. A registered capability is metadata, not proof of authorization, GitHub permission or account entitlement.
3. Never commit tokens, app private keys, webhook secrets or authorization headers.
4. Use least-privilege GitHub App/PAT permissions and explicit authorization plus audit for writes, merges, dispatches, organization administration and security changes.
5. Family package registration does not prove complete endpoint adapter coverage.
6. Report a live connection only after the API-layer authentication/status check succeeds in the deployed environment.

## Current integration boundary

The repository has shared authenticated REST transport at `backend/integration/provider/github.py` and connector routes at `backend/api/connectors.py`. The current route coverage is partial (authenticated status, account identity, repository listing and repository metadata). The 12 family packages are not evidence of 12 complete API adapters.

Core discovery is metadata-only. It performs no GitHub API calls and does not inspect or resolve credentials.
