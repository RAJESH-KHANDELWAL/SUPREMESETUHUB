# ATLASSIAN API ECOSYSTEM

Provider-owned catalog for Atlassian cloud products and API surfaces.

## Product/API areas

| Area | Intended scope | Important boundary |
|---|---|---|
| Jira Cloud Platform | Projects, issues, workflows, users, comments and work management | Respect site permissions, scopes, pagination and product API limits |
| Confluence Cloud | Spaces, pages, content, attachments and search | Respect space/page permissions and content restrictions |
| Jira Service Management | Service projects, requests, queues and customer-service workflows | Request and agent operations have distinct permissions and scopes |
| Bitbucket Cloud | Workspaces, repositories, pull requests, commits and pipelines | Workspace/repository permissions and token scopes apply |
| Atlassian Administration & identity | Organization, managed accounts, groups and directory-related administration | Restricted/admin-only APIs; do not assume access from ordinary site membership |

## Integration design

- Keep tenant/site URL, OAuth client details and tokens in a server-side secret manager or environment configuration.
- Prefer OAuth 2.0 (3LO) for user-authorized integrations where supported; use product-specific supported authentication for service-to-service cases.
- Request minimum scopes and verify exact API version and product availability before enabling an operation.
- Handle pagination, rate limiting, retries, permission failures and API error responses.
- Do not expose access tokens, refresh tokens, client secrets or authorization headers to browser code or logs.
- Separate read and write capabilities; require authorization for destructive or externally visible actions.

## Suggested setup inputs

1. Atlassian Cloud site URL (for example, `https://example.atlassian.net`).
2. Product(s): Jira, Confluence, Jira Service Management and/or Bitbucket.
3. Authentication method and OAuth app configuration appropriate to the selected product.
4. Minimum required scopes and a test account with the intended permissions.

## Current repository status

This folder is provider catalog/documentation only. No Atlassian provider adapter is currently registered in `backend/integrations/registry.py`, and no live Atlassian API request or credential validation is implemented here. `live_connection_verified` is intentionally `False`.

The existence of product names or endpoint documentation does not mean those products are connected. Implement and test each product capability independently before changing its status.
