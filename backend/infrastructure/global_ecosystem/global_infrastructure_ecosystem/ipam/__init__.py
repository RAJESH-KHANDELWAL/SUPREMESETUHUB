"""Global Infrastructure Ecosystem adapter for the canonical ipam domain.

Implementation remains in backend.infrastructure.ipam; this package provides
stable ecosystem discovery without copying or relocating runtime code.
"""
from importlib import import_module

DOMAIN_ID = "ipam"
CANONICAL_PACKAGE = "backend.infrastructure.ipam"
CANONICAL_PATH = "backend/infrastructure/ipam"
OWNERSHIP = "CANONICAL_IMPLEMENTATION_RETAINED"


def load_domain():
    """Load and return the existing canonical domain package."""
    return import_module(CANONICAL_PACKAGE)


__all__ = ["DOMAIN_ID", "CANONICAL_PACKAGE", "CANONICAL_PATH", "OWNERSHIP", "load_domain"]
