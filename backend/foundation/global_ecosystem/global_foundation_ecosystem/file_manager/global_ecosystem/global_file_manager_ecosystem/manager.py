"""Adapter manager for Global File Manager Ecosystem."""

from backend.foundation.core.ecosystem_adapter import FoundationEcosystemAdapter


class GlobalFileManagerEcosystemManager(FoundationEcosystemAdapter):
    NAME = "GLOBAL_FILE_MANAGER_ECOSYSTEM"
    COMPONENT_KEY = "file_manager"


__all__ = ["GlobalFileManagerEcosystemManager"]
