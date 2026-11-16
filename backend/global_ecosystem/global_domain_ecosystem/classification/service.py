"""Map a domain identifier to its catalog group."""
from ..catalog import DOMAIN_GROUPS

def classify_domain(domain_id: str) -> dict | None:
    key = str(domain_id or "").strip().casefold()
    for group, items in DOMAIN_GROUPS.items():
        if key in items:
            return {"domain_id": key, "group": group, "status": "CATALOG_MATCH"}
    return None

__all__ = ["classify_domain"]
