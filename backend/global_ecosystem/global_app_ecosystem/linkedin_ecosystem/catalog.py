"""LinkedIn provider metadata; catalog presence is not a live integration."""
PROVIDER = {
    "id": "linkedin", "name": "LinkedIn", "origin": "global",
    "scope": "Professional identity, organization pages and approved partner integrations",
    "credential_env": "LINKEDIN_ACCESS_TOKEN",
    "integration_status": "scaffold", "live_connection_verified": False,
}
__all__ = ["PROVIDER"]
