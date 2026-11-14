"""Environment-backed FTP profiles matching existing Hostinger workflows.

Only non-secret environment-variable names and profile labels are declared here.
Actual credentials stay in GitHub Actions secrets or the private server environment.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class FtpProfile:
    profile_id: str
    label: str
    server_env: str
    username_env: str
    password_env: str
    fallback_server: str = ""
    port_env: str = ""
    timeout_env: str = ""

    def resolve(self, environ: Mapping[str, str] | None = None) -> dict[str, str | int | bool]:
        values = os.environ if environ is None else environ
        server = values.get(self.server_env, "").strip() or self.fallback_server
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


# These names are taken from the repository's current deployment workflow setup.
# IBC's current workflow has a fixed server hostname; an environment override is
# supported without requiring a workflow change.
FTP_PROFILES: tuple[FtpProfile, ...] = (
    FtpProfile(
        profile_id="rajeshkhandelwalofficial",
        label="RAJESHKHANDELWALOFFICIAL Hostinger FTP",
        server_env="HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_SERVER",
        username_env="HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_USERNAME",
        password_env="HOSTINGER_RAJESHKHANDELWALOFFICIAL_FTP_PASSWORD",
    ),
    FtpProfile(
        profile_id="drrajeshkhandelwalibc",
        label="DR RAJESH KHANDELWAL IBC Hostinger FTP",
        server_env="HOSTINGER_DRRAJESHKHANDELWALIBC_FTP_SERVER",
        username_env="HOSTINGER_DRRAJESHKHANDELWALIBC_FTP_USERNAME",
        password_env="HOSTINGER_DRRAJESHKHANDELWALIBC_FTP_PASSWORD",
        fallback_server="ftp.drrajeshkhandelwalibc.com",
    ),
)


def get_ftp_profile(profile_id: str) -> FtpProfile:
    """Return a known profile by its stable ID."""
    normalized = profile_id.strip().casefold()
    for profile in FTP_PROFILES:
        if profile.profile_id == normalized:
            return profile
    raise KeyError(f"Unknown FTP profile: {profile_id}")


__all__ = ["FtpProfile", "FTP_PROFILES", "get_ftp_profile"]
