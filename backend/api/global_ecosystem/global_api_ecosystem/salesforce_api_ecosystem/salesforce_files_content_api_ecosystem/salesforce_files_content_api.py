"""Salesforce Files and Content metadata scaffold; not a live connector."""
SERVICE_ECOSYSTEM = {
    "provider_id": "salesforce",
    "service_id": "salesforce_files_content_api",
    "scope": "ContentVersion, ContentDocument, links, and file metadata operations.",
    "authentication_setup": "REST OAuth, file object permissions, and content-sharing controls.",
    "adapter_implemented": False,
    "live_connection_verified": False,
    "credential_persistence_implemented": False,
}
__all__ = ["SERVICE_ECOSYSTEM"]
