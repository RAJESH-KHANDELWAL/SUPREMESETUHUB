"""Read-only Twilio Core service; never calls Twilio APIs."""
from __future__ import annotations
from pathlib import Path
from typing import Any
from .catalog import API_CATALOG_PATH, get_catalog, list_products
from .contracts import CoreResult, Readiness, TenantContext
from .policy import TwilioCorePolicy

MASTER_CATALOG_PATH = "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
MASTER_CATALOG_TARGET = 2468

class TwilioCoreService:
    def status(self) -> dict[str, Any]:
        catalog = get_catalog()
        return {
            "success": True,
            "ecosystem_id": catalog["ecosystem_id"],
            "status": Readiness.CATALOG_ONLY.value,
            "provider": catalog["provider"],
            "product_family_count": len(catalog["product_families"]),
            "category_count": len(catalog["category_refs"]),
            "api_catalog_ref": API_CATALOG_PATH,
            "credentials_configured": False,
            "live_connection_verified": False,
            "api_transport_in_core": False,
        }

    def health(self) -> dict[str, Any]:
        backend_root = Path(__file__).resolve().parents[4]
        api_catalog = backend_root / API_CATALOG_PATH.removeprefix("backend/")
        master_catalog = backend_root / MASTER_CATALOG_PATH.removeprefix("backend/")
        return {
            "success": True,
            "status": "METADATA_HEALTHY",
            "api_catalog_available": api_catalog.is_file(),
            "master_catalog_available": master_catalog.is_file(),
            "master_catalog_path": MASTER_CATALOG_PATH,
            "master_catalog_target_unique_entries": MASTER_CATALOG_TARGET,
            "master_catalog_access": "READ_ONLY_ON_DEMAND",
            "live_connection_verified": False,
        }

    def inventory(self) -> dict[str, Any]:
        return {
            "provider": get_catalog()["provider"],
            "products": list_products(),
            "categories": get_catalog()["category_refs"],
        }

    def authorize_metadata_capability(self, capability: str, context: TenantContext) -> dict:
        try:
            result = TwilioCorePolicy.authorize_metadata_capability(capability, context)
        except (TypeError, ValueError) as exc:
            return CoreResult(False, "TWILIO-CORE-ECOSYSTEM", "POLICY_DENIED", errors=[str(exc)]).to_dict()
        return CoreResult(
            result["allowed"], "TWILIO-CORE-ECOSYSTEM", result["status"],
            data=result if result["allowed"] else {}, errors=[] if result["allowed"] else [result["reason"]],
            request_id=context.request_id,
        ).to_dict()
