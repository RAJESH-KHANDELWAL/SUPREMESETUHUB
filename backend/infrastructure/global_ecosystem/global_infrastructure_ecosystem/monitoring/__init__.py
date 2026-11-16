"""Global Infrastructure Ecosystem adapter for the canonical monitoring domain.

Implementation remains in backend.infrastructure.monitoring; this package provides
stable ecosystem discovery without copying or relocating runtime code.
"""
from importlib import import_module

DOMAIN_ID = "monitoring"
CANONICAL_PACKAGE = "backend.infrastructure.monitoring"
CANONICAL_PATH = "backend/infrastructure/monitoring"
OWNERSHIP = "CANONICAL_IMPLEMENTATION_RETAINED"


def load_domain():
    """Load and return the existing canonical domain package."""
    return import_module(CANONICAL_PACKAGE)


__all__ = ["DOMAIN_ID", "CANONICAL_PACKAGE", "CANONICAL_PATH", "OWNERSHIP", "load_domain"]
