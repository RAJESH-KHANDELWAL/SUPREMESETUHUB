"""Adapter manager for Global Dependencies Ecosystem."""

from backend.foundation.core.ecosystem_adapter import FoundationEcosystemAdapter


class GlobalDependenciesEcosystemManager(FoundationEcosystemAdapter):
    NAME = "GLOBAL_DEPENDENCIES_ECOSYSTEM"
    COMPONENT_KEY = "dependencies"


__all__ = ["GlobalDependenciesEcosystemManager"]
