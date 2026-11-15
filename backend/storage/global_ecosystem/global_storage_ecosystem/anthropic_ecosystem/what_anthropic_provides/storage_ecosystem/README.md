# ANTHROPIC STORAGE ECOSYSTEM

Canonical Anthropic storage taxonomy and metadata catalog for SUPREMESETUHUB.

## Child storage ecosystems

- `anthropic_claude_storage_ecosystem` — Claude platform storage-related metadata and supported file workflows.
- `anthropic_claude_projects_storage_ecosystem` — Claude Projects workspace metadata and project-scoped knowledge references.
- `anthropic_claude_artifacts_storage_ecosystem` — Claude Artifacts metadata and generated-output lifecycle references.
- `anthropic_claude_files_storage_ecosystem` — File upload, handling, and document workflow metadata.
- `anthropic_claude_knowledge_storage_ecosystem` — Knowledge, retrieval, and source-reference metadata.
- `anthropic_claude_connectors_storage_ecosystem` — Connector configuration metadata and external-source references.
- `anthropic_claude_enterprise_storage_ecosystem` — Enterprise and workspace storage governance metadata.
- `anthropic_claude_code_storage_ecosystem` — Claude Code project context, repository, and artifact metadata.

## Standard category structure

Each category is a taxonomy/package boundary. Existing complete package scaffolds remain available at the compatibility path recorded in `category_index.json`. Canonical category directories contain their own README and manifest and must be expanded with the same package baseline before runtime integration.

## Architecture boundary

The Anthropic API Ecosystem owns API clients, authentication, endpoints, scopes and API operations. This Storage Ecosystem owns storage-side taxonomy, metadata, object lifecycle mappings and storage health contracts. It references API capabilities without duplicating API clients or authentication.

## Truthful readiness

Catalog and category folders are scaffolding only. They do not establish that Claude conversations, Projects, Artifacts, Files, Connectors, Claude Code or enterprise features expose a generic storage API. Keep connections `NOT_CONFIGURED` until authorized live health checks and required read/write tests pass. Storage operations remain disabled. Never commit credentials or personal data.

## Adult-only governance

Adult-related entries are classification namespaces only. Require age assurance, informed consent, privacy, security, retention, reporting/takedown and jurisdictional legal review. Prohibit minors, coercion, exploitation and non-consensual intimate imagery. Taxonomy folders do not authorize hosting, generation or distribution.
