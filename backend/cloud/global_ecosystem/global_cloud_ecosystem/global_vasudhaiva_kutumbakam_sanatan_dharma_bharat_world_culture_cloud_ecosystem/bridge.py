"""Provider-neutral cloud bridge; no provider is presumed connected."""
from __future__ import annotations
from typing import Any
from backend.cloud.global_ecosystem.global_cloud_ecosystem.cultural_knowledge_cloud import CulturalKnowledgeCloudBridge

class GlobalCulturalCloud:
    def __init__(self, adapter: Any | None = None) -> None:
        self.bridge = CulturalKnowledgeCloudBridge(adapter=adapter)

    def status(self) -> dict[str, Any]:
        return {"ecosystem": "GLOBAL_VASUDHAIVA_KUTUMBAKAM_CLOUD", **self.bridge.status()}

    def sync_records(self, records: list[dict[str, Any]], operation: str = "UPSERT") -> Any:
        if operation not in {"UPSERT", "EXPORT", "IMPORT", "DELETE"}:
            raise ValueError("UNSUPPORTED_CULTURAL_CLOUD_OPERATION")
        return self.bridge.sync({"ecosystem": "GLOBAL_CULTURAL_KNOWLEDGE",
                                 "operation": operation, "records": records})
