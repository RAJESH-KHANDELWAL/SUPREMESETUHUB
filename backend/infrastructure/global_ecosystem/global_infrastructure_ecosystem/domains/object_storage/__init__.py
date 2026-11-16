"""Global Infrastructure Ecosystem adapter for the canonical object_storage domain."""
from importlib import import_module

DOMAIN_ID = "object_storage"
CANONICAL_PACKAGE = "backend.infrastructure.object_storage"
CANONICAL_PATH = "backend/infrastructure/object_storage"
OWNERSHIP = "CANONICAL_IMPLEMENTATION_RETAINED"


def load_domain():
    """Load the existing canonical domain package without duplicating it."""
    return import_module(CANONICAL_PACKAGE)


__all__ = ["DOMAIN_ID", "CANONICAL_PACKAGE", "CANONICAL_PATH", "OWNERSHIP", "load_domain"]
