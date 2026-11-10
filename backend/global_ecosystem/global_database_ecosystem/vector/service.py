"""Vector database and retrieval metadata; no embedding or model calls."""
from typing import Any
PLATFORMS = ("pgvector", "milvus", "weaviate", "qdrant", "pinecone", "chroma")
def describe_vector_domain() -> dict[str, Any]:
    return {"domain":"vector_and_ai_data","platforms":list(PLATFORMS),"capabilities":["vector_index","similarity_search","hybrid_search","metadata_filtering","tenant_isolation"],"guardrails":["data_provenance","consent_and_licensing","deletion_propagation","access_control"],"integration_status":"catalog_only"}
