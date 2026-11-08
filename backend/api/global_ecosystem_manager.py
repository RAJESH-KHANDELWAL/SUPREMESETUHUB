"""API-owned ecosystem facade registry.

This module is intentionally independent of CORE and ENGINE packages.
"""
from __future__ import annotations
from copy import deepcopy
from typing import Any

class GlobalEcosystemManager:
    ROOT_ID = "GLOBAL-ECOSYSTEM"
    ROOT_NAME = "GLOBAL ECOSYSTEM"
    VERSION = "1.0.0"

    def __init__(self) -> None:
        # API owns its own category catalog; no runtime import from CORE/ENGINE.
        categories = (
            ("people", "GLOBAL PEOPLE ECOSYSTEM", "global_people_ecosystem"),
            ("business", "GLOBAL BUSINESS ECOSYSTEM", "global_business_ecosystem"),
            ("companies", "GLOBAL COMPANY AND COMPANIES API ECOSYSTEM", "global_company_companies_api_ecosystem"),
            ("platforms", "GLOBAL PLATFORMS API ECOSYSTEM", "global_platforms_api_ecosystem"),
            ("server", "GLOBAL SERVER API ECOSYSTEM", "global_server_api_ecosystem"),
            ("ai", "GLOBAL AI API ECOSYSTEM", "global_ai_api_ecosystem"),
            ("software-ai", "GLOBAL SOFTWARE AI ECOSYSTEM", "global_software_ai_ecosystem"),
            ("cloud", "GLOBAL CLOUD API ECOSYSTEM", "global_cloud_api_ecosystem"),
            ("security", "GLOBAL SECURITY API ECOSYSTEM", "global_security_api_ecosystem"),
            ("individual", "GLOBAL INDIVIDUAL API ECOSYSTEM", "global_individual_api_ecosystem"),
            ("developer", "GLOBAL DEVELOPER API ECOSYSTEM", "global_developer_api_ecosystem"),
            ("communication", "GLOBAL COMMUNICATION API ECOSYSTEM", "global_communication_api_ecosystem"),
            ("language", "GLOBAL LANGUAGE API ECOSYSTEM", "global_language_api_ecosystem"),
            ("video", "GLOBAL VIDEO API ECOSYSTEM", "global_video_api_ecosystem"),
            ("payment", "GLOBAL PAYMENT API ECOSYSTEM", "global_payment_api_ecosystem"),
            ("storage", "GLOBAL STORAGE API ECOSYSTEM", "global_storage_api_ecosystem"),
            ("system", "GLOBAL SYSTEM API ECOSYSTEM", "global_system_api_ecosystem"),
            ("hosting", "GLOBAL HOSTING API ECOSYSTEM", "global_hosting_api_ecosystem"),
            ("intimacy", "GLOBAL RELATIONSHIP AND INTIMACY ECOSYSTEM", "global_relationship_and_intimacy_ecosystem"),
            ("domain", "GLOBAL DOMAIN API ECOSYSTEM", "global_domain_api_ecosystem"),
            ("web", "GLOBAL WEB API ECOSYSTEM", "global_web_api_ecosystem"),
            ("social-media", "GLOBAL SOCIAL MEDIA API ECOSYSTEM", "global_social_media_api_ecosystem"),
            ("freelancer", "GLOBAL FREELANCER API ECOSYSTEM", "global_freelancer_api_ecosystem"),
            ("database", "GLOBAL DATABASE API ECOSYSTEM", "global_database_api_ecosystem"),
        )
        self._records: dict[str, dict[str, Any]] = {
            self.ROOT_ID: {"ecosystem_id": self.ROOT_ID, "name": self.ROOT_NAME,
                "ecosystem_type": "API_ROOT", "parent_id": None, "capabilities": ["API_CATALOG", "API_DISCOVERY"]}
        }
        for category_id, category_name, folder in categories:
            key = category_id.upper().replace("-", "_")
            ecosystem_id = (
                f"GLOBAL-{key}-ECOSYSTEM"
                if category_id in {"people", "business"}
                else f"GLOBAL-{key}-API-ECOSYSTEM"
            )
            self._records[ecosystem_id] = {
                "ecosystem_id": ecosystem_id, "name": category_name,
                "ecosystem_type": "API_CATEGORY", "parent_id": self.ROOT_ID,
                "capabilities": ["API_DISCOVERY"], "metadata": {"folder": folder}
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
