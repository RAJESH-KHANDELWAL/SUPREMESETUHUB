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

GOOGLE_OWNER_ACCOUNT_ENV_VARS = (
    "SUPREME_OWNER_PRIMARY_EMAIL",
    "SUPREME_OWNER_SECONDARY_EMAIL",
    "SUPREME_OWNER_RECOVERY_EMAIL",
)
GOOGLE_OWNER_SERVICES = (
    "GMAIL",
    "GOOGLE_DRIVE",
    "GOOGLE_CALENDAR",
    "GOOGLE_DOCS",
    "GOOGLE_SHEETS",
    "GOOGLE_CONTACTS",
    "GOOGLE_TASKS",
    "GOOGLE_MEET",
    "YOUTUBE",
    "GOOGLE_ANALYTICS",
)

OWNER_CONTROLLED_DOMAINS = (
    "IDENTITY",
    "SUPREME ECOSYSTEM",
    "BUSINESS AND COMPANY RECORDS",
    "AI AND AUTOMATION",
    "FILES AND STORAGE",
    "SECURITY AND ACCESS CONTROL",
    "API AND INTEGRATION SETTINGS",
    "GOOGLE ACCOUNTS AND SERVICES",
    "WORDPRESS SITES",
    "DASHBOARD AND AUDIT",
)


class SupremeOwnerAdminService:
    """Describe the private owner boundary and registered owner resources."""

    @staticmethod
    def _google_oauth_configured() -> bool:
        return all(
            os.getenv(name, "").strip()
            for name in ("GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REDIRECT_URI")
        )

    def google_owner_accounts(self) -> list[dict[str, Any]]:
        """Return owner-approved Google identities from deployment environment only.

        Account allowlisting is not OAuth consent and does not imply that Gmail or Drive
        has been connected. OAuth callback/state validation, encrypted token storage,
        and provider API verification must be completed separately.
        """
        emails: list[str] = []
        # Optional consolidated list supports deployments with more than two accounts.
        consolidated = os.getenv("GOOGLE_OWNER_ACCOUNT_EMAILS", "")
        for email in consolidated.replace(";", ",").split(","):
            normalized = email.strip().casefold()
            if normalized and normalized not in emails:
                emails.append(normalized)

        for env_name in GOOGLE_OWNER_ACCOUNT_ENV_VARS:
            normalized = os.getenv(env_name, "").strip().casefold()
            if normalized and normalized not in emails:
                emails.append(normalized)

        oauth_configured = self._google_oauth_configured()
        return [
            {
                "account_id": f"google-owner-{index + 1}",
                "email": email,
                "provider": "GOOGLE",
                "ownership_scope": "SUPREME_OWNER_PRIVATE",
                "approved_services": list(GOOGLE_OWNER_SERVICES),
                "oauth_app_configured": oauth_configured,
                "authorization_status": (
                    "CONSENT_REQUIRED" if oauth_configured else "OAUTH_APP_NOT_CONFIGURED"
                ),
                "connected": False,
                "live_connection_verified": False,
                "token_storage_status": "NOT_IMPLEMENTED",
            }
            for index, email in enumerate(emails)
        ]

    def owner_status(self) -> dict[str, Any]:
        configured_username = str(SUPREME_OWNER_USERNAME or "").strip()
        google_accounts = self.google_owner_accounts()
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
            "google_owner_account_count": len(google_accounts),
            "google_oauth_app_configured": self._google_oauth_configured(),
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
            "google_owner_accounts": self.google_owner_accounts(),
            "owned_platforms": self.owned_platforms(),
            "security_rules": [
                "No public SUPREME owner dashboard or owner-management endpoints",
                "Owner identity is determined by the configured backend username and a valid session token",
                "WordPress credentials and Google OAuth client secrets stay in private backend deployment secrets",
                "Google account allowlisting is not OAuth consent and does not prove Gmail or Drive is connected",
                "Google OAuth tokens must not be exposed in API responses and require encrypted persistent storage before live use",
                "External WordPress connectivity must be verified separately per site",
                "Never expose passwords, OAuth secrets, tokens, or database credentials in API responses",
            ],
        }
