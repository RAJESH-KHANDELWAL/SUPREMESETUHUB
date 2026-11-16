"""Global Infrastructure Ecosystem adapter for the canonical model domain."""
from importlib import import_module

DOMAIN_ID = "model"
CANONICAL_PACKAGE = "backend.infrastructure.model"
CANONICAL_PATH = "backend/infrastructure/model"
OWNERSHIP = "CANONICAL_IMPLEMENTATION_RETAINED"


def load_domain():
    """Load the existing canonical domain package without duplicating it."""
    return import_module(CANONICAL_PACKAGE)


__all__ = ["DOMAIN_ID", "CANONICAL_PACKAGE", "CANONICAL_PATH", "OWNERSHIP", "load_domain"]
