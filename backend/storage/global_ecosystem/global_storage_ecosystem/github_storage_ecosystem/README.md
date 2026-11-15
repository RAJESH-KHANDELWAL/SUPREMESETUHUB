# GITHUB Storage Ecosystem

Parent namespace for 30 GitHub storage-related category packages.

- `taxonomy/github_storage_taxonomy.json`: canonical grouped taxonomy.
- `category_index.json`: category folder names, groups and repository paths.
- Each category package owns category-specific storage metadata and readiness declarations.

This is a storage taxonomy and metadata catalog—not a claim that every category is a standalone GitHub product or a separate storage service. Git repositories, Git objects, release assets, Actions artifacts and package registries have distinct semantics, limits, retention behavior and permissions that must be verified against current GitHub APIs and account entitlements.

## Architecture boundary
This STORAGE namespace owns storage-side taxonomy, metadata, lifecycle definitions and health contracts. GitHub API clients, OAuth/PAT authentication, scopes, endpoints and external operations remain in their API/integration layers. Production persistence belongs in the central database.

## Readiness
All category packages start as `NOT_CONFIGURED`. Do not claim live GitHub connectivity or enable write/delete operations until authorized health checks and end-to-end tests pass. Never commit access tokens, webhook secrets or private repository content.
