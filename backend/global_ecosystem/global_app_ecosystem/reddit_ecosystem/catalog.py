"""Reddit provider metadata; catalog presence is not a live integration."""
PROVIDER = {
    "id": "reddit", "name": "Reddit", "origin": "global",
    "scope": "Communities, posts, moderation and approved API workflows",
    "credential_env": "REDDIT_CLIENT_ID",
    "integration_status": "scaffold", "live_connection_verified": False,
}
__all__ = ["PROVIDER"]
