"""Database capability metadata for Bada Business program persistence."""

ECOSYSTEM_ID = "BADA-BUSINESS-DATABASE-PROGRAMS"
LAYER = "DATABASE"
TABLES = ("bada_business_program_records", "bada_business_program_migrations")
CANONICAL_RESOURCE_CATALOG = "backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog"
PERSISTENCE_MODEL = "OWNER_SCOPED_PROGRAM_SNAPSHOT"
EXTERNAL_PROVIDER_SYNC = False
PAYMENT_DATA_STORED = False

def get_program_database_catalog():
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "layer": LAYER,
        "tables": list(TABLES),
        "canonical_resource_catalog": CANONICAL_RESOURCE_CATALOG,
        "persistence_model": PERSISTENCE_MODEL,
        "external_provider_sync": EXTERNAL_PROVIDER_SYNC,
        "payment_data_stored": PAYMENT_DATA_STORED,
    }
