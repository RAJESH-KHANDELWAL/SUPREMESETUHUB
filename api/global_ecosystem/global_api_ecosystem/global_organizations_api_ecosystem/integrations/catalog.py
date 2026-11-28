"""Declared integration contracts; declarations do not mean live connections."""
INTEGRATION_CATALOG = [
 {"integration_id":"company_companies","target_ecosystem":"GLOBAL COMPANY / COMPANIES API ECOSYSTEM","direction":"canonical_entity_reference","contract":"Reference canonical company_id where an organization is also a registered company; Company Companies retains the legal-company profile."},
 {"integration_id":"bada_business","target_ecosystem":"GLOBAL BADA BUSINESS API ECOSYSTEM","direction":"classification_crosswalk","contract":"Map relevant activity to stable business category and industry IDs; do not copy Bada Business records."},
 {"integration_id":"platforms","target_ecosystem":"GLOBAL PLATFORMS API ECOSYSTEM","direction":"canonical_entity_reference","contract":"Reference platform_id for platforms owned, operated, published, funded, or used by an organization."},
 {"integration_id":"global_entity_relationships","target_ecosystem":"GLOBAL ENTITY RELATIONSHIPS API ECOSYSTEM","direction":"shared_relationship_storage","contract":"Store cross-ecosystem relationship edges centrally; do not maintain a second relationship graph."}
]
