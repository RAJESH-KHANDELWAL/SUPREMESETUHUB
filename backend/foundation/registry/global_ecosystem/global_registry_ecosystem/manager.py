"""Adapter manager for Global Registry Ecosystem."""

from backend.foundation.core.ecosystem_adapter import FoundationEcosystemAdapter


class GlobalRegistryEcosystemManager(FoundationEcosystemAdapter):
    NAME = "GLOBAL_REGISTRY_ECOSYSTEM"
    COMPONENT_KEY = "registry"


__all__ = ["GlobalRegistryEcosystemManager"]
