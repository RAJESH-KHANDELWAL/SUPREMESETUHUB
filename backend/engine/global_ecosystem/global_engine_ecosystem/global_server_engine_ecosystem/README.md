# GLOBAL SERVER ENGINE

ENGINE-owned execution and lifecycle boundary for server infrastructure.

## Responsibilities
- Provider-specific runtime adapter interfaces.
- Engine registration, retrieval and removal.
- Execution handler validation and status reporting.
- Provider adapter catalog and ENGINE-owned tests.

## Layer boundaries
This package imports no API or CORE implementation. SERVER owns the inventory of registered server resources. ENGINE owns execution adapters. DATABASE owns durable persistence, and STORAGE owns file/object storage. This ENGINE registry is process-local and not a durable database.

## Provider safety
Provider folders are adapter namespaces, not proof of authenticated cloud accounts. Handlers must be explicitly configured with authorized SDK clients and enforce least privilege. No credentials are stored here. No remote provisioning or host monitoring occurs by default.
