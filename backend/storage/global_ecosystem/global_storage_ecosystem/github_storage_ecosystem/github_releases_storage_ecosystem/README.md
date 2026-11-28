# GITHUB RELEASES STORAGE ECOSYSTEM

Category package within the GITHUB Storage Ecosystem.

## Classification
- Provider: GitHub
- Category: `RELEASES`
- Group: `REPOSITORY_AND_SOURCE_STORAGE`
- Parent: `GITHUB_STORAGE_ECOSYSTEM`

## Responsibility
Owns storage-side taxonomy, metadata, lifecycle definitions and readiness declarations for this data domain. GitHub API clients, authentication, scopes, endpoints and external operations remain in API/integration layers. Production persistence belongs in the central database.

## Readiness and safety
Status: `NOT_CONFIGURED`. This scaffold does not prove that the category is a standalone GitHub product, that the current account is entitled to it, or that API access is available. Verify official API support, repository/org permissions, retention behavior and end-to-end operations before enabling integration. Never commit tokens, webhook secrets or private repository content.
