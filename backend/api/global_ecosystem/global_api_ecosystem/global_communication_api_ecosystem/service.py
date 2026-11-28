"""Catalog and status services.

This module deliberately reports integrations as unconfigured until provider
credentials, permissions, webhook verification, and tests are supplied.
It does not send messages or access adult-content services.
"""

from copy import deepcopy
from typing import Any, Dict, List, Optional

ECOSYSTEM_ID = "GLOBAL_COMMUNICATION_API_ECOSYSTEM"
VERSION = "1.0.0"

CATEGORIES: List[Dict[str, Any]] = [
    {"category_id": "messaging", "display_name": "Messaging & Chat", "tier": "standard_to_enterprise", "audience": ["consumer", "business", "enterprise"], "providers": ["meta_whatsapp", "google_chat", "microsoft_teams", "slack", "telegram"], "compliance_controls": ["consent", "rate_limits", "abuse_reporting"]},
    {"category_id": "email", "display_name": "Email & Business Mail", "tier": "standard_to_enterprise", "audience": ["consumer", "business", "enterprise"], "providers": ["google_workspace", "microsoft_graph", "aws_ses"], "compliance_controls": ["sender_authentication", "unsubscribe", "anti_spam"]},
    {"category_id": "sms", "display_name": "SMS & OTP", "tier": "standard_to_enterprise", "audience": ["consumer", "business", "enterprise"], "providers": ["twilio", "aws_sns"], "compliance_controls": ["opt_in", "sender_rules", "rate_limits"]},
    {"category_id": "voice", "display_name": "Voice & Telephony", "tier": "standard_to_enterprise", "audience": ["consumer", "business", "enterprise"], "providers": ["twilio", "aws_communication"], "compliance_controls": ["consent", "recording_disclosure", "regional_law"]},
    {"category_id": "video_meetings", "display_name": "Video Meetings & Webinars", "tier": "standard_to_enterprise", "audience": ["consumer", "business", "enterprise"], "providers": ["zoom", "google_meet", "microsoft_teams"], "compliance_controls": ["meeting_consent", "recording_disclosure", "access_controls"]},
    {"category_id": "social_messaging", "display_name": "Social & Community Messaging", "tier": "standard_to_premium", "audience": ["creator", "business", "community"], "providers": ["meta", "telegram", "slack"], "compliance_controls": ["platform_policy", "consent", "moderation"]},
    {"category_id": "customer_support", "display_name": "Customer Support & Contact Center", "tier": "standard_to_enterprise", "audience": ["business", "enterprise"], "providers": ["twilio", "aws_communication", "microsoft"], "compliance_controls": ["data_retention", "recording_disclosure", "access_controls"]},
    {"category_id": "notifications", "display_name": "Transactional & Product Notifications", "tier": "standard_to_enterprise", "audience": ["developer", "business", "enterprise"], "providers": ["aws_sns", "google", "microsoft"], "compliance_controls": ["purpose_limitation", "rate_limits", "delivery_logs"]},
    {"category_id": "dating_relationships", "display_name": "Dating & Relationships", "tier": "consumer_to_premium", "audience": ["adults_18_plus"], "providers": [], "compliance_controls": ["age_18_plus", "consent", "block_report", "privacy", "anti_harassment"]},
    {"category_id": "sexual_wellness_education", "display_name": "Sexual Wellness & Education", "tier": "standard_to_premium", "audience": ["adults", "educational_services"], "providers": [], "compliance_controls": ["age_appropriate_access", "medical_content_review", "privacy", "regional_law"]},
    {"category_id": "adult_platform_directory", "display_name": "Adult 18+ Platform Directory", "tier": "restricted_adult", "audience": ["verified_adults_18_plus"], "providers": [], "compliance_controls": ["strict_age_verification", "lawful_content_only", "consent_only", "no_minors", "no_nonconsensual_content", "regional_access_controls"]},
    {"category_id": "adult_creator_business", "display_name": "Adult Creator Business Tools", "tier": "restricted_adult", "audience": ["verified_adult_creators", "verified_adult_customers"], "providers": [], "compliance_controls": ["age_verification", "creator_consent", "content_rights", "payout_compliance", "privacy"]},
    {"category_id": "age_verification_safety", "display_name": "Age Verification, Consent & Safety", "tier": "advanced", "audience": ["platform_operators", "adult_users"], "providers": [], "compliance_controls": ["data_minimization", "secure_verification", "appeals", "audit_logs"]},
    {"category_id": "moderation_trust_safety", "display_name": "Moderation, Trust & Safety", "tier": "advanced_to_enterprise", "audience": ["community", "business", "enterprise"], "providers": [], "compliance_controls": ["reporting", "human_review", "appeals", "audit_logs"]},
    {"category_id": "privacy_security", "display_name": "Privacy, Security & Identity", "tier": "advanced_to_enterprise", "audience": ["all"], "providers": [], "compliance_controls": ["encryption", "least_privilege", "retention_limits", "incident_response"]},
]

