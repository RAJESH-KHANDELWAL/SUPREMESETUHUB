"""Global Infrastructure Ecosystem adapter for the canonical network domain."""
from importlib import import_module

DOMAIN_ID = "network"
CANONICAL_PACKAGE = "backend.infrastructure.network"
CANONICAL_PATH = "backend/infrastructure/network"
OWNERSHIP = "CANONICAL_IMPLEMENTATION_RETAINED"


def load_domain():
    """Load the existing canonical domain package without duplicating it."""
    return import_module(CANONICAL_PACKAGE)


__all__ = ["DOMAIN_ID", "CANONICAL_PACKAGE", "CANONICAL_PATH", "OWNERSHIP", "load_domain"]
