# Jira Storage Ecosystem

## Purpose
Projects, issues, work items, boards, sprints, workflows, comments, attachments, fields and audit metadata. This catalog does not itself create, modify or export Jira content.

## Package boundary
This child package owns the product-specific metadata and storage taxonomy for `ATLASSIAN_JIRA`. It remains under the canonical `atlassian_storage_ecosystem/` parent. Shared backend infrastructure, central persistence, credentials and Atlassian API clients are not duplicated here.

## Classification directories
- `domains/` — business and personal-use domain classification; metadata only
- `geography/` — Bharat, regional and global jurisdiction references
- `maturity_levels/` — normal, professional, advanced, enterprise and supreme organizational maturity labels

## Integration boundary
Verify the product's documented API, tenant/plan entitlement, scopes, rate limits, data residency and operation-specific permissions. Keep connection state `NOT_CONFIGURED` and storage operations disabled until authorization, live health checks and end-to-end tests pass.

## Security
Use least privilege, secure token storage, encryption, audit logs, data minimization, retention/deletion controls and jurisdictional compliance. Never commit credentials, tokens or private customer content.

## Readiness
`CATEGORY_FOUNDATION_SCAFFOLD` describes catalog documentation only; it is not a live connection or working product API, export, synchronization or storage implementation.
