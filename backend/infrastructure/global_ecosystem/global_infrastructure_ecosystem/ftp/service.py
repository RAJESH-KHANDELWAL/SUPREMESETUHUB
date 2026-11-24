"""Named, read-only FTP profile service.

This service delegates all protocol work to the existing explicit-FTPS healthcheck.
It deliberately exposes no upload, delete, rename, or permission-changing methods.
"""
from __future__ import annotations

import os
from typing import Any, Mapping

from .healthcheck import FtpTarget, check_ftp_connection
from .profiles import FTP_PROFILES, get_ftp_profile


class FtpInfrastructureService:
    """Resolve existing deployment credentials and run safe FTPS checks."""

    def __init__(self, environ: Mapping[str, str] | None = None) -> None:
        self.environ = os.environ if environ is None else environ

    def list_profiles(self) -> list[dict[str, Any]]:
        """List profile readiness without returning usernames or credentials."""
        results = []
        for profile in FTP_PROFILES:
            values = profile.resolve(self.environ)
            results.append({
                "profile_id": values["profile_id"],
                "label": values["label"],
                "server_configured": values["server_configured"],
                "username_configured": values["username_configured"],
                "password_configured": values["password_configured"],
                "configured": values["configured"],
                "port": values["port"],
                "protocol": "explicit-ftps",
            })
        return results

    def check_profile(self, profile_id: str) -> dict[str, Any]:
        """Run the existing read-only FTPS login and starting-directory check."""
        profile = get_ftp_profile(profile_id)
        values = profile.resolve(self.environ)
        if not values["configured"]:
            return {
                "success": False,
                "status": "CONFIGURATION_INCOMPLETE",
                "profile_id": profile.profile_id,
                "missing": [
                    key for key, ready in (
                        ("server", values["server_configured"]),
                        ("username", values["username_configured"]),
                        ("password", values["password_configured"]),
                    ) if not ready
                ],
                "mutations_performed": False,
                "credentials_returned": False,
            }

        target = FtpTarget(
            host=str(values["server"]),
            username=str(values["username"]),
            password=str(values["password"]),
            port=int(values["port"]),
            timeout=int(values["timeout"]),
            site=profile.profile_id,
        )
        result = check_ftp_connection(target)
        return {
            **result,
            "profile_id": profile.profile_id,
            "mutations_performed": False,
            "credentials_returned": False,
        }


__all__ = ["FtpInfrastructureService"]
