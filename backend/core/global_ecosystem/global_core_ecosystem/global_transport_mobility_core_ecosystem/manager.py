"""Canonical manager for Global Transport and Mobility Core."""
from .catalog import ECOSYSTEM_ID, PARENT_ID, STATUS, list_catalog
from .contracts import core_result, validate_identifier
from .policy import CORE_POLICY

class TransportMobilityCoreManager:
    def status(self):
        return core_result(success=True, ecosystem_id=ECOSYSTEM_ID, status=STATUS, data={"parent_id": PARENT_ID, "entry_count": len(list_catalog()), "policy": dict(CORE_POLICY)})
    def list_entries(self):
        items = list_catalog()
        return core_result(success=True, ecosystem_id=ECOSYSTEM_ID, status=STATUS, data={"count": len(items), "entries": items})
    def get_entry(self, entry_id):
        key = validate_identifier(entry_id)
        return next((item for item in list_catalog() if item["id"] == key), None)

def get_manager(): return TransportMobilityCoreManager()
