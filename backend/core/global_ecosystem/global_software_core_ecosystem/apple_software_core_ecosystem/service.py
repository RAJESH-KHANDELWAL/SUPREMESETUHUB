"""Read-only Apple provider descriptor; no API adapter is implemented."""
from .ecosystem_config import CAPABILITIES, DOMAINS, PROVIDER_ID, PROVIDER_NAME, STATUS


def describe() -> dict:
    return {"provider_id": PROVIDER_ID, "name": PROVIDER_NAME, "status": STATUS, "domains": list(DOMAINS), "capabilities": list(CAPABILITIES), "live_connection_verified": False, "execution_enabled": False}
