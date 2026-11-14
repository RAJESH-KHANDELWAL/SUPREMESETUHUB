"""Five logical FTP scopes backed by one shared account or explicit overrides.

The default deployment uses one physical FTP account. Each identity remains a
logical profile label; optional identity-specific environment variables can
override the shared account when separately provisioned later.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class FtpProfile:
    profile_id: str
    label: str
    identity_code: str
    server_env: str
    name_env: str
    username_env: str
    password_env: str
    port_env: str

    def resolve(self, environ: Mapping[str, str] | None = None) -> dict[str, str | int | bool]:
        values = os.environ if environ is None else environ

        # Identity-specific settings take precedence. Otherwise all five
        # logical scopes may use the one shared deployment FTP account.
        server = (values.get(self.server_env) or values.get("FTP_SERVER", "")).strip()
        name = (values.get(self.name_env) or self.label).strip()
        username = (values.get(self.username_env) or values.get("FTP_USERNAME", "")).strip()
        password = values.get(self.password_env) or values.get("FTP_PASSWORD", "")
        port_raw = (values.get(self.port_env) or values.get("FTP_PORT") or "21").strip()
        timeout_raw = values.get("FTP_TIMEOUT", "15").strip()
        try:
            port = int(port_raw)
        except ValueError:
            port = 0
        try:
            timeout = int(timeout_raw)
        except ValueError:
            timeout = 0

        return {
            "profile_id": self.profile_id,
            "label": self.label,
            "identity_code": self.identity_code,
            "server_configured": bool(server),
            "name_configured": bool(name),
            "username_configured": bool(username),
            "password_configured": bool(password),
            "configured": bool(server and name and username and password and 1 <= port <= 65535 and 1 <= timeout <= 120),
            "port": port,
            "timeout": timeout,
            "server": server,
            "host": server,
            "name": name,
            "username": username,
            "password": password,
        }


def _profile(identity: str) -> FtpProfile:
    prefix = identity
    return FtpProfile(
        profile_id=identity.casefold(),
        label=f"{identity} FTP",
        identity_code=identity,
        server_env=f"{prefix}_FTP_HOST",
        name_env=f"{prefix}_FTP_NAME",
        username_env=f"{prefix}_FTP_USER",
        password_env=f"{prefix}_FTP_PASSWORD",
        port_env=f"{prefix}_FTP_PORT",
    )


FTP_PROFILES: tuple[FtpProfile, ...] = tuple(
    _profile(identity)
    for identity in (
        "SUPREMESETUHUB",
        "RAJESHKHANDELWALOFFICIAL",
        "RAJESHKHANDELWAL",
        "DRRAJESHKHANDELWALIBCOFFICIAL",
        "DRRAJESHKHANDELWALIBC",
    )
)


def get_ftp_profile(profile_id: str) -> FtpProfile:
    normalized = profile_id.strip().casefold()
    for profile in FTP_PROFILES:
        if profile.profile_id == normalized:
            return profile
    raise KeyError(f"Unknown FTP profile: {profile_id}")


__all__ = ["FtpProfile", "FTP_PROFILES", "get_ftp_profile"]
