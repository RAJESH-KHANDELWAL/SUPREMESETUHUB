"""Adapter to the canonical CORE foundation package."""
from importlib import import_module

CANONICAL_PACKAGE = "backend.core"
CANONICAL_PATH = "backend/core"
INTEGRATION_STATUS = "FOUNDATION_LINKED"


def load_core():
    """Load the existing CORE foundation package."""
    return import_module(CANONICAL_PACKAGE)


__all__ = ["CANONICAL_PACKAGE", "CANONICAL_PATH", "INTEGRATION_STATUS", "load_core"]
