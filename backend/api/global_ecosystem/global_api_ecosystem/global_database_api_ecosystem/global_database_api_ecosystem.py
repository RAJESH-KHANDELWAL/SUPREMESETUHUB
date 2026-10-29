"""Global database ecosystem catalog.

This file is a discovery/catalog index, not a live connector registry.
Provider inclusion does not imply an official API, account access, support,
or a verified production connection. Adult-industry references are separated
from actual database engines and database-service providers.
"""

from __future__ import annotations

GLOBAL_DATABASE_API_ECOSYSTEM = {
    "name": "GLOBAL DATABASE API ECOSYSTEM",
    "family": "DATABASE",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "catalog_scope": "Broad international catalog; not an exhaustive census of every vendor worldwide.",
    "existing_provider_modules": {
        "apple": "apple_database_api_ecosystem/apple_database_api_ecosystem.py",
        "aws": "aws_database_api_ecosystem/aws_database_api_ecosystem.py",
        "google": "google_database_api_ecosystem/google_database_api_ecosystem.py",
        "ibm": "ibm_database_api_ecosystem/ibm_database_api_ecosystem.py",
        "microsoft": "microsoft_database_api_ecosystem/microsoft_database_api_ecosystem.py",
        "oracle": "oracle_database_api_ecosystem/oracle_database_api_ecosystem.py",
        "salesforce": "salesforce_database_api_ecosystem/salesforce_database_api_ecosystem.py",
    },
    "category_modules": {
        "relational_sql": "relational_database_ecosystem/relational_database_api_ecosystem.py",
        "document_key_value": "document_database_ecosystem/document_database_api_ecosystem.py",
        "graph": "graph_database_ecosystem/graph_database_api_ecosystem.py",
        "time_series": "time_series_database_ecosystem/time_series_database_api_ecosystem.py",
        "search_analytics": "search_analytics_database_ecosystem/search_analytics_database_api_ecosystem.py",
        "vector_ai": "vector_ai_database_ecosystem/vector_ai_database_api_ecosystem.py",
        "warehouse_lakehouse": "warehouse_lakehouse_ecosystem/warehouse_lakehouse_api_ecosystem.py",
        "embedded_edge": "embedded_edge_database_ecosystem/embedded_edge_database_api_ecosystem.py",
        "cloud_platforms": "cloud_database_platform_ecosystem/cloud_database_platform_api_ecosystem.py",
        "blockchain_specialized": "blockchain_specialized_data_ecosystem/blockchain_specialized_data_api_ecosystem.py",
        "adult_industry_references": "adult_industry_reference_ecosystem/adult_industry_reference_api_ecosystem.py",
    },
    "database_engines_and_projects": {
        "relational_sql": [
            "PostgreSQL", "MySQL", "MariaDB", "SQLite", "DuckDB", "Firebird",
            "SAP HANA", "SAP SQL Anywhere", "InterBase", "H2 Database", "HSQLDB",
            "Apache Derby", "CockroachDB", "YugabyteDB", "TiDB", "OceanBase",
            "GaussDB", "KingbaseES", "Dameng DM", "openGauss", "PolarDB",
            "Greenplum", "EDB Postgres Advanced Server", "Percona Server for MySQL",
        ],
        "enterprise_and_cloud_relational": [
            "Oracle Database", "Microsoft SQL Server", "Azure SQL", "Amazon RDS",
            "Amazon Aurora", "Amazon Redshift", "Google Cloud SQL",
            "Google AlloyDB", "Google Spanner", "Google BigQuery",
            "Azure Cosmos DB", "Azure Database for PostgreSQL",
            "Azure Database for MySQL", "IBM Db2", "IBM Informix",
            "Snowflake", "Teradata Vantage", "Vertica", "Actian",
            "SingleStore", "Firebolt", "Materialize", "Neon", "Supabase",
            "PlanetScale", "Aiven", "DigitalOcean Managed Databases",
            "Linode/Akamai Managed Databases", "Heroku Postgres",
            "Render PostgreSQL", "Railway PostgreSQL", "Crunchy Bridge",
            "Tembo", "Xata", "Turso", "Convex",
        ],
        "document_and_key_value": [
            "MongoDB", "MongoDB Atlas", "Amazon DocumentDB", "Couchbase",
            "Couchbase Capella", "CouchDB", "RavenDB", "RethinkDB",
            "Azure Table Storage", "Amazon DynamoDB", "Google Firestore",
            "Google Firebase Realtime Database", "Redis", "Valkey", "KeyDB",
            "Dragonfly", "Aerospike", "ScyllaDB", "FoundationDB", "Riak",
            "Voldemort", "Etcd", "Consul KV", "Memcached",
        ],
        "wide_column_and_distributed": [
            "Apache Cassandra", "DataStax Astra DB", "Apache HBase",
            "Google Bigtable", "Amazon Keyspaces", "ScyllaDB",
            "YugabyteDB", "TiDB", "CockroachDB", "Citus",
            "Apache Accumulo", "Apache Kudu", "Apache Ignite",
        ],
        "graph_databases": [
            "Neo4j", "Amazon Neptune", "Azure Cosmos DB Gremlin API",
            "ArangoDB", "OrientDB", "JanusGraph", "TigerGraph",
            "Memgraph", "Dgraph", "NebulaGraph", "HugeGraph",
            "TypeDB", "TerminusDB", "Kuzu", "FalkorDB",
        ],
        "time_series_and_observability": [
            "InfluxDB", "TimescaleDB", "QuestDB", "VictoriaMetrics",
            "Prometheus", "OpenTSDB", "Apache IoTDB", "TDengine",
            "Druid", "Apache Pinot", "ClickHouse", "GreptimeDB",
            "M3DB", "Graphite", "CrateDB",
        ],
        "search_and_analytics_engines": [
            "Elasticsearch", "OpenSearch", "Apache Solr", "Vespa",
            "Typesense", "Meilisearch", "Quickwit", "Algolia",
            "Azure AI Search", "Amazon OpenSearch Service",
            "Google Vertex AI Search", "ClickHouse", "Apache Druid",
            "Apache Pinot", "Trino", "Presto", "Apache Doris",
            "StarRocks", "Databend", "Apache Doris",
        ],
        "vector_and_ai_data_stores": [
            "Pinecone", "Weaviate", "Qdrant", "Milvus", "Zilliz Cloud",
            "Chroma", "LanceDB", "pgvector", "Vespa", "Redis Vector Search",
            "MongoDB Atlas Vector Search", "Elasticsearch Vector Search",
            "OpenSearch Vector Engine", "Typesense Vector Search",
            "Azure AI Search Vector Search", "Oracle AI Vector Search",
            "Snowflake Cortex Search", "Vertex AI Vector Search",
            "Amazon OpenSearch vector engine", "Marqo", "Vald",
        ],
        "data_warehouse_and_lakehouse": [
            "Snowflake", "Google BigQuery", "Amazon Redshift",
            "Databricks Lakehouse", "Microsoft Fabric Warehouse",
            "Azure Synapse Analytics", "Teradata Vantage",
            "IBM Db2 Warehouse", "Oracle Autonomous Data Warehouse",
            "ClickHouse Cloud", "Firebolt", "Dremio",
            "Starburst Galaxy", "MotherDuck", "DuckDB",
            "Apache Iceberg", "Delta Lake", "Apache Hudi",
            "Trino", "Presto", "Apache Spark",
        ],
        "embedded_mobile_and_edge": [
            "SQLite", "DuckDB", "Realm", "ObjectBox", "Couchbase Lite",
            "PouchDB", "RxDB", "WatermelonDB", "Isar", "Hive",
            "Core Data", "CloudKit", "IndexedDB", "LevelDB",
            "RocksDB", "LMDB", "libSQL", "Turso",
        ],
        "blockchain_and_specialized_data": [
            "The Graph", "Dune", "Flipside", "Goldsky", "Subsquid",
            "Covalent", "Bitquery", "Google Blockchain Analytics",
            "Blockscout", "ClickHouse blockchain datasets",
        ],
    },
    "database_platform_and_api_providers": [
        "Amazon Web Services", "Google Cloud", "Microsoft Azure",
        "Oracle Cloud Infrastructure", "IBM Cloud", "Alibaba Cloud",
        "Tencent Cloud", "Huawei Cloud", "Baidu AI Cloud", "JD Cloud",
        "Volcengine", "Yandex Cloud", "Akamai Connected Cloud",
        "DigitalOcean", "OVHcloud", "Scaleway", "Hetzner",
        "Vultr", "Linode", "Cloudflare D1", "Cloudflare Durable Objects",
        "Cloudflare R2", "Firebase", "Supabase", "Appwrite",
        "PocketBase", "Nhost", "Hasura", "PostgREST",
        "Prisma Data Platform", "Convex", "Xata", "Nile",
        "Aiven", "Tembo", "Neon", "PlanetScale", "Cockroach Labs",
        "MongoDB", "Redis", "Elastic", "Confluent", "DataStax",
        "SingleStore", "Snowflake", "Databricks", "ClickHouse",
        "Pinecone", "Weaviate", "Qdrant", "Zilliz", "Milvus",
    ],
    "adult_industry_related_data_platforms": {
        "classification": "INDUSTRY_REFERENCE_ONLY_NOT_DATABASE_PROVIDERS",
        "status": "CATALOG_ONLY",
        "official_api_verified": False,
        "live_connection_verified": False,
        "note": (
            "These are adult-industry businesses, platforms, payment providers, "
            "advertising services, or hosting references—not a claim that each "
            "is a database provider or offers a public API. Keep this list separate "
            "from the database-engine catalog."
        ),
        "references": [
            "AbeloHost", "AlexHost", "BangBros", "Brazzers", "BlueAngelHost",
            "CCBill", "Clips4Sale", "CrakRevenue", "EPOCH", "Evil Angel",
            "ExoClick", "Fansly", "FapHouse", "FlokiNET", "HostKey",
            "HostSailor", "LoyalFans", "ManyVids", "Naughty America",
            "NSFWInfra", "OnlyFans", "Paxum", "Pornhub", "Reality Kings",
            "Segpay", "Shinjiru", "TrafficJunky", "Verotel", "ViceTemple",
            "xHamster", "XVideos",
        ],
    },
    "integration_policy": {
        "default_status": "CATALOG_ONLY",
        "require_official_documentation_before_adapter": True,
        "require_credentials_from_environment_or_secret_store": True,
        "never_claim_live_connection_without_successful_tests": True,
        "verify_terms_privacy_and_data_rights_before_ingestion": True,
    },
}
