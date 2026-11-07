# GITHUB API ECOSYSTEM

Canonical provider-owned catalog for GitHub's official REST and GraphQL APIs. The provider folder follows the same root naming convention as Google, AWS, Apple, Adobe, DeepSeek and DigitalOcean.

## API family structure

- `github_rest_api_ecosystem/` — REST API: REST resources, pagination, rate limits and endpoint-specific operations.
- `github_graphql_api_ecosystem/` — GRAPHQL API: GraphQL queries, mutations, schemas and API versioning.
- `github_repositories_api_ecosystem/` — REPOSITORIES API: Repositories, branches, commits, trees, blobs, contents and releases.
- `github_issues_api_ecosystem/` — ISSUES API: Issues, labels, milestones, assignees and issue comments.
- `github_pull_requests_api_ecosystem/` — PULL REQUESTS API: Pull requests, reviews, review comments, review requests and merge operations.
- `github_actions_api_ecosystem/` — ACTIONS API: Workflows, workflow runs, jobs, logs, artifacts and workflow permissions.
- `github_apps_api_ecosystem/` — APPS API: GitHub Apps, installations, app permissions and installation access tokens.
- `github_authentication_api_ecosystem/` — AUTHENTICATION API: Fine-grained personal access tokens, OAuth flows, GitHub App authentication and token handling.
- `github_webhooks_api_ecosystem/` — WEBHOOKS API: Webhook subscriptions, deliveries, signatures, event processing and retries.
- `github_checks_api_ecosystem/` — CHECKS API: Check runs, check suites and commit status reporting.
- `github_security_api_ecosystem/` — SECURITY API: Code scanning, secret scanning, Dependabot alerts and security advisories.
- `github_organizations_api_ecosystem/` — ORGANIZATIONS API: Organizations, teams, members, roles and organization-level controls.

## Shared category mappings

- `backend/api/global_ecosystem/global_api_ecosystem/global_developer_api_ecosystem/github_developer_api_ecosystem/`
- `backend/api/global_ecosystem/global_api_ecosystem/global_software_api_ecosystem/github_software_api_ecosystem/`
- `backend/api/global_ecosystem/global_api_ecosystem/global_tools_api_ecosystem/github_tools_api_ecosystem/`

## Existing implementation boundary

`backend/api/connectors.py` currently provides public-repository status checking. That must not be represented as full authenticated GitHub API connectivity. The provider catalog and family folders are architecture/documentation scaffolds; they do not execute API calls.

## Integration and security requirements

- Use GitHub's official API documentation as the source of truth for endpoints, permissions, scopes and API versions.
- Keep tokens and app private keys in environment variables or a managed secret store; never commit secrets.
- Apply least-privilege permissions and repository/organization scoping.
- Handle pagination, rate limits, secondary rate limits, retries and webhook signature verification.
- Add endpoint-specific tests before enabling write operations.

Live connection verified: **No**.

## Backend API connection

The backend now includes an authenticated GitHub REST provider at `backend/integrations/providers/github.py`, registered as `GITHUB` in the integration registry.

### Required runtime secret

Set **one** of these environment variables in the backend hosting environment:

- `GITHUB_TOKEN` (recommended), or
- `GH_TOKEN`

Use a fine-grained personal access token or GitHub App installation token. For the currently implemented read-only routes, grant access only to the required account/repositories and **Metadata: Read-only**. Add further permissions only when additional API operations are implemented. Never paste the token into source files, commit it, or send it in chat.

### Implemented backend routes

- `GET /api/v1/connectors/github/status` — validates the token against `GET /user` and the configured repository.
- `GET /api/v1/connectors/github/api/user` — returns the authenticated GitHub account identity.
- `GET /api/v1/connectors/github/api/repositories` — lists repositories visible to the token.
- `GET /api/v1/connectors/github/api/repository/{owner}/{repo}` — reads repository metadata and granted permissions.

The repository checked by the status route defaults to `RAJESH-KHANDELWAL/SUPREMESETUHUB`; override with `SUPREMESETUHUB_GITHUB_REPOSITORY` if required.

### Activation and verification

After setting the secret in the backend runtime, restart/redeploy the backend and call `/api/v1/connectors/github/status`. A successful authenticated response reports `status: CONNECTED` and `live_connection_verified: true`. If the token is missing, the route reports `NEEDS_CONFIGURATION`.

Current implementation is read-only. Repository writes, issues, pull requests, Actions, webhooks, GraphQL and security operations require separate endpoint implementations, least-privilege permissions and tests. The 12 API-family directories remain architecture/documentation scaffolds until those operations are built.
