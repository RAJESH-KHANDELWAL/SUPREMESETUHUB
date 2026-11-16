"""Global Infrastructure Ecosystem adapter for the canonical load_balancer domain.

Implementation remains in backend.infrastructure.load_balancer; this package provides
stable ecosystem discovery without copying or relocating runtime code.
"""
from importlib import import_module

DOMAIN_ID = "load_balancer"
CANONICAL_PACKAGE = "backend.infrastructure.load_balancer"
CANONICAL_PATH = "backend/infrastructure/load_balancer"
OWNERSHIP = "CANONICAL_IMPLEMENTATION_RETAINED"


def load_domain():
    """Load and return the existing canonical domain package."""
    return import_module(CANONICAL_PACKAGE)


__all__ = ["DOMAIN_ID", "CANONICAL_PACKAGE", "CANONICAL_PATH", "OWNERSHIP", "load_domain"]
