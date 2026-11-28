# GLOBAL_DATABASE Storage Ecosystem

Storage taxonomy and foundation for database technologies and database-managed data. Each category is an independent direct-child package in this directory; there are no generic `categories/` or `providers/` nesting layers.

## Responsibility

This package owns storage-side database category identity, metadata, taxonomy, schema descriptors, lifecycle definitions and storage-health metadata. Provider API clients, authentication, database engines and external operations remain in their respective API/integration layers.

## Readiness boundary

All categories start as `NOT_CONFIGURED`. Provider product support, account entitlement, authorized connectivity, query execution, read/write operations, migrations, replication and backup/recovery are not implied. Never commit credentials or personal data.

## Categories

- `global_database_relational_storage_ecosystem/`
- `global_database_sql_storage_ecosystem/`
- `global_database_nosql_storage_ecosystem/`
- `global_database_document_storage_ecosystem/`
- `global_database_key_value_storage_ecosystem/`
- `global_database_wide_column_storage_ecosystem/`
- `global_database_graph_storage_ecosystem/`
- `global_database_time_series_storage_ecosystem/`
- `global_database_vector_storage_ecosystem/`
- `global_database_spatial_storage_ecosystem/`
- `global_database_geospatial_storage_ecosystem/`
- `global_database_in_memory_storage_ecosystem/`
- `global_database_distributed_storage_ecosystem/`
- `global_database_newsql_storage_ecosystem/`
- `global_database_data_warehouse_storage_ecosystem/`
- `global_database_data_lake_storage_ecosystem/`
- `global_database_lakehouse_storage_ecosystem/`
- `global_database_analytical_storage_ecosystem/`
- `global_database_transactional_storage_ecosystem/`
- `global_database_operational_storage_ecosystem/`
- `global_database_embedded_storage_ecosystem/`
- `global_database_serverless_storage_ecosystem/`
- `global_database_cloud_native_storage_ecosystem/`
- `global_database_multi_model_storage_ecosystem/`
- `global_database_object_storage_ecosystem/`
- `global_database_backup_storage_ecosystem/`
- `global_database_replication_storage_ecosystem/`
- `global_database_sharding_storage_ecosystem/`
- `global_database_partitioned_storage_ecosystem/`
- `global_database_cache_storage_ecosystem/`
- `global_database_metadata_storage_ecosystem/`
- `global_database_catalog_storage_ecosystem/`
- `global_database_schema_storage_ecosystem/`
- `global_database_index_storage_ecosystem/`
- `global_database_query_storage_ecosystem/`
- `global_database_log_storage_ecosystem/`
- `global_database_archive_storage_ecosystem/`
- `global_database_ledger_storage_ecosystem/`
- `global_database_search_storage_ecosystem/`
- `global_database_backup_recovery_storage_ecosystem/`
