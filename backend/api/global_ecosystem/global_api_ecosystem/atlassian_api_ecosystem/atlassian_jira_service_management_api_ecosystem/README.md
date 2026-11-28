# Jira Service Management API

Provider family: ATLASSIAN API ECOSYSTEM

## Scope

Service projects, customer requests, request types, queues, organizations and service-desk workflows.

## Authentication and access

Product-specific OAuth scopes and agent/customer permissions; verify endpoint availability for the tenant.

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
