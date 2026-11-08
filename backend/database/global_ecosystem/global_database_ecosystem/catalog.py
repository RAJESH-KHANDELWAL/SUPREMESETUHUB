"""Canonical independent GLOBAL DATABASE ECOSYSTEM catalog."""

LAYER = "DATABASE"
ROOT_ID = "GLOBAL-DATABASE-ECOSYSTEM"
ROOT_NAME = "GLOBAL DATABASE ECOSYSTEM"
MIRRORED_API_DIRECTORY_COUNT = 3382
PROVIDER_IDS = ("aws", "google", "mega", "microsoft", "proton")

def get_catalog():
    return {
        "ecosystem_id": ROOT_ID,
        "name": ROOT_NAME,
        "layer": LAYER,
        "mirrored_directory_count": MIRRORED_API_DIRECTORY_COUNT,
        "provider_ids": list(PROVIDER_IDS),
        "independent": True,
        "connection_status": "not_configured",
        "live_connections_verified": False,
    }
