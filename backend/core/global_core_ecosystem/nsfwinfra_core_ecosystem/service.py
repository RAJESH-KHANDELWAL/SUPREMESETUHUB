"""Public service facade for NSF Winfra Core metadata."""
from __future__ import annotations
from typing import Any
from .manager import ROOT_ID, ROOT_NAME
from .orchestrator import NSFWinfraCoreOrchestrator
class NSFWinfraCoreService:
    def __init__(self) -> None: self._orchestrator = NSFWinfraCoreOrchestrator()
    def status(self) -> dict[str, Any]:
        health = self._orchestrator.health()
        return {"success": health["success"], "ecosystem_id": ROOT_ID, "name": ROOT_NAME, "status": "CORE_CATALOG_ONLY", "ecosystem_count": health["registered_ecosystems"], "live_connection_verified": False, "api_calls_performed": 0, "persistence_enabled": False, "execution_performed": False, "master_catalog_reference": self._orchestrator.master_catalog_reference()}
