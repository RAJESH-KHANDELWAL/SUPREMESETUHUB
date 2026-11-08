# Salesforce Apex APIs API Ecosystem

## Scope
Apex execution and supported Apex REST interfaces for controlled automation.

## Setup
Appropriate Apex authoring/execution permissions; restrict execution to trusted administrators.
Configure a Salesforce Connected App, OAuth scopes, org/instance domain, API-enabled integration user, and object-level permissions. Use sandbox-first testing and store secrets in a managed secret store.

## Status
Service-family scaffold only. Adapter implementation, production credential persistence, and live connection are not verified. Enforce tenant isolation, least privilege, rate limits, audit logs, and token revocation before production use.
