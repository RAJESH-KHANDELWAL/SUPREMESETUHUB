"""Domain-specific discovery catalog for the Global App Ecosystem."""
from .scope import get_domain

DOMAIN_ID = __name__.rsplit(".", 2)[-2].removesuffix("_ecosystem")
DOMAIN_PROFILE = get_domain(DOMAIN_ID)
if DOMAIN_PROFILE is None:
    raise RuntimeError(f"Domain package is missing from APP scope: {DOMAIN_ID}")

def get_catalog():
    """Return a defensive copy of this application's domain profile."""
    return {
        **DOMAIN_PROFILE,
        "examples": list(DOMAIN_PROFILE.get("examples", [])),
        "safeguards": list(DOMAIN_PROFILE.get("safeguards", [])),
    }

__all__ = ["DOMAIN_ID", "DOMAIN_PROFILE", "get_catalog"]
