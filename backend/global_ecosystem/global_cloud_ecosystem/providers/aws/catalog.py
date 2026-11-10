"""AWS provider metadata; catalog presence is not a live integration claim."""
PROVIDER = {
    "provider_id": "aws",
    "name": "Amazon Web Services",
    "category": "public_cloud",
    "origin": "global",
    "integration_status": "adapter_scaffold",
    "live_connection_verified": False,
    "capabilities": ["compute", "object_storage", "database", "network", "identity"],
}
