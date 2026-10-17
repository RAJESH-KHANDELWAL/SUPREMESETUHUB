"""Private SUPREME OWNER ADMIN control-plane metadata.

Every configured owner Google account is treated as a PRIMARY owner account.
No Google account is classified as secondary by this registry.
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

# Legacy variables are accepted as email sources for compatibility only.
# They do not establish a primary/secondary hierarchy in this registry.
GOOGLE_OWNER_EMAIL_SOURCE_VARS = (
    "SUPREME_OWNER_EMAILS",
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
GOOGLE_OWNER_PURPOSES = (
    "BANKING_AND_FINANCIAL_NOTIFICATIONS",
    "SENSITIVE_DOCUMENTS_AND_RECORDS",
    "PLATFORM_OWNERSHIP_AND_ADMINISTRATION",
    "GOOGLE_WORKSPACE_AND_PRODUCTIVITY",
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
    "GLOBAL BUSINESS COACHING AND CONSULTING",
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
        """List all configured owner Google accounts at equal PRIMARY tier.

        The list is an allowlist only. It is not OAuth consent or proof that Gmail,
        Drive, banking systems, or other platforms are connected. Never place banking
        passwords, card data, recovery codes, or provider tokens in this registry.
        """
        emails: list[str] = []

        def add_emails(raw: str) -> None:
            for item in raw.replace(";", ",").split(","):
                normalized = item.strip().casefold()
                if normalized and normalized not in emails:
                    emails.append(normalized)

        # Canonical variable supports any number of owner-controlled Gmail accounts.
        add_emails(os.getenv("GOOGLE_OWNER_ACCOUNT_EMAILS", ""))

        # Include all configured owner emails; legacy variable names do not imply rank.
        for env_name in GOOGLE_OWNER_EMAIL_SOURCE_VARS:
            add_emails(os.getenv(env_name, ""))

        oauth_configured = self._google_oauth_configured()
        return [
            {
                "account_id": f"google-owner-{index + 1}",
                "email": email,
                "provider": "GOOGLE",
                "owner_account_tier": "PRIMARY",
                "ownership_scope": "SUPREME_OWNER_PRIVATE",
                "purposes": list(GOOGLE_OWNER_PURPOSES),
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

    def global_business_coach_profile(self) -> dict[str, Any]:
        """Describe the public-facing global coaching and consulting contact.

        This registry entry does not itself forward messages or prove that the
        mailbox is connected. Lead intake, forwarding, and delivery need separate
        setup and end-to-end verification.
        """
        email = os.getenv(
            "GLOBAL_BUSINESS_COACH_EMAIL",
            "drrajeshkhandelwalibc@gmail.com",
        ).strip().casefold()
        social_username = os.getenv(
            "GLOBAL_BUSINESS_COACH_SOCIAL_USERNAME",
            "DRRAJESHKHANDELWALIBC",
        ).strip().lstrip("@")
        website = os.getenv(
            "GLOBAL_BUSINESS_COACH_WEBSITE",
            "https://drrajeshkhandelwalibc.com",
        ).strip().rstrip("/")
        website_form = os.getenv("GLOBAL_BUSINESS_COACH_WEBSITE_FORM_URL", "").strip()
        whatsapp_number = os.getenv("GLOBAL_BUSINESS_COACH_WHATSAPP_NUMBER", "917611967229").strip()
        whatsapp_digits = "".join(character for character in whatsapp_number if character.isdigit())
        return {
            "profile_id": "dr-rajesh-khandelwal-ibc-global-business-coach",
            "brand": "DR RAJESH KHANDELWAL IBC",
            "role": "GLOBAL BUSINESS COACH AND INDEPENDENT BUSINESS CONSULTANT",
            "contact_email": email or None,
            "website": website or None,
            "contact_channels": {
                "email": {
                    "address": email or None,
                    "mailto_url": f"mailto:{email}" if email else None,
                    "configured": bool(email),
                    "delivery_verified": False,
                },
                "whatsapp": {
                    "url": f"https://wa.me/{whatsapp_digits}" if whatsapp_digits else None,
                    "number_configured": bool(whatsapp_digits),
                    "delivery_verified": False,
                },
                "website_form": {
                    "url": website_form or None,
                    "configured": bool(website_form),
                    "delivery_verified": False,
                },
            },
            "social_identity": {
                "intended_username": social_username or None,
                "handle": f"@{social_username}" if social_username else None,
                "platforms_requested": [
                    "FACEBOOK",
                    "INSTAGRAM",
                    "LINKEDIN",
                    "YOUTUBE",
                    "X",
                    "THREADS",
                    "TELEGRAM",
                ],
                "profile_urls_verified": False,
                "username_availability_verified": False,
                "note": "This registers the requested handle in the ecosystem profile; it does not create or edit third-party social accounts.",
            },
            "audience": [
                "BHARAT AND GLOBAL WORLD",
                "BUSINESS OWNERS AND PROFESSIONALS",
                "ENTREPRENEURS AND STARTUP FOUNDERS",
                "ENTREPRENEURSHIP AND BUSINESS BUILDERS",
                "FREELANCERS AND INDEPENDENT CONSULTANTS",
                "PEOPLE SEEKING BUSINESS COLLABORATIONS",
                "WORK, SERVICE, AND PARTNERSHIP OPPORTUNITIES",
            ],
            "scope": [
                "BUSINESS COACHING AND CONSULTING",
                "BUSINESS NETWORKING AND COLLABORATION",
                "ENTREPRENEURSHIP AND STARTUP CONNECTIONS",
                "FREELANCE, WORK, AND SERVICE LEADS",
                "WORDPRESS AND WEBSITE DEVELOPMENT",
                "AFFILIATE MARKETING",
                "STARTUP AND ENTREPRENEURSHIP GUIDANCE",
                "DIGITAL MARKETING AND SEO",
                "AUTHORIZED ECOSYSTEM AND PLATFORM INQUIRIES",
            ],
            "intake_status": "CONTACT_REGISTERED_NOT_LIVE_VERIFIED",
            "automatic_forwarding_enabled": False,
            "mailbox_connection_verified": False,
        }

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
            "global_business_coach_contact_registered": bool(self.global_business_coach_profile()["contact_email"]),
            "google_owner_account_tier": "ALL_PRIMARY",
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
            "global_business_coach_profile": self.global_business_coach_profile(),
            "owned_platforms": self.owned_platforms(),
            "security_rules": [
                "No public SUPREME owner dashboard or owner-management endpoints",
                "All configured owner Google accounts are equal PRIMARY accounts; no secondary tier is assigned by this registry",
                "Owner identity is determined by the configured backend username and a valid session token",
                "WordPress credentials and Google OAuth client secrets stay in private backend deployment secrets",
                "Google account allowlisting is not OAuth consent and does not prove Gmail or Drive is connected",
                "Global business coach contact registration does not itself enable email forwarding or verify mailbox delivery",
                "Banking passwords, payment credentials, recovery codes, and OAuth tokens must not be stored in the account registry",
                "Google OAuth tokens require encrypted persistent storage before live use",
                "External WordPress connectivity must be verified separately per site",
                "Never expose passwords, OAuth secrets, tokens, or database credentials in API responses",
            ],
        }
