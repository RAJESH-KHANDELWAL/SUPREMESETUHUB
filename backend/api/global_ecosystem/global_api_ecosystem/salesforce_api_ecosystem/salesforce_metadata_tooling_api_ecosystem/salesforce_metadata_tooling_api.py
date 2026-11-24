"""Salesforce Metadata and Tooling APIs metadata scaffold; not a live connector."""
SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_metadata_tooling_api",
    "scope": "Metadata deployment/retrieval, schema development, Apex and developer tooling resources.",
    "authentication_setup": "Modify Metadata/authoring permissions, deployment policy, and sandbox-first workflow.",
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}
__all__ = ["SERVICE_ECOSYSTEM"]
