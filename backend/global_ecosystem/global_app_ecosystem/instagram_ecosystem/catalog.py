"""Instagram provider metadata; catalog presence is not a live integration."""
PROVIDER = {
    "id": "instagram", "name": "Instagram", "origin": "global",
    "scope": "Professional and creator publishing, media insights and messaging integrations",
    "credential_env": "META_ACCESS_TOKEN",
    "integration_status": "scaffold", "live_connection_verified": False,
}
__all__ = ["PROVIDER"]
