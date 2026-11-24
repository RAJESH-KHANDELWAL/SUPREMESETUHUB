"""Document and flexible-schema database descriptors."""
from typing import Any
PLATFORMS = ("mongodb", "couchdb", "firestore", "azure_cosmos_db", "amazon_documentdb")
def describe_document_domain() -> dict[str, Any]:
    return {"domain":"document_nosql","platforms":list(PLATFORMS),"capabilities":["document_records","nested_objects","schema_evolution","secondary_indexes","replication"],"integration_status":"catalog_only"}
