"""Private SUPREME OWNER ADMIN control-plane metadata.

This module centralizes the owner's governance boundary and owned-platform registry.
It never returns credentials or claims external platforms are live-connected.
"""
from __future__ import annotations

import os
from typing import Any

from backend.supreme.config import (
    SUPREME_OWNER,
    USERNAME as SUPREME_OWNER_USERNAME,
)

WORDPRESS_SITES: tuple[dict[str, str], ...] = (
    {
        "site_id": "rajeshkhandelwalofficial",
        "display_name": "RAJESHKHANDELWALOFFICIAL WORDPRESS",
        "url_env": "WORDPRESS_SITE_URL",
        "username_env": "WORDPRESS_USERNAME",
        "application_password_env": "WORDPRESS_APPLICATION_PASSWORD",
        "database_prefix": "WORDPRESS",
    },
    {
        "site_id": "drrajeshkhandelwalibc",
        "display_name": "DR RAJESH KHANDELWAL IBC WORDPRESS",
        "url_env": "WORDPRESS_IBC_SITE_URL",
        "username_env": "WORDPRESS_IBC_USERNAME",
        "application_password_env": "WORDPRESS_IBC_APPLICATION_PASSWORD",
        "database_prefix": "WORDPRESS_IBC",
    },
)

OWNER_CONTROLLED_DOMAINS = (
    "IDENTITY",
    "SUPREME ECOSYSTEM",
    "BUSINESS AND COMPANY RECORDS",
    "AI AND AUTOMATION",
    "FILES AND STORAGE",
    "SECURITY AND ACCESS CONTROL",
    "API AND INTEGRATION SETTINGS",
    "WORDPRESS SITES",
    "DASHBOARD AND AUDIT",
)


class SupremeOwnerAdminService:
    """Describe the private owner boundary and WordPress resources."""

    def owner_status(self) -> dict[str, Any]:
        configured_username = str(SUPREME_OWNER_USERNAME or "").strip()
        return {
            "success": True,
            "control_plane": "SUPREME_OWNER_ADMIN",
            "privacy": "OWNER_ONLY",
            "owner_role": "SUPREME_OWNER_ADMIN",
            "owner_username_configured": bool(configured_username),
            "owner_username": configured_username or None,
            "owner_level": 100,
            "single_owner_policy": True,
            "self_service_owner_signup": False,
            "access_policy": (
                "Only the configured SUPREME owner account may access this control plane. "
                "ADMIN/OWNER roles in other systems do not automatically grant SUPREME owner access."
            ),
            "controlled_domains": list(OWNER_CONTROLLED_DOMAINS),
            "wordpress_site_count": len(WORDPRESS_SITES),
            "wordpress_sites_configured": sum(
                bool(os.getenv(site["url_env"], "").strip())
                and bool(os.getenv(site["username_env"], "").strip())
                and bool(os.getenv(site["application_password_env"], "").strip())
                for site in WORDPRESS_SITES
            ),
            "external_connections_verified": False,
        }

    def owned_platforms(self) -> list[dict[str, Any]]:
        """Return safe site metadata and config readiness, never credentials."""
        result = []
        for site in WORDPRESS_SITES:
            url = os.getenv(site["url_env"], "").strip()
            username_set = bool(os.getenv(site["username_env"], "").strip())
            password_set = bool(os.getenv(site["application_password_env"], "").strip())
            result.append({
                "site_id": site["site_id"],
                "display_name": site["display_name"],
                "url": url or None,
                "platform": "WORDPRESS",
                "ownership_scope": "SUPREME_OWNER_PRIVATE",
                "credentials_source": "BACKEND_DEPLOYMENT_SECRETS",
                "url_configured": bool(url),
                "username_configured": username_set,
                "application_password_configured": password_set,
                "credentials_configured": bool(url and username_set and password_set),
                "live_connection_verified": False,
                "database_prefix": site["database_prefix"],
            })
        return result

    def governance(self) -> dict[str, Any]:
        return {
            "success": True,
            "owner": self.owner_status(),
            "owned_platforms": self.owned_platforms(),
            "security_rules": [
                "No public SUPREME owner dashboard or owner-management endpoints",
                "Owner identity is determined by the configured backend username and a valid session token",
                "WordPress credentials stay in private backend deployment secrets",
                "External WordPress connectivity must be verified separately per site",
                "Never expose passwords, OAuth secrets, tokens, or database credentials in API responses",
            ],
        }
