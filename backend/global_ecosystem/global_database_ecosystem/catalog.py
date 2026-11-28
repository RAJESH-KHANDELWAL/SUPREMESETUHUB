"""Global database ecosystem taxonomy and capability catalog.

Provider-neutral: runtime database drivers, credentials, connection pools,
transactions, migrations, and query execution belong to the canonical DATABASE
architecture layer, not this ecosystem catalog.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

REGIONS = {
    "bharat": ("India", "states", "union_territories", "districts", "cities", "rural", "urban"),
    "south_asia": ("South Asia",),
    "asia_pacific": ("Asia Pacific",),
    "middle_east": ("Middle East",),
    "europe": ("Europe",),
    "africa": ("Africa",),
    "north_america": ("North America",),
    "latin_america": ("Latin America",),
    "global": ("Cross-border", "multinational", "multi-region", "sovereign-cloud"),
}

MATURITY_LEVELS = ("normal", "standard", "professional", "enterprise", "advanced", "supreme")

DATABASE_DOMAINS: dict[str, tuple[str, ...]] = {
    "relational_sql": ("postgresql", "mysql", "mariadb", "sqlite", "microsoft_sql_server", "oracle_database"),
    "distributed_sql": ("cockroachdb", "yugabytedb", "tidb", "google_spanner", "oceanbase"),
    "document_nosql": ("mongodb", "couchdb", "firestore", "documentdb"),
    "key_value": ("redis", "valkey", "keydb", "dynamodb", "foundationdb"),
    "wide_column": ("cassandra", "scylladb", "hbase", "bigtable"),
    "graph": ("neo4j", "neptune", "janusgraph", "arangodb"),
    "time_series": ("timescaledb", "influxdb", "questdb", "tdengine", "victoriametrics"),
    "search_and_analytics": ("opensearch", "elasticsearch", "clickhouse", "duckdb", "trino"),
    "vector_and_ai_data": ("pgvector", "milvus", "weaviate", "qdrant", "pinecone", "chroma"),
    "object_and_lakehouse": ("iceberg", "delta_lake", "hudi", "duckdb_lakehouse", "lakefs"),
    "embedded_and_edge": ("sqlite", "rocksdb", "lmdb", "libsql", "edge_replication"),
    "ledger_and_immutable": ("ledger_database", "append_only_store", "event_store", "audit_log_store"),
    "cache_and_session": ("distributed_cache", "session_store", "materialized_view_cache"),
    "warehouse_and_olap": ("data_warehouse", "olap_cube", "columnar_store", "semantic_layer"),
    "backup_and_recovery": ("snapshot_catalog", "point_in_time_recovery", "replica_catalog", "archive_index"),
}

WORKLOADS: dict[str, tuple[str, ...]] = {
    "public_services": ("government_records", "municipal_services", "public_health_statistics", "land_and_property_records"),
    "finance": ("banking", "payments", "accounting", "insurance", "risk_and_compliance"),
    "commerce": ("retail", "ecommerce", "marketplaces", "inventory", "orders", "crm", "erp"),
    "industry": ("manufacturing", "supply_chain", "logistics", "iot_telemetry", "energy"),
    "knowledge_and_media": ("education", "research", "publishing", "media_catalogs", "digital_archives"),
    "health_and_science": ("clinical_systems", "research_datasets", "laboratory_data", "genomics"),
    "communications": ("messaging_metadata", "community_platforms", "social_networks", "customer_support"),
    "adult_and_sexual_content": (
        "adult_creator_accounts", "age_assurance_status", "consent_and_release_records",
        "content_metadata", "subscription_entitlements", "payout_ledger",
        "moderation_cases", "copyright_and_takedown_records", "privacy_requests",
    ),
    "security_and_identity": ("identity_records", "access_events", "fraud_signals", "security_audit_events"),
    "ai_and_automation": ("training_metadata", "feature_store", "vector_retrieval", "model_evaluation", "agent_memory"),
}

QUALITY_CAPABILITIES = (
    "schema_design", "data_modeling", "constraints_and_integrity", "indexing",
    "partitioning", "sharding", "replication", "multi_region_consistency",
    "transactions", "streaming_ingestion", "batch_ingestion", "cdc",
    "governance", "lineage", "catalog_and_discovery", "encryption",
    "access_control", "privacy_controls", "retention_and_deletion",
    "backup_restore", "disaster_recovery", "observability", "cost_optimization",
    "migration_and_interoperability",
)

ADULT_DATA_GUARDRAILS = {
    "scope": "Lawful adult-oriented services involving consenting adults only.",
    "age_assurance": "Store minimal verification status and provider reference; avoid unnecessary identity document retention.",
    "consent": "Maintain versioned, revocable consent and model/content release evidence where legally required.",
    "privacy": "Apply strict access controls, encryption, data minimization, purpose limitation, and retention schedules.",
    "safety": (
        "No minor-related sexual content, exploitation, trafficking, coercion, non-consensual intimate imagery, "
        "or evasion of lawful reporting and takedown obligations."
    ),
}

def get_database_ecosystem_catalog() -> dict[str, Any]:
    """Return a detached, provider-neutral catalog; no live database is implied."""
    return {
        "ecosystem_id": "global_database_ecosystem",
        "scope": "Bharat to global; normal to supreme; cross-industry data platforms",
        "integration_status": "taxonomy_only",
        "live_connections_verified": False,
        "regions": deepcopy(REGIONS),
        "maturity_levels": list(MATURITY_LEVELS),
        "database_domains": deepcopy(DATABASE_DOMAINS),
        "workloads": deepcopy(WORKLOADS),
        "quality_capabilities": list(QUALITY_CAPABILITIES),
        "adult_data_guardrails": deepcopy(ADULT_DATA_GUARDRAILS),
        "architecture_boundary": {
            "this_package_owns": "domain taxonomy, capability metadata, workload classification",
            "canonical_database_layer_owns": (
                "drivers, connection management, query execution, transactions, migrations, "
                "replication runtime, backups, secrets, authorization, and operational APIs"
            ),
        },
    }

def validate_database_ecosystem_catalog() -> tuple[str, ...]:
    """Return taxonomy consistency errors; an empty tuple means structurally valid."""
    errors: list[str] = []
    if len(MATURITY_LEVELS) != len(set(MATURITY_LEVELS)):
        errors.append("duplicate maturity levels")
    for group_name, values in DATABASE_DOMAINS.items():
        if not values:
            errors.append(f"database domain {group_name} is empty")
    for group_name, values in WORKLOADS.items():
        if not values:
            errors.append(f"workload group {group_name} is empty")
    if "adult_and_sexual_content" not in WORKLOADS:
        errors.append("adult workload classification is missing")
    required_guardrails = {"age_assurance", "consent", "privacy", "safety"}
    if not required_guardrails.issubset(ADULT_DATA_GUARDRAILS):
        errors.append("adult data guardrails are incomplete")
    return tuple(errors)

__all__ = [
    "REGIONS", "MATURITY_LEVELS", "DATABASE_DOMAINS", "WORKLOADS",
    "QUALITY_CAPABILITIES", "ADULT_DATA_GUARDRAILS",
    "get_database_ecosystem_catalog", "validate_database_ecosystem_catalog",
]
