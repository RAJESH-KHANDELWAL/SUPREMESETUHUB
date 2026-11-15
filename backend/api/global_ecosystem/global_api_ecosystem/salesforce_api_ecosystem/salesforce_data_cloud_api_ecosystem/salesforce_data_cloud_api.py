"""Salesforce Data Cloud metadata scaffold; not a live connector."""
SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_data_cloud_api",
    "scope": "Data Cloud ingestion, query, metadata, and activation interfaces.",
    "authentication_setup": "Data Cloud org entitlement, OAuth scopes, data space access, and service-specific permissions.",
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}
__all__ = ["SERVICE_ECOSYSTEM"]
