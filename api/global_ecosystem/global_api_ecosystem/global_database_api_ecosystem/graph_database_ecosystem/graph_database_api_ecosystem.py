"""Catalog-only global database category module; not a live connector."""

GRAPH_DATABASES = {
    "category": "GRAPH_DATABASES",
    "status": "CATALOG_ONLY",
    "live_connection_verified": False,
    "providers": [
        "Neo4j",
        "Amazon Neptune",
        "Azure Cosmos DB Gremlin API",
        "ArangoDB",
        "OrientDB",
        "JanusGraph",
        "TigerGraph",
        "Memgraph",
        "Dgraph",
        "NebulaGraph",
        "HugeGraph",
        "TypeDB",
        "TerminusDB",
        "Kuzu",
        "FalkorDB"
    ],
}
