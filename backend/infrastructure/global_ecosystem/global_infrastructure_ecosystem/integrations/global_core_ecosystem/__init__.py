"""Adapter to the canonical GLOBAL CORE ECOSYSTEM hierarchy."""
from importlib import import_module

CANONICAL_PACKAGE = "backend.core.global_ecosystem.global_core_ecosystem"
CANONICAL_PATH = "backend/core/global_ecosystem/global_core_ecosystem"
INFRASTRUCTURE_CORE_PACKAGE = CANONICAL_PACKAGE + ".global_infrastructure_core_ecosystem"
INTEGRATION_STATUS = "FOUNDATION_LINKED"


def load_global_core_ecosystem():
    """Load the existing global CORE ecosystem package."""
    return import_module(CANONICAL_PACKAGE)


def load_infrastructure_core():
    """Load the dedicated infrastructure CORE contracts."""
    return import_module(INFRASTRUCTURE_CORE_PACKAGE)


__all__ = ["CANONICAL_PACKAGE", "CANONICAL_PATH", "INFRASTRUCTURE_CORE_PACKAGE", "INTEGRATION_STATUS", "load_global_core_ecosystem", "load_infrastructure_core"]
