"""Graph database domain descriptors."""
from typing import Any
PLATFORMS = ("neo4j", "amazon_neptune", "janusgraph", "arangodb")
def describe_graph_domain() -> dict[str, Any]:
    return {"domain":"graph","platforms":list(PLATFORMS),"capabilities":["nodes","edges","relationship_traversal","path_queries","graph_analytics"],"integration_status":"catalog_only"}