PROVIDERS: List[Dict[str, Any]] = [
    {"provider_id": "aws_communication", "display_name": "Amazon Web Services Communication", "category": "cloud_communication"},
    {"provider_id": "aws_ses", "display_name": "Amazon SES", "category": "email"},
    {"provider_id": "aws_sns", "display_name": "Amazon SNS", "category": "sms_notifications"},
    {"provider_id": "google_workspace", "display_name": "Google Workspace APIs", "category": "email_productivity"},
    {"provider_id": "google_chat", "display_name": "Google Chat API", "category": "messaging"},
    {"provider_id": "google_meet", "display_name": "Google Meet API", "category": "video_meetings"},
    {"provider_id": "meta", "display_name": "Meta Platform APIs", "category": "social_messaging"},
    {"provider_id": "meta_whatsapp", "display_name": "WhatsApp Business Platform", "category": "business_messaging"},
    {"provider_id": "microsoft", "display_name": "Microsoft Graph APIs", "category": "communication"},
    {"provider_id": "microsoft_graph", "display_name": "Microsoft Graph", "category": "email_productivity"},
    {"provider_id": "microsoft_teams", "display_name": "Microsoft Teams APIs", "category": "messaging_meetings"},
    {"provider_id": "slack", "display_name": "Slack API", "category": "business_messaging"},
    {"provider_id": "twilio", "display_name": "Twilio APIs", "category": "sms_voice"},
    {"provider_id": "zoom", "display_name": "Zoom APIs", "category": "video_meetings"},
    {"provider_id": "telegram", "display_name": "Telegram APIs", "category": "messaging"},
]

SAFETY_CONTROLS = {
    "adult_access_default": "disabled",
    "minimum_adult_age": 18,
    "age_verification_required_for_restricted_adult_categories": True,
    "allow_minors_in_adult_categories": False,
    "allow_nonconsensual_or_exploitative_content": False,
    "allow_illegal_content": False,
    "require_provider_terms_and_regional_legal_review": True,
    "store_provider_secrets_in_server_side_secret_manager": True,
    "never_commit_api_keys_or_tokens": True,
    "live_actions_require_explicit_user_confirmation": True,
}


def list_categories(tier: Optional[str] = None) -> List[Dict[str, Any]]:
    items = deepcopy(CATEGORIES)
    if tier:
        items = [item for item in items if item["tier"] == tier]
    return items


def get_category(category_id: str) -> Optional[Dict[str, Any]]:
    for item in CATEGORIES:
        if item["category_id"] == category_id:
            return deepcopy(item)
    return None


def list_providers() -> List[Dict[str, Any]]:
    return [dict(item, integration_status="not_configured", official_api_required=True,
                 supported_regions=["IN", "GLOBAL"]) for item in PROVIDERS]


def ecosystem_status() -> Dict[str, Any]:
    providers = list_providers()
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "version": VERSION,
        "category_count": len(CATEGORIES),
        "provider_count": len(providers),
        "connected_provider_count": 0,
        "live_messaging_enabled": False,
        "integrations": providers,
        "safety_controls": deepcopy(SAFETY_CONTROLS),
    }
