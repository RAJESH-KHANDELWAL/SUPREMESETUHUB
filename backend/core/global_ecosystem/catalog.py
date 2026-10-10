```python
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


# Existing 18 ecosystem categories.
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
        "capabilities": ["CREATOR_TOOLS", "MEDIA", "PUBLISHING", "MONETIZATION"],
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
)


# Existing personal registrations.
PERSONAL_REGISTRATIONS: tuple[dict[str, Any], ...] = (
    {
        "ecosystem_id": "PERSONAL-RAJESHKHANDELWAL",
        "name": "RAJESHKHANDELWAL",
        "ecosystem_type": "PERSONAL",
        "repository_ref": "RAJESHKHANDELWALOFFICIAL/RAJESHKHANDELWAL",
        "capabilities": ["IDENTITY", "PROFILE", "WEBSITE", "DOMAIN", "PROJECTS"],
        "parent_id": "GLOBAL-PEOPLE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "PERSONAL-RAJESHKHANDELWALOFFICIAL",
        "name": "RAJESHKHANDELWALOFFICIAL",
        "ecosystem_type": "PERSONAL",
        "repository_ref": "RAJESHKHANDELWALOFFICIAL/MAIN-BASE-FOUNDATION",
        "capabilities": [
            "IDENTITY", "PROFILE", "BUSINESS",
            "WEBSITE", "DOMAIN", "PROJECTS",
        ],
        "parent_id": "GLOBAL-PEOPLE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "PERSONAL-DRRAJESHKANDELWALIBC",
        "name": "DRRAJESHKANDELWALIBC",
        "ecosystem_type": "PERSONAL_BRAND",
        "capabilities": ["IDENTITY", "BRAND", "BUSINESS", "WEBSITE", "DOMAIN"],
        "parent_id": "GLOBAL-PEOPLE-ECOSYSTEM",
    },
    {
        "ecosystem_id": "PERSONAL-DRRAJESHKANDELWALIBCOFFICIAL",
        "name": "DRRAJESHKANDELWALIBCOFFICIAL",
        "ecosystem_type": "PERSONAL_BRAND",
        "capabilities": ["IDENTITY", "BRAND", "BUSINESS", "WEBSITE", "DOMAIN"],
        "parent_id": "GLOBAL-PEOPLE-ECOSYSTEM",
    },
)


# Existing company and company-group registrations.
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
    """Return the root, all 18 categories, and all 8 registrations."""
    records = [
        ROOT,
        *CATEGORIES,
        *PERSONAL_REGISTRATIONS,
        *COMPANY_REGISTRATIONS,
    ]
    return [_normalize_record(record) for record in records]


def get_category_catalog() -> list[dict[str, Any]]:
    """Return independent copies of the 18 existing categories."""
    return [_normalize_record(record) for record in CATEGORIES]


def get_registration_catalog() -> list[dict[str, Any]]:
    """Return independent copies of the 8 existing registrations."""
    records = [*PERSONAL_REGISTRATIONS, *COMPANY_REGISTRATIONS]
    return [_normalize_record(record) for record in records]
```
