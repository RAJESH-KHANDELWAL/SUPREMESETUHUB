"""API-owned ecosystem facade registry.

This module is intentionally independent of CORE and ENGINE packages.
"""
from __future__ import annotations
from copy import deepcopy
from typing import Any

class GlobalEcosystemManager:
    ROOT_ID = "GLOBAL-API-ECOSYSTEM"
    ROOT_NAME = "GLOBAL API ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self) -> None:
        from backend.api.global_ecosystem.global_api_ecosystem import CATEGORY_ECOSYSTEMS
        self._records: dict[str, dict[str, Any]] = {
            self.ROOT_ID: {"ecosystem_id": self.ROOT_ID, "name": self.ROOT_NAME,
                "ecosystem_type": "API_ROOT", "parent_id": None, "capabilities": ["API_CATALOG", "API_DISCOVERY"]}
        }
        for item in CATEGORY_ECOSYSTEMS:
            key = str(item["id"]).upper().replace("-", "_")
            ecosystem_id = f"GLOBAL-{key}-API-ECOSYSTEM"
            self._records[ecosystem_id] = {
                "ecosystem_id": ecosystem_id, "name": item["name"],
                "ecosystem_type": "API_CATEGORY", "parent_id": self.ROOT_ID,
                "capabilities": ["API_DISCOVERY"], "metadata": {"folder": item.get("folder")}
            }

    def status(self) -> dict[str, Any]:
        return {"success": True, "ecosystem_id": self.ROOT_ID, "name": self.ROOT_NAME,
                "version": self.VERSION, "status": "REGISTERED", "count": len(self._records)}
    def health(self) -> dict[str, Any]:
        return {"success": self.ROOT_ID in self._records, "root_exists": self.ROOT_ID in self._records,
                "registry_count": len(self._records), "status": "HEALTHY"}
    def list(self) -> dict[str, Any]:
        items=[deepcopy(x) for x in self._records.values()]
        return {"success": True, "count": len(items), "ecosystems": items}
    def names(self) -> dict[str, Any]:
        items=[x["name"] for x in self._records.values()]
        return {"success": True, "count": len(items), "names": items}
    def get(self, ecosystem_id: str) -> dict[str, Any] | None:
        item=self._records.get(ecosystem_id.strip())
        if item is None:
            needle=ecosystem_id.strip().casefold()
            item=next((x for x in self._records.values() if x["name"].casefold()==needle),None)
        return deepcopy(item) if item else None
    def exists(self, ecosystem_id: str) -> bool: return self.get(ecosystem_id) is not None
    def register(self, identity: Any) -> dict[str, Any]:
        item=identity.to_dict() if hasattr(identity,"to_dict") else deepcopy(identity)
        key=str(item.get("ecosystem_id","")).strip()
        if not key: return {"success":False,"error":"ECOSYSTEM_ID_REQUIRED"}
        if key in self._records: return {"success":False,"error":"ECOSYSTEM_ALREADY_EXISTS"}
        parent=item.get("parent_id") or self.ROOT_ID
        if parent not in self._records: return {"success":False,"error":"PARENT_NOT_FOUND","parent_id":parent}
        item["parent_id"]=parent; self._records[key]=item
        return {"success":True,"ecosystem":deepcopy(item)}
    def tree(self) -> dict[str, Any]:
        by_id={k:{**deepcopy(v),"children":[]} for k,v in self._records.items()}
        for k,v in self._records.items():
            parent=v.get("parent_id")
            if parent in by_id: by_id[parent]["children"].append(by_id[k])
        return {"success":True,"tree":by_id[self.ROOT_ID]}
    def connection_map(self) -> dict[str, Any]:
        edges=[{"source":v["parent_id"],"target":k,"relationship":"CONTAINS"}
               for k,v in self._records.items() if v.get("parent_id")]
        return {"success":True,"node_count":len(self._records),"edge_count":len(edges),"edges":edges}
EcosystemManager = GlobalEcosystemManager
