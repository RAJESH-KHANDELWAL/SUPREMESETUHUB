# GITHUB CORE ECOSYSTEM

Canonical provider-level CORE control plane for GitHub's 12 API families.

## Mission
Provider/family identity, capability registration, tenant and caller-context contracts, policy classification, lifecycle metadata, readiness, discovery and cross-family orchestration.

## Registered families
- **Actions** — Workflows, workflow runs, jobs, logs, artifacts and workflow permissions
- **Apps** — GitHub Apps, installations, app permissions and installation access tokens
- **Authentication** — Fine-grained personal access tokens, OAuth flows, GitHub App authentication and token handling
- **Checks** — Check runs, check suites and commit status reporting
- **GraphQL** — GraphQL queries, mutations, schemas and API versioning
- **Issues** — Issues, labels, milestones, assignees and issue comments
- **Organizations** — Organizations, teams, members, roles and organization-level controls
- **Pull Requests** — Pull requests, reviews, review comments, review requests and merge operations
- **Repositories** — Repositories, branches, commits, trees, blobs, contents and releases
- **REST** — REST resources, pagination, rate limits and endpoint-specific operations
- **Security** — Code scanning, secret scanning, Dependabot alerts and security advisories
- **Webhooks** — Webhook subscriptions, deliveries, signatures, event processing and retries

## Existing API integration
The repository contains an authenticated GitHub REST provider at `backend/integration/provider/github.py` and routes in `backend/api/connectors.py`. Exposed routes cover authenticated connection status, account identity, repository listing and repository metadata. CORE references these components and does not duplicate them or inspect token values.

The 12 API family directories are not proof of 12 complete endpoint adapters. Family-specific endpoint coverage, scopes and live smoke tests must be verified in the API layer.

## Layer ownership
| Layer | Responsibility |
|---|---|
| CORE | identity, capability metadata, policy, lifecycle, readiness, orchestration |
| API / Integration | token authentication, REST/GraphQL transport, endpoint adapters, response normalization |
| ENGINE | jobs, retries, rate-limit scheduling, webhook execution |
| DATABASE / STORAGE | structured records, transactions, files and artifacts |
| Application | sessions, consent, workflows and UI |

Never commit tokens, app private keys or webhook secrets. Use least-privilege permissions and explicit authorization for writes, merges, workflow dispatches, organization administration and security changes.
