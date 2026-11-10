"""Analytical warehouse and lakehouse descriptors."""
from typing import Any
PLATFORMS = ("snowflake", "bigquery", "redshift", "databricks", "clickhouse", "apache_iceberg", "delta_lake")
def describe_warehouse_domain() -> dict[str, Any]:
    return {"domain":"warehouse_and_lakehouse","platforms":list(PLATFORMS),"capabilities":["columnar_storage","olap","data_lake","lakehouse_tables","semantic_models","batch_analytics"],"integration_status":"catalog_only"}
