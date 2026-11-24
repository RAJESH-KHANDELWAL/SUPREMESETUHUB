# Salesforce Streaming API API Ecosystem

## Scope
PushTopics, generic streaming, and change data capture subscriptions where supported.

## Setup
Streaming permissions, supported API version, and event channel configuration.
Configure a Salesforce Connected App, OAuth scopes, org/instance domain, API-enabled integration user, and object-level permissions. Use sandbox-first testing and store secrets in a managed secret store.

## Status
Service-family scaffold only. Adapter implementation, production credential persistence, and live connection are not verified. Enforce tenant isolation, least privilege, rate limits, audit logs, and token revocation before production use.
