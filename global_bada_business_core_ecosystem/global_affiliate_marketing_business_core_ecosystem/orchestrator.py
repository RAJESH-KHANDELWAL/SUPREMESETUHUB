"""Provider-neutral affiliate CORE orchestration and readiness reporting."""
from __future__ import annotations

from typing import Any

from .manager import GlobalAffiliateMarketingCoreManager
from .service import AffiliateMarketingCoreService

class AffiliateMarketingCoreOrchestrator:
    """Compose catalog discovery and an optional repository-backed business service."""

    def __init__(self, repository: Any | None = None) -> None:
        self.manager = GlobalAffiliateMarketingCoreManager()
        self.service = AffiliateMarketingCoreService(repository) if repository is not None else None

    def status(self) -> dict[str, Any]:
        status = self.manager.status()
        status["workflow_service_configured"] = self.service is not None
        status["provider_api_calls"] = 0
        status["payout_execution_enabled"] = False
        return status

    def discover(self, *, region: str | None = None) -> dict[str, Any]:
        records = self.manager.list_platforms(region=region)
        return {"success": True, "count": len(records), "platforms": records}

__all__ = ["AffiliateMarketingCoreOrchestrator"]
