# GLOBAL SERVER ENGINE

ENGINE-owned execution and lifecycle boundary for server infrastructure.

## Responsibilities
- Provider-specific runtime adapter interfaces.
- Engine registration, retrieval and removal.
- Execution handler validation and status reporting.
- Provider adapter catalog and ENGINE-owned tests.

## Boundaries
This package imports no API or CORE implementation. The ENGINE registry is process-local. Provider folders are adapter namespaces, not authenticated cloud accounts. Handlers must be explicitly configured with authorized SDK clients and enforce least privilege. No provider credentials are stored in this repository, and no remote provisioning occurs by default.

SERVER owns registered server-resource inventory. ENGINE owns execution adapters. DATABASE owns durable persistence; this ENGINE registry is not a durable database.
