"""SQLite schema definitions for Bada Business program persistence."""

PROGRAM_TABLE = "bada_business_program_records"
PROGRAM_MIGRATION_TABLE = "bada_business_program_migrations"

CREATE_PROGRAM_TABLE = f"""
CREATE TABLE IF NOT EXISTS {PROGRAM_TABLE} (
    record_id TEXT PRIMARY KEY,
    owner_user_id TEXT NOT NULL,
    program_id TEXT NOT NULL,
    provider_id TEXT NOT NULL DEFAULT 'bada_business',
    program_name TEXT NOT NULL,
    program_status TEXT NOT NULL DEFAULT 'UNCONFIRMED',
    source_catalog TEXT NOT NULL DEFAULT 'backend.global_ecosystem.global_bada_business_ecosystem.platform_resources.catalog',
    source_version TEXT NOT NULL DEFAULT '',
    snapshot_json TEXT NOT NULL DEFAULT '{{}}',
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(owner_user_id, program_id)
)
"""

CREATE_OWNER_INDEX = f"""
CREATE INDEX IF NOT EXISTS idx_{PROGRAM_TABLE}_owner_status
ON {PROGRAM_TABLE}(owner_user_id, program_status, updated_at DESC)
"""

CREATE_MIGRATION_TABLE = f"""
CREATE TABLE IF NOT EXISTS {PROGRAM_MIGRATION_TABLE} (
    migration_id TEXT PRIMARY KEY,
    applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

SCHEMA_VERSION = "001_bada_business_program_records"

def schema_statements():
    return (CREATE_MIGRATION_TABLE, CREATE_PROGRAM_TABLE, CREATE_OWNER_INDEX)
