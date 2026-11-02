"""Private owner-admin governance metadata for the SUPREME ECOSYSTEM.

This module reports configuration readiness only. It does not authenticate
requests, establish live external connections, or expose credentials.
"""
from __future__ import annotations

import os
from typing import Any


ECOSYSTEM_DOMAINS = (
    "API AND INTEGRATIONS",
    "AI ECOSYSTEM",
    "BUSINESS ECOSYSTEM",
    "CLOUD ECOSYSTEM",
    "USERS AND ROLES",
    "SECURITY AND AUDIT",
    "WORDPRESS ECOSYSTEM SITES",
    "ECOSYSTEM CONFIGURATION",
)

WORDPRESS_SITES = (
    {
        "site_id": "rajeshkhandelwalofficial",
        "display_name": "RAJESHKHANDELWALOFFICIAL WORDPRESS",
        "url_env": "WORDPRESS_SITE_URL",
        "username_env": "WORDPRESS_USERNAME",
        "application_password_env": "WORDPRESS_APPLICATION_PASSWORD",
    },
    {
        "site_id": "drrajeshkhandelwalibc",
        "display_name": "DR RAJESH KHANDELWAL IBC WORDPRESS",
        "url_env": "WORDPRESS_IBC_SITE_URL",
        "username_env": "WORDPRESS_IBC_USERNAME",
        "application_password_env": "WORDPRESS_IBC_APPLICATION_PASSWORD",
    },
)


class SupremeEcosystemOwnerAdminService:
    """Return safe status for the separate ecosystem owner-admin boundary."""

    def owner_status(self) -> dict[str, Any]:
        username = os.getenv("SUPREME_OWNER_USERNAME", "").strip()
        return {
            "success": True,
            "control_plane": "SUPREME_OWNER_ADMIN_ECOSYSTEM",
            "privacy": "OWNER_ONLY",
            "owner_role": "SUPREME_OWNER_ADMIN_ECOSYSTEM",
            "owner_username_configured": bool(username),
            "self_service_owner_signup": False,
            "controlled_domains": list(ECOSYSTEM_DOMAINS),
            "wordpress_site_count": len(WORDPRESS_SITES),
            "wordpress_sites_configured": sum(
                bool(os.getenv(site["url_env"], "").strip())
                and bool(os.getenv(site["username_env"], "").strip())
                and bool(os.getenv(site["application_password_env"], "").strip())
                for site in WORDPRESS_SITES
            ),
            "external_connections_verified": False,
            "runtime_status": "METADATA_ONLY_UNTIL_ROUTES_AUTH_AND_TESTS_ARE_WIRED",
        }

    def wordpress_sites(self) -> list[dict[str, Any]]:
        """List WordPress site readiness without returning credentials."""
        sites = []
        for site in WORDPRESS_SITES:
            url = os.getenv(site["url_env"], "").strip()
            username_set = bool(os.getenv(site["username_env"], "").strip())
            password_set = bool(os.getenv(site["application_password_env"], "").strip())
            sites.append({
                "site_id": site["site_id"],
                "display_name": site["display_name"],
                "platform": "WORDPRESS",
                "url": url or None,
                "url_configured": bool(url),
                "username_configured": username_set,
                "application_password_configured": password_set,
                "credentials_configured": bool(url and username_set and password_set),
                "live_connection_verified": False,
                "credentials_source": "BACKEND_DEPLOYMENT_SECRETS",
            })
        return sites

    def governance(self) -> dict[str, Any]:
        return {
            "success": True,
            "owner": self.owner_status(),
            "wordpress_sites": self.wordpress_sites(),
            "security_rules": [
                "Keep the ecosystem owner-admin separate from the root SUPREME owner-admin",
                "Require authenticated owner-only backend routes before exposing control actions",
                "Do not store WordPress passwords, application passwords, API keys, or tokens in source control",
                "Use WordPress Application Passwords over HTTPS and store them only in deployment secrets",
                "Do not claim a WordPress site is connected until a live authenticated health check succeeds",
                "Audit privileged changes and apply least-privilege permissions",
            ],
        }
