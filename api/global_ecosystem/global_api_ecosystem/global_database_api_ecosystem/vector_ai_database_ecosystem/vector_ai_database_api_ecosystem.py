"""Catalog-only global database category module; not a live connector."""

VECTOR_AND_AI_DATA_STORES = {
    "category": "VECTOR_AND_AI_DATA_STORES",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "providers": [
        "Pinecone",
        "Weaviate",
        "Qdrant",
        "Milvus",
        "Zilliz Cloud",
        "Chroma",
        "LanceDB",
        "pgvector",
        "Redis Vector Search",
        "MongoDB Atlas Vector Search",
        "Elasticsearch Vector Search",
        "OpenSearch Vector Engine",
        "Typesense Vector Search",
        "Oracle AI Vector Search",
        "Snowflake Cortex Search",
        "Vertex AI Vector Search",
        "Marqo",
        "Vald"
    ],
}
