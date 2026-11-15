# ANTHROPIC Storage Ecosystem

Canonical Anthropic provider storage catalog for SUPREMESETUHUB.

- `taxonomy/anthropic_storage_taxonomy.json`: canonical category, domain, geography and maturity taxonomy.
- `category_index.json`: all 8 child category folders and repository paths.
- Each child category contains the same canonical Python package foundation pattern used by Google Storage Ecosystem, together with Anthropic-specific metadata and taxonomy directories.

## Child storage ecosystems

- `anthropic_claude_storage_ecosystem` — CLAUDE; group: `CLAUDE_PLATFORM`.
- `anthropic_claude_projects_storage_ecosystem` — CLAUDE PROJECTS; group: `PROJECT_WORKSPACE`.
- `anthropic_claude_artifacts_storage_ecosystem` — CLAUDE ARTIFACTS; group: `GENERATED_ARTIFACTS`.
- `anthropic_claude_files_storage_ecosystem` — CLAUDE FILES; group: `FILE_WORKFLOWS`.
- `anthropic_claude_knowledge_storage_ecosystem` — CLAUDE KNOWLEDGE; group: `KNOWLEDGE_RETRIEVAL`.
- `anthropic_claude_connectors_storage_ecosystem` — CLAUDE CONNECTORS; group: `CONNECTOR_METADATA`.
- `anthropic_claude_enterprise_storage_ecosystem` — CLAUDE ENTERPRISE; group: `ENTERPRISE_WORKSPACE`.
- `anthropic_claude_code_storage_ecosystem` — CLAUDE CODE; group: `DEVELOPER_WORKSPACE`.

## Canonical child package structure

Each child package follows the Google category package baseline:
- `README.md`, `__init__.py`
- `api/__init__.py`, `api/routes.py`
- `ecosystem_config.py`, `ecosystem_manifest.json`
- `ecosystem_models.py`, `ecosystem_service.py`, `service.py`
- `models/__init__.py`, `models/record.py`
- `php/` read-only metadata helper
- `schemas/manifest.schema.json`
- `tests/test_foundation.py`
- Anthropic taxonomy: `domains/`, `geography/`, `maturity_levels/`

## Architecture boundary

The Anthropic API Ecosystem owns API clients, authentication, endpoints, scopes and API operations. This Storage Ecosystem owns storage-side taxonomy, metadata, object lifecycle mappings and storage health contracts. It references API capabilities without duplicating API clients or authentication.

## Truthful readiness

This catalog and its child folders are taxonomy/scaffolding only. They do not establish that Claude conversations, Projects, Artifacts, Files, Connectors, Claude Code or enterprise features expose a generic storage API. Product availability, account entitlements, API support, permissions and regional behavior must be verified independently. Keep every child `NOT_CONFIGURED` until authorized live health checks and required read/write tests pass. Storage operations remain disabled. Never commit credentials or personal data.

## Adult-only governance

Adult-only classifications are limited to lawful adult contexts. Require robust age assurance, informed consent, privacy and security controls, reporting/takedown, retention controls and jurisdiction-specific legal review. Prohibit minors, coercion, exploitation and non-consensual intimate imagery. Taxonomy folders do not authorize hosting, generation or distribution.
