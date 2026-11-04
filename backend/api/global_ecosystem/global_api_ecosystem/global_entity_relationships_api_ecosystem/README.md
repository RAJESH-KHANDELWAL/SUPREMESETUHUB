# GLOBAL ENTITY RELATIONSHIPS API ECOSYSTEM

A shared relationship layer for linking records across Company, Enterprise, Corporate Group and Platform ecosystems without duplicating canonical identities.

Supported relationship types: owns, operates, publishes, distributes, parent_of, subsidiary_of, brand_of, founded_by, partner_of and resells.

Each edge requires a stable relationship ID, source and target entity IDs, relationship type, verification status and (for verified edges) source URLs. The registry is read-only and starts empty. A relationship is not inferred from a brand name or provider folder. No live ownership verification is claimed.

Endpoints:
- GET /api/v1/global-api-ecosystem/global/entity-relationships/status
- GET /api/v1/global-api-ecosystem/global/entity-relationships?entity_id=...&relationship_type=...
