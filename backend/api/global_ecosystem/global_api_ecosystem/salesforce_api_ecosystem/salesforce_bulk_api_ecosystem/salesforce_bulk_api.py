"""Salesforce Bulk API 2.0 metadata scaffold; not a live connector."""
SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_bulk_api",
    "scope": "Asynchronous high-volume ingest and query jobs.",
    "authentication_setup": "Bulk API access, OAuth, object permissions, and data governance controls.",
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}
__all__ = ["SERVICE_ECOSYSTEM"]
