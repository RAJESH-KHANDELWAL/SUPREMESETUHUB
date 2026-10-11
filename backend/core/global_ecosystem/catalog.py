"""Canonical GLOBAL ECOSYSTEM catalog under CORE."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


ROOT_ID = "GLOBAL-ECOSYSTEM"

ROOT: dict[str, Any] = {
    "ecosystem_id": ROOT_ID,
    "name": "GLOBAL ECOSYSTEM",
    "ecosystem_type": "MASTER",
    "repository_ref": None,
    "status": "REGISTERED",
    "enabled": True,
    "capabilities": [
        "CENTRAL_REGISTRY",
        "HIERARCHY",
        "DISCOVERY",
    ],
    "parent_id": None,
    "metadata": {},
}


# 18 original categories + 16 new API, Language, and Video ecosystems.
CATEGORIES: tuple[dict[str, Any], ...] = (
    {
        "ecosystem_id": "GLOBAL-SUPREME-ECOSYSTEM",
        "name": "GLOBAL SUPREME ECOSYSTEM",
        "ecosystem_type": "CORE",
        "capabilities": ["ADMINISTRATION", "PLATFORM_CONTROL", "INTEGRATION"],
    },
    {
        "ecosystem_id": "GLOBAL-PEOPLE-ECOSYSTEM",
        "name": "GLOBAL PEOPLE ECOSYSTEM",
        "ecosystem_type": "AUDIENCE",
        "capabilities": ["IDENTITY", "PROFILE", "COMMUNITY"],
    },
    {
        "ecosystem_id": "GLOBAL-BUSINESS-ECOSYSTEM",
        "name": "GLOBAL BUSINESS ECOSYSTEM",
        "ecosystem_type": "AUDIENCE",
        "capabilities": ["ORGANIZATION", "BUSINESS", "TEAM", "PROJECTS"],
    },
    {
        "ecosystem_id": "GLOBAL-ENTREPRENEUR-ECOSYSTEM",
        "name": "GLOBAL ENTREPRENEUR ECOSYSTEM",
        "ecosystem_type": "AUDIENCE",
        "capabilities": ["STARTUPS", "VENTURES", "BUSINESS_DEVELOPMENT"],
    },
    {
        "ecosystem_id": "GLOBAL-CLOUD-ECOSYSTEM",
        "name": "GLOBAL CLOUD ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["COMPUTE", "INFRASTRUCTURE", "NETWORKING"],
    },
    {
        "ecosystem_id": "GLOBAL-CLOUD-STORAGE-ECOSYSTEM",
        "name": "GLOBAL CLOUD STORAGE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["OBJECT_STORAGE", "FILE_STORAGE", "DATA_STORAGE"],
    },
    {
        "ecosystem_id": "GLOBAL-STORAGE-ECOSYSTEM",
        "name": "GLOBAL STORAGE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["STORAGE_CATALOG", "ADAPTERS", "ASSET_METADATA"],
    },
    {
        "ecosystem_id": "GLOBAL-SERVER-ECOSYSTEM",
        "name": "GLOBAL SERVER ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["SERVER_MANAGEMENT", "DEPLOYMENT", "MONITORING"],
    },
    {
        "ecosystem_id": "GLOBAL-WEB-HOSTING-ECOSYSTEM",
        "name": "GLOBAL WEB & HOSTING ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["WEBSITES", "DOMAINS", "HOSTING", "CMS"],
    },
    {
        "ecosystem_id": "GLOBAL-SOCIAL-MEDIA-ECOSYSTEM",
        "name": "GLOBAL SOCIAL MEDIA ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["SOCIAL_NETWORKS", "PUBLISHING", "COMMUNITIES"],
    },
    {
        "ecosystem_id": "GLOBAL-CREATOR-MEDIA-ECOSYSTEM",
        "name": "GLOBAL CREATOR & MEDIA ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "CREATOR_TOOLS",
            "MEDIA",
            "PUBLISHING",
            "MONETIZATION",
        ],
    },
    {
        "ecosystem_id": "GLOBAL-ADULT-ENTERTAINMENT-ECOSYSTEM",
        "name": "GLOBAL ADULT ENTERTAINMENT ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "AGE_RESTRICTED_SERVICES",
            "CREATOR_SERVICES",
            "PLATFORM_DISCOVERY",
        ],
        "metadata": {
            "age_restricted": True,
            "age_verification_required": True,
            "consent_and_rights_required": True,
            "legal_compliance_required": True,
        },
    },
    {
        "ecosystem_id": "GLOBAL-AI-AUTOMATION-ECOSYSTEM",
        "name": "GLOBAL AI & AUTOMATION ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["AI_MODELS", "AI_APIS", "AUTOMATION"],
    },
    {
        "ecosystem_id": "GLOBAL-PAYMENT-COMMERCE-ECOSYSTEM",
        "name": "GLOBAL PAYMENT & COMMERCE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["PAYMENTS", "BILLING", "SUBSCRIPTIONS", "COMMERCE"],
    },
    {
        "ecosystem_id": "GLOBAL-IDENTITY-SECURITY-ECOSYSTEM",
        "name": "GLOBAL IDENTITY & SECURITY ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["AUTHENTICATION", "AUTHORIZATION", "PRIVACY"],
    },
    {
        "ecosystem_id": "GLOBAL-COMMUNICATION-ECOSYSTEM",
        "name": "GLOBAL COMMUNICATION ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["EMAIL", "MESSAGING", "NOTIFICATIONS"],
    },
    {
        "ecosystem_id": "GLOBAL-DATA-DATABASE-ECOSYSTEM",
        "name": "GLOBAL DATA & DATABASE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["DATABASES", "DATA_EXCHANGE", "ANALYTICS"],
    },
    {
        "ecosystem_id": "GLOBAL-DEVELOPER-ECOSYSTEM",
        "name": "GLOBAL DEVELOPER ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["APIS", "SDKS", "REPOSITORIES", "CI_CD"],
    },

    # API hierarchy
    {
        "ecosystem_id": "GLOBAL-API-ECOSYSTEM",
        "name": "GLOBAL API ECOSYSTEM",
        "ecosystem_type": "PLATFORM",
        "capabilities": ["API_CATALOG", "API_ROUTING", "INTEGRATION"],
    },
    {
        "ecosystem_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
        "name": "GLOBAL BUSINESS API ECOSYSTEM",
        "ecosystem_type": "PLATFORM",
        "capabilities": ["BUSINESS_APIS", "BUSINESS_INTEGRATIONS"],
        "parent_id": "GLOBAL-API-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-NETWORK-MARKETING-API-ECOSYSTEM",
        "name": "GLOBAL NETWORK MARKETING API ECOSYSTEM",
        "ecosystem_type": "BUSINESS_API",
        "capabilities": [
            "DIRECT_SELLING",
            "NETWORK_MARKETING",
            "PARTNER_NETWORKS",
        ],
        "parent_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-AFFILIATE-MARKETING-API-ECOSYSTEM",
        "name": "GLOBAL AFFILIATE MARKETING API ECOSYSTEM",
        "ecosystem_type": "BUSINESS_API",
        "capabilities": ["AFFILIATE_TRACKING", "REFERRALS", "COMMISSIONS"],
        "parent_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-ECOMMERCE-API-ECOSYSTEM",
        "name": "GLOBAL E-COMMERCE API ECOSYSTEM",
        "ecosystem_type": "BUSINESS_API",
        "capabilities": ["PRODUCT_CATALOG", "ORDERS", "INVENTORY"],
        "parent_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-CRM-LEAD-GENERATION-API-ECOSYSTEM",
        "name": "GLOBAL CRM & LEAD GENERATION API ECOSYSTEM",
        "ecosystem_type": "BUSINESS_API",
        "capabilities": ["CRM", "LEAD_CAPTURE", "LEAD_MANAGEMENT"],
        "parent_id": "GLOBAL-BUSINESS-API-ECOSYSTEM",
    },

    # Language hierarchy
    {
        "ecosystem_id": "GLOBAL-LANGUAGE-ECOSYSTEM",
        "name": "GLOBAL LANGUAGE ECOSYSTEM",
        "ecosystem_type": "PLATFORM",
        "capabilities": [
            "LANGUAGE_PREFERENCES",
            "LOCALIZATION",
            "MULTILINGUAL_SUPPORT",
        ],
    },
    {
        "ecosystem_id": "GLOBAL-LANGUAGE-TRANSLATION-ECOSYSTEM",
        "name": "GLOBAL LANGUAGE TRANSLATION ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "TEXT_TRANSLATION",
            "MESSAGE_TRANSLATION",
            "CONTENT_TRANSLATION",
        ],
        "parent_id": "GLOBAL-LANGUAGE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-SPEECH-ECOSYSTEM",
        "name": "GLOBAL SPEECH ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["SPEECH_PROCESSING", "AUDIO_LANGUAGE_SUPPORT"],
        "parent_id": "GLOBAL-LANGUAGE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-SPEECH-TO-TEXT-ECOSYSTEM",
        "name": "GLOBAL SPEECH TO TEXT ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["TRANSCRIPTION", "SPEECH_RECOGNITION"],
        "parent_id": "GLOBAL-SPEECH-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-TEXT-TO-SPEECH-ECOSYSTEM",
        "name": "GLOBAL TEXT TO SPEECH ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["SPEECH_SYNTHESIS", "VOICE_OUTPUT"],
        "parent_id": "GLOBAL-SPEECH-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-SUBTITLE-ECOSYSTEM",
        "name": "GLOBAL SUBTITLE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": ["CAPTIONS", "SUBTITLE_TRANSLATION", "TIMED_TEXT"],
        "parent_id": "GLOBAL-LANGUAGE-ECOSYSTEM",
    },

    # Video hierarchy
    {
        "ecosystem_id": "GLOBAL-VIDEO-ECOSYSTEM",
        "name": "GLOBAL VIDEO ECOSYSTEM",
        "ecosystem_type": "PLATFORM",
        "capabilities": [
            "VIDEO_CATALOG",
            "VIDEO_PROCESSING",
            "VIDEO_PUBLISHING",
        ],
    },
    {
        "ecosystem_id": "GLOBAL-VIDEO-LANGUAGE-ECOSYSTEM",
        "name": "GLOBAL VIDEO LANGUAGE ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "VIDEO_TRANSCRIPTION",
            "DUBBING",
            "MULTILINGUAL_AUDIO",
        ],
        "parent_id": "GLOBAL-VIDEO-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-MEDIA-INGESTION-ECOSYSTEM",
        "name": "GLOBAL MEDIA INGESTION ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "AUTHORIZED_UPLOADS",
            "MEDIA_IMPORT",
            "FORMAT_VALIDATION",
        ],
        "parent_id": "GLOBAL-VIDEO-ECOSYSTEM",
    },
    {
        "ecosystem_id": "GLOBAL-VIDEO-ACCESSIBILITY-ECOSYSTEM",
        "name": "GLOBAL VIDEO ACCESSIBILITY ECOSYSTEM",
        "ecosystem_type": "FUNCTIONAL",
        "capabilities": [
            "CAPTIONS",
            "AUDIO_DESCRIPTION",
            "ACCESSIBILITY_PREFERENCES",
        ],
        "parent_id": "GLOBAL-VIDEO-ECOSYSTEM",
    },
)


# Existing personal registrations
PERSONAL_REGISTRATIONS: tuple[dict[str, Any], ...] = (
    {
        "ecosystem_id": "PERSONAL-RAJESHKHANDELWAL",
        "name": "RAJESHKHANDELWAL",
        "ecosystem_type": "PERSONAL",
        "repository_ref": "RAJESHKHANDELWALOFFICIAL/RAJESHKHANDELWAL",
        "capabilities": [
            "IDENTITY",
            "PROFILE",
            "WEBSITE",
            "DOMAIN",
            "PROJECTS",
        ],
        "parent_id": "GLOBAL-PEOPLE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "PERSONAL-RAJESHKHANDELWALOFFICIAL",
        "name": "RAJESHKHANDELWALOFFICIAL",
        "ecosystem_type": "PERSONAL",
        "repository_ref": "RAJESHKHANDELWALOFFICIAL/MAIN-BASE-FOUNDATION",
        "capabilities": [
            "IDENTITY",
            "PROFILE",
            "BUSINESS",
            "WEBSITE",
            "DOMAIN",
            "PROJECTS",
        ],
        "parent_id": "GLOBAL-PEOPLE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "PERSONAL-DRRAJESHKANDELWALIBC",
        "name": "DRRAJESHKANDELWALIBC",
        "ecosystem_type": "PERSONAL_BRAND",
        "capabilities": [
            "IDENTITY",
            "BRAND",
            "BUSINESS",
            "WEBSITE",
            "DOMAIN",
        ],
        "parent_id": "GLOBAL-PEOPLE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "PERSONAL-DRRAJESHKANDELWALIBCOFFICIAL",
        "name": "DRRAJESHKANDELWALIBCOFFICIAL",
        "ecosystem_type": "PERSONAL_BRAND",
        "capabilities": [
            "IDENTITY",
            "BRAND",
            "BUSINESS",
            "WEBSITE",
            "DOMAIN",
        ],
        "parent_id": "GLOBAL-PEOPLE-ECOSYSTEM",
    },
)


# Existing company and company-group registrations
_COMPANY_CAPABILITIES = [
    "ORGANIZATION",
    "BUSINESS",
    "TEAM",
    "PROJECTS",
    "WEBSITE",
    "DOMAIN",
]

COMPANY_REGISTRATIONS: tuple[dict[str, Any], ...] = (
    {
        "ecosystem_id": "COMPANY-KHANDELWALGROUPANDCOMPANY",
        "name": "KHANDELWALGROUPANDCOMPANY",
        "ecosystem_type": "COMPANY",
        "capabilities": _COMPANY_CAPABILITIES,
        "parent_id": "GLOBAL-BUSINESS-ECOSYSTEM",
    },
    {
        "ecosystem_id": "COMPANY-KHANDELWALGROUPANDCOMPANYOFFICIAL",
        "name": "KHANDELWALGROUPANDCOMPANYOFFICIAL",
        "ecosystem_type": "COMPANY",
        "capabilities": _COMPANY_CAPABILITIES,
        "parent_id": "GLOBAL-BUSINESS-ECOSYSTEM",
    },
    {
        "ecosystem_id": "COMPANY-KHANDELWALGROUPANDCOMPANIES",
        "name": "KHANDELWALGROUPANDCOMPANIES",
        "ecosystem_type": "COMPANY_GROUP",
        "capabilities": _COMPANY_CAPABILITIES,
        "parent_id": "GLOBAL-BUSINESS-ECOSYSTEM",
    },
    {
        "ecosystem_id": "COMPANY-KHANDELWALGROUPANDCOMPANIESOFFICIAL",
        "name": "KHANDELWALGROUPANDCOMPANIESOFFICIAL",
        "ecosystem_type": "COMPANY_GROUP",
        "capabilities": _COMPANY_CAPABILITIES,
        "parent_id": "GLOBAL-BUSINESS-ECOSYSTEM",
    },
)


def _normalize_record(record: dict[str, Any]) -> dict[str, Any]:
    """Return a complete, independent record with safe defaults."""
    normalized = deepcopy(record)
    normalized.setdefault("repository_ref", None)
    normalized.setdefault("status", "REGISTERED")
    normalized.setdefault("enabled", True)
    normalized.setdefault("capabilities", [])
    normalized.setdefault("parent_id", ROOT_ID)
    normalized.setdefault("metadata", {})
    return normalized


def get_catalog() -> list[dict[str, Any]]:
    """Return the root, all 34 categories, and all 8 registrations."""
    records = [
        ROOT,
        *CATEGORIES,
        *PERSONAL_REGISTRATIONS,
        *COMPANY_REGISTRATIONS,
    ]
    return [_normalize_record(record) for record in records]


def get_category_catalog() -> list[dict[str, Any]]:
    """Return independent copies of all 34 ecosystem categories."""
    return [_normalize_record(record) for record in CATEGORIES]


def get_registration_catalog() -> list[dict[str, Any]]:
    """Return independent copies of the 8 existing registrations."""
    records = [
        *PERSONAL_REGISTRATIONS,
        *COMPANY_REGISTRATIONS,
    ]
    return [_normalize_record(record) for record in records]
