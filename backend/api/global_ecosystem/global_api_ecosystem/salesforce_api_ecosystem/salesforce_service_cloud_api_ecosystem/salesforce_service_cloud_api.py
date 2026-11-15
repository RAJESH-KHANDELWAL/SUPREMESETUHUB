"""Salesforce Service Cloud metadata scaffold; not a live connector."""
SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_service_cloud_api",
    "scope": "Cases, service workflows, knowledge, and supported service resources.",
    "authentication_setup": "Service Cloud licensing, object permissions, and approved API scopes.",
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}
__all__ = ["SERVICE_ECOSYSTEM"]
