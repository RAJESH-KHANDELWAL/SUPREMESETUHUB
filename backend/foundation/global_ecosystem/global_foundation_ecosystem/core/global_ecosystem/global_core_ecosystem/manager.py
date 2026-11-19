"""Adapter manager for Global Core Ecosystem."""

from backend.foundation.core.ecosystem_adapter import FoundationEcosystemAdapter


class GlobalCoreEcosystemManager(FoundationEcosystemAdapter):
    NAME = "GLOBAL_CORE_ECOSYSTEM"
    COMPONENT_KEY = "core"


__all__ = ["GlobalCoreEcosystemManager"]
