"""Knowledge and retrieval-augmented generation building blocks."""
from .schemas import CatalogRecord

KNOWLEDGE_COMPONENTS = tuple(
    CatalogRecord(key, name, "knowledge_component", description)
    for key, name, description in (
        ("connectors", "Source connectors", "Read from approved files, databases and services."),
        ("ingestion", "Ingestion", "Import source material with provenance metadata."),
        ("parsing", "Parsing", "Extract text, tables and document structure."),
        ("chunking", "Chunking", "Split content into retrievable units."),
        ("embedding", "Embedding", "Represent content as vectors."),
        ("vector_store", "Vector store", "Persist and query vector representations."),
        ("hybrid_search", "Hybrid search", "Combine lexical and semantic retrieval."),
        ("reranking", "Reranking", "Improve candidate ordering."),
        ("grounding", "Grounding and citations", "Tie generated claims to retrieved evidence."),
        ("retention", "Retention and deletion", "Apply data lifecycle and deletion policies."),
    )
)
