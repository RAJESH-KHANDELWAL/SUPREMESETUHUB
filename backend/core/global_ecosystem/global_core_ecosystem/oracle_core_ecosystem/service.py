"""Public status facade; master catalog is a read-only reference."""
from pathlib import Path
import json
from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME, PROVIDER_ID, PARENT_ID, MASTER_CATALOG_PATH, MASTER_CATALOG_TARGET
from .orchestrator import OracleCoreOrchestrator

class OracleCoreEcosystemService:
    def __init__(self) -> None:
        self._orchestrator = OracleCoreOrchestrator()

    def master_catalog_reference(self) -> dict:
        path = Path(__file__).resolve().parents[4] / "GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
        result = {"path": MASTER_CATALOG_PATH, "target_unique_entries": MASTER_CATALOG_TARGET,
                  "access_mode": "READ_ONLY_ON_DEMAND", "available": path.is_file()}
        if path.is_file():
            try:
                expansion = json.loads(path.read_text(encoding="utf-8")).get("expansion", {})
                result["current_unique_entries"] = expansion.get("current_unique_entries")
                result["remaining_unique_entries"] = expansion.get("remaining_unique_entries")
            except (OSError, json.JSONDecodeError):
                result["read_error"] = True
        return result

    def status(self) -> dict:
        return {"ecosystem_id": ECOSYSTEM_ID, "name": ECOSYSTEM_NAME, "provider": PROVIDER_ID,
                "parent_id": PARENT_ID, "health": self._orchestrator.health(),
                "master_catalog": self.master_catalog_reference(),
                "live_connection_verified": False, "api_calls_performed": 0,
                "remote_operations_enabled": False}
