"""Read-only controller for registered explicit-FTPS profiles."""
from __future__ import annotations

from typing import Any

from .service import FtpInfrastructureService


class FtpInfrastructureController:
    """Expose profile readiness and safe FTPS checks; no remote file mutations."""

    def __init__(self, service: FtpInfrastructureService | None = None) -> None:
        self.service = service or FtpInfrastructureService()

    def list_profiles(self) -> list[dict[str, Any]]:
        return self.service.list_profiles()

    def check_profile(self, profile_id: str) -> dict[str, Any]:
        return self.service.check_profile(profile_id)


__all__ = ["FtpInfrastructureController"]
