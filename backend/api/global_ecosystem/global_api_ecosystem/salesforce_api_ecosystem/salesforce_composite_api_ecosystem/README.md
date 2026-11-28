# Salesforce Composite API API Ecosystem

## Scope
Composite, batch, tree, and graph-style grouped REST operations.

## Setup
REST API OAuth token and permissions for every referenced object/resource.
Configure a Salesforce Connected App, OAuth scopes, org/instance domain, API-enabled integration user, and object-level permissions. Use sandbox-first testing and store secrets in a managed secret store.

## Status
Service-family scaffold only. Adapter implementation, production credential persistence, and live connection are not verified. Enforce tenant isolation, least privilege, rate limits, audit logs, and token revocation before production use.
