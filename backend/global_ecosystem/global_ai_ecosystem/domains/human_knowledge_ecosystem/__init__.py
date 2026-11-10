"""Domain package metadata shared by all domain subpackages."""
from ..domain_catalog import get_domain_profile
DOMAIN_ID = __name__.rsplit(".", 1)[-1].removesuffix("_ecosystem")
DOMAIN_PROFILE = get_domain_profile(DOMAIN_ID)
if DOMAIN_PROFILE is None:
    raise RuntimeError(f"Unregistered AI domain package: {DOMAIN_ID}")
__all__ = ["DOMAIN_ID", "DOMAIN_PROFILE"]
