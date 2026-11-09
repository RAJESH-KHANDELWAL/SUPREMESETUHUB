# BADA BUSINESS DATABASE ECOSYSTEM

This package owns Bada Business-specific persistence capabilities.

## Programs

The `programs/` subpackage stores owner-scoped snapshots of program metadata
and references the canonical resource catalog. It does not duplicate provider
descriptions, registration URLs, pricing data or business rules.

## Architecture

- DATABASE: schema, migration, repository and persistence service.
- Canonical provider facts: `backend/global_ecosystem/global_bada_business_ecosystem/`.
- Program business rules: CORE.
- HTTP transport: API.
- External provider execution: injected integration/runtime adapters.

No live provider API sync or payment processing is enabled.
