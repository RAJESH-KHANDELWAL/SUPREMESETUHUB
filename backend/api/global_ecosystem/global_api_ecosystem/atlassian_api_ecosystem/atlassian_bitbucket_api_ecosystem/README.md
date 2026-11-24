# Bitbucket Cloud API

Provider family: ATLASSIAN API ECOSYSTEM

## Scope

Workspaces, repositories, source, pull requests, commits, pipelines and deployment metadata.

## Authentication and access

Bitbucket OAuth or supported workspace/repository access token; scope and workspace permissions apply.

Use the minimum required scopes. Keep client secrets and access/refresh tokens in server-side secret storage. Never commit credentials or expose tokens in browser code or logs.

## Operational requirements

- Confirm the selected Atlassian product is enabled for the target tenant.
- Enforce tenant, site, project, space, workspace and user permissions.
- Implement pagination, rate-limit handling, bounded retries and structured error handling.
- Record audit events without recording secrets or authorization headers.
- Require explicit confirmation for destructive or externally visible write operations.

## Status

Catalog and documentation scaffold only. No live API request, token exchange or credential validation is implemented in this family yet.

Canonical provider adapter (configuration readiness only): `backend/integrations/providers/atlassian.py`.
