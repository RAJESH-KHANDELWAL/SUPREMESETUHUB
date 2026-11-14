"""Five brand-named FTP profiles using the requested HOST/NAME/USER/PASSWORD/PORT pattern.

HOST, USER, PASSWORD and PORT must be populated with the exact FTP account
details from Hostinger hPanel before connecting. NAME is a logical profile label.
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
        server = values.get(self.server_env, "").strip()
        name = values.get(self.name_env, "").strip()
        username = values.get(self.username_env, "").strip()
        password = values.get(self.password_env, "")
        port_raw = values.get(self.port_env, "").strip()
        try:
            port = int(port_raw) if port_raw else 0
        except ValueError:
            port = 0

        return {
            "profile_id": self.profile_id,
            "label": self.label,
            "identity_code": self.identity_code,
            "server_configured": bool(server),
            "name_configured": bool(name),
            "username_configured": bool(username),
            "password_configured": bool(password),
            "configured": bool(server and name and username and password and 1 <= port <= 65535),
            "port": port,
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
