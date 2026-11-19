"""Adapter manager for Global Sync Ecosystem."""

from backend.foundation.core.ecosystem_adapter import FoundationEcosystemAdapter


class GlobalSyncEcosystemManager(FoundationEcosystemAdapter):
    NAME = "GLOBAL_SYNC_ECOSYSTEM"
    COMPONENT_KEY = "sync"


__all__ = ["GlobalSyncEcosystemManager"]
