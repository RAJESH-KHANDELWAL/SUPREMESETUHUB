"""Catalog-only global database category module; not a live connector."""

SEARCH_AND_ANALYTICS_DATABASES = {
    "category": "SEARCH_AND_ANALYTICS_DATABASES",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "providers": [
        "Elasticsearch",
        "OpenSearch",
        "Apache Solr",
        "Vespa",
        "Typesense",
        "Meilisearch",
        "Quickwit",
        "Algolia",
        "Azure AI Search",
        "Amazon OpenSearch Service",
        "Google Vertex AI Search",
        "Trino",
        "Presto",
        "Apache Doris",
        "StarRocks",
        "Databend",
        "Dremio",
        "Starburst Galaxy"
    ],
}
