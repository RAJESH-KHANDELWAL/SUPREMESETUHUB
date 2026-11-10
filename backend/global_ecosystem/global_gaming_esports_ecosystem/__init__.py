"""Domain package entry point; detailed metadata is maintained centrally."""
from ..domain_registry import get_domain_profile

_DOMAIN_ID = __name__.rsplit(".", 1)[-1]
DOMAIN_PROFILE = get_domain_profile(_DOMAIN_ID)


def get_profile() -> dict:
    """Return this package's detached domain profile."""
    if DOMAIN_PROFILE is None:
        raise RuntimeError(f"No registered domain profile for {_DOMAIN_ID}")
    return get_domain_profile(_DOMAIN_ID)


__all__ = ["DOMAIN_PROFILE", "get_profile"]
