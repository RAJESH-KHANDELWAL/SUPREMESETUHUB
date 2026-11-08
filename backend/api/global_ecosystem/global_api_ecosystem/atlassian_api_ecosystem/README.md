# ATLASSIAN API ECOSYSTEM

Canonical provider root for Atlassian cloud products and developer/business workflow APIs in SUPREMESETUHUB.

## Provider structure

- `atlassian_api_ecosystem.py` — provider metadata and API-family listing.
- `atlassian_jira_api_ecosystem/` — Jira Cloud Platform.
- `atlassian_confluence_api_ecosystem/` — Confluence Cloud.
- `atlassian_jira_service_management_api_ecosystem/` — Jira Service Management.
- `atlassian_bitbucket_api_ecosystem/` — Bitbucket Cloud.
- `atlassian_admin_identity_api_ecosystem/` — Atlassian Administration and identity APIs.

Shared provider adapter: `backend/integrations/providers/atlassian.py`.

Shared integration registration: `backend/integrations/registry.py` (provider key: `ATLASSIAN`).

## Product/API overview

| API family | Scope | Access boundary |
|---|---|---|
| Jira Cloud | Projects, issues, workflows, users, comments and work management | Site permissions, OAuth scopes, pagination and API limits |
| Confluence Cloud | Spaces, pages, content, attachments and search | Space/page permissions and content restrictions |
| Jira Service Management | Service projects, customer requests, queues and service workflows | Product-specific scopes and agent/customer permissions |
| Bitbucket Cloud | Workspaces, repositories, pull requests, commits and pipelines | Workspace/repository permissions and Bitbucket scopes |
| Administration & identity | Organization, managed accounts, groups and directory operations where available | Restricted organization/admin privileges |

## Setup configuration

The readiness scaffold recognizes these alternative server-side configuration groups:

**Atlassian OAuth group**
- `ATLASSIAN_CLIENT_ID`
- `ATLASSIAN_CLIENT_SECRET`
- `ATLASSIAN_REDIRECT_URI`
- `ATLASSIAN_SITE_URL`

**Bitbucket OAuth group**
- `BITBUCKET_CLIENT_ID`
- `BITBUCKET_CLIENT_SECRET`
- `BITBUCKET_REDIRECT_URI`

Use the authentication method supported by the selected product and API. OAuth scopes, tenant/site URL, product entitlements and administrator approval must be confirmed before enabling each capability. Do not assume one credential set grants access to every Atlassian product.

## Security and operations

- Store client secrets and tokens only in server-side environment configuration or a managed secret store.
- Never commit credentials or expose tokens in browser code, API responses or logs.
- Request least-privilege scopes and enforce tenant, site, project, space and workspace permissions.
- Implement pagination, rate-limit handling, bounded retries, timeouts and structured error handling.
- Keep read and write permissions separate; require explicit confirmation for destructive or externally visible operations.
- Audit sensitive administrative actions without logging authorization headers or secrets.

## Status semantics

- `NEEDS_CONFIGURATION`: no complete supported OAuth configuration group is present.
- `CONFIGURED_NOT_VERIFIED`: a complete configuration group is present; credentials and API connectivity have not been tested.
- `CONNECTED`: only use after token exchange and an API-family smoke test succeed in the deployed environment.

The adapter currently checks configuration presence only. It does not exchange tokens, validate secrets, or make live Atlassian API requests. Each product family remains a catalog/documentation scaffold until separately implemented and tested.
