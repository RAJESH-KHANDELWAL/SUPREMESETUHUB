"""Local read-only catalog facade; HTTP endpoints belong in the API layer."""
from .ecosystem_taxonomy import load_taxonomy
from .ecosystem_service import EcosystemService


def get_catalog() -> dict:
    return {
        "ecosystem": EcosystemService().describe(),
        "taxonomy": load_taxonomy(),
        "mode": "READ_ONLY_CATALOG",
    }
