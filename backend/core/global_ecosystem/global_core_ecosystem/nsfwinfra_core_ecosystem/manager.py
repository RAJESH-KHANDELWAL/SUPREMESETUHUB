"""Canonical manager for NSF Winfra Core metadata and catalog discovery."""
from __future__ import annotations
from typing import Any
from .catalog import ROOT_ID, ROOT_NAME
from .orchestrator import NSFWinfraCoreOrchestrator
from .service import NSFWinfraCoreService
class NSFWinfraCoreManager:
    NAME = ROOT_NAME
    ECOSYSTEM_ID = ROOT_ID
    def __init__(self) -> None:
        self._orchestrator = NSFWinfraCoreOrchestrator(); self._service = NSFWinfraCoreService()
    def status(self) -> dict[str, Any]: return self._service.status()
    def health(self) -> dict[str, Any]: return self._orchestrator.health()
    def list_ecosystems(self, *, enabled_only: bool = False) -> dict[str, Any]: return self._orchestrator.list_ecosystems(enabled_only=enabled_only)
    def get_ecosystem(self, ecosystem_id: str) -> dict[str, Any] | None: return self._orchestrator.get_ecosystem(ecosystem_id)
    def dependency_map(self) -> dict[str, Any]: return self._orchestrator.dependency_map()
    def master_catalog_reference(self, *, load_summary: bool = False) -> dict[str, Any]: return self._orchestrator.master_catalog_reference(load_summary=load_summary)
def get_manager() -> NSFWinfraCoreManager: return NSFWinfraCoreManager()
__all__ = ["NSFWinfraCoreManager", "get_manager"]
