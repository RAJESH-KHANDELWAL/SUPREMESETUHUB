"""Provider-neutral database platform metadata (no driver or credentials)."""
from __future__ import annotations
from typing import Any

PLATFORMS: tuple[dict[str, Any], ...] = (
    {"id":"postgresql","name":"PostgreSQL","model":"relational_sql","deployment":("self_hosted","managed_cloud")},
    {"id":"mysql","name":"MySQL","model":"relational_sql","deployment":("self_hosted","managed_cloud")},
    {"id":"mariadb","name":"MariaDB","model":"relational_sql","deployment":("self_hosted","managed_cloud")},
    {"id":"sqlite","name":"SQLite","model":"embedded_and_edge","deployment":("embedded","edge")},
    {"id":"sql_server","name":"Microsoft SQL Server","model":"relational_sql","deployment":("self_hosted","managed_cloud")},
    {"id":"oracle","name":"Oracle Database","model":"relational_sql","deployment":("self_hosted","managed_cloud")},
    {"id":"mongodb","name":"MongoDB","model":"document_nosql","deployment":("self_hosted","managed_cloud")},
    {"id":"redis","name":"Redis","model":"key_value","deployment":("self_hosted","managed_cloud")},
    {"id":"cassandra","name":"Apache Cassandra","model":"wide_column","deployment":("self_hosted","managed_cloud")},
    {"id":"neo4j","name":"Neo4j","model":"graph","deployment":("self_hosted","managed_cloud")},
    {"id":"influxdb","name":"InfluxDB","model":"time_series","deployment":("self_hosted","managed_cloud")},
    {"id":"clickhouse","name":"ClickHouse","model":"search_and_analytics","deployment":("self_hosted","managed_cloud")},
    {"id":"opensearch","name":"OpenSearch","model":"search_and_analytics","deployment":("self_hosted","managed_cloud")},
    {"id":"qdrant","name":"Qdrant","model":"vector_and_ai_data","deployment":("self_hosted","managed_cloud")},
    {"id":"milvus","name":"Milvus","model":"vector_and_ai_data","deployment":("self_hosted","managed_cloud")},
    {"id":"cockroachdb","name":"CockroachDB","model":"distributed_sql","deployment":("self_hosted","managed_cloud")},
    {"id":"yugabytedb","name":"YugabyteDB","model":"distributed_sql","deployment":("self_hosted","managed_cloud")},
    {"id":"dynamodb","name":"Amazon DynamoDB","model":"key_value","deployment":("managed_cloud",)},
    {"id":"firestore","name":"Google Cloud Firestore","model":"document_nosql","deployment":("managed_cloud",)},
    {"id":"spanner","name":"Google Cloud Spanner","model":"distributed_sql","deployment":("managed_cloud",)},
    {"id":"bigtable","name":"Google Cloud Bigtable","model":"wide_column","deployment":("managed_cloud",)},
    {"id":"cosmosdb","name":"Azure Cosmos DB","model":"document_nosql","deployment":("managed_cloud",)},
    {"id":"supabase","name":"Supabase","model":"relational_sql","deployment":("managed_cloud","self_hosted")},
    {"id":"neon","name":"Neon","model":"relational_sql","deployment":("managed_cloud",)},
    {"id":"planetscale","name":"PlanetScale","model":"relational_sql","deployment":("managed_cloud",)},
    {"id":"tidb","name":"TiDB","model":"distributed_sql","deployment":("self_hosted","managed_cloud")},
    {"id":"oceanbase","name":"OceanBase","model":"distributed_sql","deployment":("self_hosted","managed_cloud")},
    {"id":"weaviate","name":"Weaviate","model":"vector_and_ai_data","deployment":("self_hosted","managed_cloud")},
    {"id":"pinecone","name":"Pinecone","model":"vector_and_ai_data","deployment":("managed_cloud",)},
    {"id":"duckdb","name":"DuckDB","model":"search_and_analytics","deployment":("embedded","analytics")},
    {"id":"iceberg","name":"Apache Iceberg","model":"object_and_lakehouse","deployment":("lakehouse",)},
    {"id":"delta_lake","name":"Delta Lake","model":"object_and_lakehouse","deployment":("lakehouse",)},
)

def get_platform_catalog() -> tuple[dict[str, Any], ...]:
    """Return detached provider metadata."""
    return tuple({**item, "deployment": tuple(item["deployment"]), "integration_status": "catalog_only"} for item in PLATFORMS)

def find_platforms(*, model: str | None = None, deployment: str | None = None) -> tuple[dict[str, Any], ...]:
    """Filter database platform catalog without contacting providers."""
    values = get_platform_catalog()
    if model is not None:
        values = tuple(item for item in values if item["model"] == model)
    if deployment is not None:
        values = tuple(item for item in values if deployment in item["deployment"])
    return values
