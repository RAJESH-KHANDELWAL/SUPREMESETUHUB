"""Catalog-only global database category module; not a live connector."""

DATA_WAREHOUSE_AND_LAKEHOUSE = {
    "category": "DATA_WAREHOUSE_AND_LAKEHOUSE",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "providers": [
        "Snowflake",
        "Google BigQuery",
        "Amazon Redshift",
        "Databricks Lakehouse",
        "Microsoft Fabric Warehouse",
        "Azure Synapse Analytics",
        "Teradata Vantage",
        "IBM Db2 Warehouse",
        "Oracle Autonomous Data Warehouse",
        "ClickHouse Cloud",
        "Firebolt",
        "MotherDuck",
        "Apache Iceberg",
        "Delta Lake",
        "Apache Hudi",
        "Apache Spark"
    ],
}
