# ANTHROPIC Storage Ecosystem

Canonical Anthropic provider storage catalog for SUPREMESETUHUB.

This package follows the same parent-catalog pattern as `google_storage_ecosystem`: one provider storage root, a canonical taxonomy, a category index, and independent category packages.

## Child storage ecosystems

- `anthropic_claude_storage_ecosystem` — Claude platform storage-related metadata and supported file workflows.
- `anthropic_claude_projects_storage_ecosystem` — Claude Projects workspace metadata and project-scoped knowledge references.
- `anthropic_claude_artifacts_storage_ecosystem` — Claude Artifacts metadata and generated-output lifecycle references.
- `anthropic_claude_files_storage_ecosystem` — file upload, handling and document workflow metadata.
- `anthropic_claude_knowledge_storage_ecosystem` — knowledge, retrieval and source-reference metadata.
- `anthropic_claude_connectors_storage_ecosystem` — connector configuration metadata and external-source references.
- `anthropic_claude_enterprise_storage_ecosystem` — enterprise and workspace storage governance metadata.
- `anthropic_claude_code_storage_ecosystem` — Claude Code project context, repository and artifact metadata.

## Canonical package structure

- `taxonomy/anthropic_storage_taxonomy.json`: provider-specific grouped taxonomy.
- `category_index.json`: canonical index of all 8 child category packages and paths.
- Each child package owns its README, manifest, Python package foundation, API namespace, models, PHP metadata helper, schema, tests, and `domains/`, `geography/`, `maturity_levels/` taxonomy directories.

## Architecture boundary

The Anthropic API Ecosystem owns API clients, authentication, endpoints, scopes and API operations. This Storage Ecosystem owns storage-side taxonomy, metadata, object lifecycle mappings and storage health contracts. It references API capabilities without duplicating API clients or authentication.

## Truthful readiness

This catalog and its child folders are taxonomy and package scaffolding only. They do not establish that Claude conversations, Projects, Artifacts, Files, Connectors, Claude Code or enterprise features expose a generic storage API. Product availability, account entitlements, API support, permissions and regional behavior must be verified independently. Keep every child `NOT_CONFIGURED` until authorized live health checks and required read/write tests pass. Storage operations remain disabled. Never commit credentials or personal data.

## Adult-only governance

Adult-only classifications are limited to lawful adult contexts. Require robust age assurance, informed consent, privacy and security controls, reporting/takedown, retention controls and jurisdiction-specific legal review. Prohibit minors, coercion, exploitation and non-consensual intimate imagery. Taxonomy folders do not authorize hosting, generation or distribution.
