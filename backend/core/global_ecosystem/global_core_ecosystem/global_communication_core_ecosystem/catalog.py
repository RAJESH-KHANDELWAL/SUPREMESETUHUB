"""Read-only Global Communication Core catalog.

Provider metadata is mirrored from the API catalog contract. Core does not import
or depend on the API layer; adapters and transport remain outside this package.
"""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path

ECOSYSTEM_ID = "GLOBAL-COMMUNICATION-CORE-ECOSYSTEM"
API_CATALOG_REF = "backend/api/global_ecosystem/global_api_ecosystem/global_communication_api_ecosystem/service.py"
CATEGORY_IDS = (
    "messaging", "email", "sms", "voice", "video_meetings", "social_messaging",
    "customer_support", "notifications", "dating_relationships",
    "sexual_wellness_education", "adult_platform_directory",
    "adult_creator_business", "age_verification_safety",
    "moderation_trust_safety", "privacy_security",
)
PROVIDERS = (
    {"provider_id": "aws_communication", "display_name": "Amazon Web Services Communication", "category": "cloud_communication", "package": "aws_communication_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "aws_ses", "display_name": "Amazon SES", "category": "email", "package": "aws_ses_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "aws_sns", "display_name": "Amazon SNS", "category": "sms_notifications", "package": "aws_sns_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "google_workspace", "display_name": "Google Workspace APIs", "category": "email_productivity", "package": "google_workspace_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "google_chat", "display_name": "Google Chat API", "category": "messaging", "package": "google_chat_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "google_meet", "display_name": "Google Meet API", "category": "video_meetings", "package": "google_meet_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "meta", "display_name": "Meta Platform APIs", "category": "social_messaging", "package": "meta_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "meta_whatsapp", "display_name": "WhatsApp Business Platform", "category": "business_messaging", "package": "meta_whatsapp_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "microsoft", "display_name": "Microsoft Graph APIs", "category": "communication", "package": "microsoft_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "microsoft_graph", "display_name": "Microsoft Graph", "category": "email_productivity", "package": "microsoft_graph_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "microsoft_teams", "display_name": "Microsoft Teams APIs", "category": "messaging_meetings", "package": "microsoft_teams_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "slack", "display_name": "Slack API", "category": "business_messaging", "package": "slack_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "twilio", "display_name": "Twilio APIs", "category": "sms_voice", "package": "twilio_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "zoom", "display_name": "Zoom APIs", "category": "video_meetings", "package": "zoom_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
    {"provider_id": "telegram", "display_name": "Telegram APIs", "category": "messaging", "package": "telegram_provider_core_ecosystem", "status": "CORE_CATALOG_ONLY", "live_connection_verified": False},
)


def list_providers():
    return deepcopy(list(PROVIDERS))


def get_provider(provider_id: str):
    if not isinstance(provider_id, str) or not provider_id.strip():
        return None
    needle = provider_id.strip().casefold()
    return next(
        (deepcopy(provider) for provider in PROVIDERS if provider["provider_id"] == needle),
        None,
    )


def list_categories():
    return list(CATEGORY_IDS)


def validate_catalog():
    ids = [provider["provider_id"] for provider in PROVIDERS]
    packages = [provider["package"] for provider in PROVIDERS]
    base = Path(__file__).parent
    missing_packages = [
        name for name in packages
        if not (base / name / "ecosystem_manifest.json").is_file()
    ]
    valid = (
        len(ids) == 15
        and len(set(ids)) == len(ids)
        and len(set(packages)) == len(packages)
        and not missing_packages
    )
    return {
        "valid": valid,
        "provider_count": len(ids),
        "category_count": len(CATEGORY_IDS),
        "missing_packages": missing_packages,
    }
