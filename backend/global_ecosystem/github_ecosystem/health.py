"""Local package health; does not probe GitHub."""
from .service import catalog

def health():
    return {"provider": "github", "status": "catalog_ready",
            "capability_count": len(catalog()), "network_probe_performed": False}
