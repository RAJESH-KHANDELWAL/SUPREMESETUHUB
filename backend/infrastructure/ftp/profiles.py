"""Canonical brand-named Hostinger FTP credential profiles.

The profile ID/display name follows the brand identity. The FTP username remains
the exact account username created in Hostinger hPanel; do not assume it equals
the brand name. All passwords are loaded from secret environment variables.
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
    username_env: str
    password_env: str
    port_env: str = ""
    timeout_env: str = ""

    def resolve(self, environ: Mapping[str, str] | None = None) -> dict[str, str | int | bool]:
        values = os.environ if environ is None else environ
        server = values.get(self.server_env, "").strip()
        username = values.get(self.username_env, "").strip()
        password = values.get(self.password_env, "")
        port_raw = values.get(self.port_env, "21") if self.port_env else "21"
        timeout_raw = values.get(self.timeout_env, "15") if self.timeout_env else "15"
        try:
            port = int(port_raw)
            timeout = int(timeout_raw)
        except ValueError:
            port, timeout = 21, 15
            numeric_settings_valid = False
        else:
            numeric_settings_valid = 1 <= port <= 65535 and 1 <= timeout <= 120

        return {
            "profile_id": self.profile_id,
            "label": self.label,
            "identity_code": self.identity_code,
            "server_configured": bool(server),
            "username_configured": bool(username),
            "password_configured": bool(password),
            "configured": bool(server and username and password and numeric_settings_valid),
            "port": port,
            "timeout": timeout,
            "server": server,
            "username": username,
            "password": password,
        }


FTP_PROFILES: tuple[FtpProfile, ...] = (
    FtpProfile(
        profile_id="supremesetuhub",
        label="SUPREMESETUHUB Hostinger FTP",
        identity_code="SUPREMESETUHUB",
        server_env="HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_SERVER",
        username_env="HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_USERNAME",
        password_env="HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_PASSWORD",
    ),
    FtpProfile(
        profile_id="rajeshkhandelwalofficial",
        label="RAJESHKHANDELWALOFFICIAL Hostinger FTP",
        identity_code="RAJESHKHANDELWALOFFICIAL",
        server_env="HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_SERVER",
        username_env="HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_USERNAME",
        password_env="HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_PASSWORD",
    ),
    FtpProfile(
        profile_id="rajeshkhandelwal",
        label="RAJESHKHANDELWAL Hostinger FTP",
        identity_code="RAJESHKHANDELWAL",
        server_env="HOSTINGER_RAJESHKHANDELWAL_FTP_SERVER",
        username_env="HOSTINGER_RAJESHKHANDELWAL_FTP_USERNAME",
        password_env="HOSTINGER_RAJESHKHANDELWAL_FTP_PASSWORD",
    ),
    FtpProfile(
        profile_id="drrajeshkhandelwalibcofficial",
        label="DRRAJESHKHANDELWALIBCOFFICIAL Hostinger FTP",
        identity_code="DRRAJESHKHANDELWALIBCOFFICIAL",
        server_env="HOSTINGER_DRRAJESHKHANDELWALIBCOFFICIAL_FTP_SERVER",
        username_env="HOSTINGER_DRRAJESHKHANDELWALIBCOFFICIAL_FTP_USERNAME",
        password_env="HOSTINGER_DRRAJESHKHANDELWALIBCOFFICIAL_FTP_PASSWORD",
    ),
    FtpProfile(
        profile_id="drrajeshkhandelwalibc",
        label="DRRAJESHKHANDELWALIBC Hostinger FTP",
        identity_code="DRRAJESHKHANDELWALIBC",
        server_env="HOSTINGER_DRRAJESHKHANDELWALIBC_FTP_SERVER",
        username_env="HOSTINGER_DRRAJESHKHANDELWALIBC_FTP_USERNAME",
        password_env="HOSTINGER_DRRAJESHKHANDELWALIBC_FTP_PASSWORD",
    ),
)


def get_ftp_profile(profile_id: str) -> FtpProfile:
    normalized = profile_id.strip().casefold()
    for profile in FTP_PROFILES:
        if profile.profile_id == normalized:
            return profile
    raise KeyError(f"Unknown FTP profile: {profile_id}")


__all__ = ["FtpProfile", "FTP_PROFILES", "get_ftp_profile"]
