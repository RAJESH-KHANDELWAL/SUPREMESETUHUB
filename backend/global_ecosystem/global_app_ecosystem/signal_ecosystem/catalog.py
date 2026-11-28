"""Signal provider metadata; catalog presence is not a live integration."""
PROVIDER = {
    "id": "signal",
    "name": "Signal",
    "origin": "global",
    "scope": "Private messaging and calling; integration requires an explicitly deployed supported bridge",
    "authentication": "Deployment-specific bridge credentials",
    "credential_env": "SIGNAL_SERVICE_URL",
    "integration_status": "scaffold",
    "live_connection_verified": False,
}

__all__ = ["PROVIDER"]
