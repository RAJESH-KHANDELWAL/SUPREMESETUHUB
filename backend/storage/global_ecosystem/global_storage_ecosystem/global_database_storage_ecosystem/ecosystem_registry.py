"""Direct-child database category registry."""
from pathlib import Path
ROOT = Path(__file__).parent
CATEGORY_PACKAGES = [
    "global_database_relational_storage_ecosystem",
    "global_database_sql_storage_ecosystem",
    "global_database_nosql_storage_ecosystem",
    "global_database_document_storage_ecosystem",
    "global_database_key_value_storage_ecosystem",
    "global_database_wide_column_storage_ecosystem",
    "global_database_graph_storage_ecosystem",
    "global_database_time_series_storage_ecosystem",
    "global_database_vector_storage_ecosystem",
    "global_database_spatial_storage_ecosystem",
    "global_database_geospatial_storage_ecosystem",
    "global_database_in_memory_storage_ecosystem",
    "global_database_distributed_storage_ecosystem",
    "global_database_newsql_storage_ecosystem",
    "global_database_data_warehouse_storage_ecosystem",
    "global_database_data_lake_storage_ecosystem",
    "global_database_lakehouse_storage_ecosystem",
    "global_database_analytical_storage_ecosystem",
    "global_database_transactional_storage_ecosystem",
    "global_database_operational_storage_ecosystem",
    "global_database_embedded_storage_ecosystem",
    "global_database_serverless_storage_ecosystem",
    "global_database_cloud_native_storage_ecosystem",
    "global_database_multi_model_storage_ecosystem",
    "global_database_object_storage_ecosystem",
    "global_database_backup_storage_ecosystem",
    "global_database_replication_storage_ecosystem",
    "global_database_sharding_storage_ecosystem",
    "global_database_partitioned_storage_ecosystem",
    "global_database_cache_storage_ecosystem",
    "global_database_metadata_storage_ecosystem",
    "global_database_catalog_storage_ecosystem",
    "global_database_schema_storage_ecosystem",
    "global_database_index_storage_ecosystem",
    "global_database_query_storage_ecosystem",
    "global_database_log_storage_ecosystem",
    "global_database_archive_storage_ecosystem",
    "global_database_ledger_storage_ecosystem",
    "global_database_search_storage_ecosystem",
    "global_database_backup_recovery_storage_ecosystem"
]

def validate_category_packages():
    return [name for name in CATEGORY_PACKAGES if not (ROOT / name).is_dir()]
