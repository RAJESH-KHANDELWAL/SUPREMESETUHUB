"""Read-only discovery service for affiliate platform CORE modules."""
from __future__ import annotations

from .catalog import get_platform, list_platforms
from .models import AffiliatePlatformIdentity

class AffiliatePlatformModuleService:
    """Expose canonical platform identities without provider API calls."""

    def list(self, *, region: str | None = None, include_candidates: bool = True) -> list[AffiliatePlatformIdentity]:
        return [
            AffiliatePlatformIdentity.from_record(record)
            for record in list_platforms(region=region, include_candidates=include_candidates)
        ]

    def get(self, platform_id: str) -> AffiliatePlatformIdentity | None:
        record = get_platform(platform_id)
        return AffiliatePlatformIdentity.from_record(record) if record else None

    def status(self) -> dict[str, object]:
        platforms = self.list()
        return {
            "success": True,
            "platform_count": len(platforms),
            "program_platform_count": sum(item.record_type == "PROGRAM_PLATFORM" for item in platforms),
            "network_candidate_count": sum(item.record_type == "NETWORK_CANDIDATE" for item in platforms),
            "verified_program_count": sum(item.verification_status == "VERIFIED" for item in platforms),
            "live_connections_verified": 0,
            "discovery_only_candidates": True,
        }

__all__ = ["AffiliatePlatformModuleService"]
