"""Global Infrastructure Ecosystem adapter for the canonical dns domain.

Implementation remains in backend.infrastructure.dns; this package provides
stable ecosystem discovery without copying or relocating runtime code.
"""
from importlib import import_module

DOMAIN_ID = "dns"
CANONICAL_PACKAGE = "backend.infrastructure.dns"
CANONICAL_PATH = "backend/infrastructure/dns"
OWNERSHIP = "CANONICAL_IMPLEMENTATION_RETAINED"


def load_domain():
    """Load and return the existing canonical domain package."""
    return import_module(CANONICAL_PACKAGE)


__all__ = ["DOMAIN_ID", "CANONICAL_PACKAGE", "CANONICAL_PATH", "OWNERSHIP", "load_domain"]
