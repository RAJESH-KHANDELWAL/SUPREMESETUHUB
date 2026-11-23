"""Google-wide Core domain inventory built from the repository's provider catalog.

This is a Core taxonomy and governance view. It does not imply that every
Google product has a public API, an available entitlement, or a live adapter.
"""
from __future__ import annotations

from collections import Counter
from typing import Any

from backend.global_ecosystem.google_ecosystem.runtime.service import GoogleEcosystemService

DOMAIN_DEFINITIONS: dict[str, dict[str, Any]] = {
    "PROVIDER_GOVERNANCE": {"name": "Provider Governance", "purpose": "Google provider identity, product registration, lifecycle, policy and readiness."},
    "IDENTITY_ACCESS_AND_ADMIN": {"name": "Identity, Access and Administration", "purpose": "Accounts, OAuth identity boundaries, IAM, Workspace administration, devices and compliance."},
    "WORKSPACE_AND_COLLABORATION": {"name": "Workspace and Collaboration", "purpose": "Gmail, Calendar, Chat, Meet, Drive, Docs, Sheets, Slides, Forms and collaboration."},
    "CLOUD_INFRASTRUCTURE_AND_NETWORK": {"name": "Cloud Infrastructure and Networking", "purpose": "Google Cloud projects, compute, containers, serverless, networking, DNS and hosting."},
    "STORAGE_DATABASE_AND_DATA": {"name": "Storage, Databases and Data Platforms", "purpose": "Cloud Storage, databases, data processing, warehouses, migration and content metadata boundaries."},
    "AI_ML_AND_INTELLIGENCE": {"name": "AI, Machine Learning and Intelligence", "purpose": "Gemini, Vertex AI, conversational AI, search/RAG, vision, language and recommendations."},
    "ANALYTICS_AND_OBSERVABILITY": {"name": "Analytics and Observability", "purpose": "Analytics, tagging, business intelligence, monitoring, logging and performance insights."},
    "MAPS_GEOSPATIAL_AND_TRAVEL": {"name": "Maps, Geospatial and Travel", "purpose": "Maps Platform, Places, Routes, geocoding, Earth, imagery, travel discovery and location services."},
    "DEVELOPER_AND_APPLICATION_PLATFORM": {"name": "Developer and Application Platform", "purpose": "Firebase, APIs, SDKs, build pipelines, AppSheet, Apps Script, developer resources and app delivery."},
    "ANDROID_AND_MOBILE": {"name": "Android and Mobile", "purpose": "Android platform, Play services, app integrity, mobile distribution, gaming and device management."},
    "SECURITY_PRIVACY_AND_COMPLIANCE": {"name": "Security, Privacy and Compliance", "purpose": "Identity security, abuse prevention, safe browsing, reCAPTCHA, secrets, keys and e-discovery."},
    "ADVERTISING_COMMERCE_AND_MONETIZATION": {"name": "Advertising, Commerce and Monetization", "purpose": "Google Ads, Ad Manager, AdSense, AdMob, Merchant Center, Shopping and commerce feeds."},
    "SEARCH_PUBLISHING_AND_DISCOVERY": {"name": "Search, Publishing and Discovery", "purpose": "Search, Search Console, Blogger, Books, News, Arts and Culture and web discovery."},
    "MEDIA_VIDEO_AND_AUDIO": {"name": "Media, Video and Audio", "purpose": "YouTube, Photos, media, video analytics, speech, audio and media experiences."},
    "BUSINESS_EDUCATION_AND_LOCAL": {"name": "Business, Education and Local Services", "purpose": "Business Profile, Classroom, assignments, Workspace education and local business presence."},
    "PAYMENTS_WALLET_AND_SUBSCRIPTIONS": {"name": "Payments, Wallet and Subscriptions", "purpose": "Google Pay, Wallet, subscriptions and account-plan boundaries."},
    "CONSUMER_DEVICES_AND_SMART_HOME": {"name": "Consumer Devices and Smart Home", "purpose": "Pixel, Nest, Google Store and smart-home product families."},
    "LANGUAGE_ACCESSIBILITY_AND_PRODUCTIVITY": {"name": "Language, Accessibility and Productivity", "purpose": "Translation, language tools, productivity utilities, notes and task management."},
    "SPECIALTY_AND_CROSS_PRODUCT": {"name": "Specialty and Cross-product Services", "purpose": "Google offerings whose category spans multiple product families or needs manual classification."},
}

_CATEGORY_GROUPS = {
    "IDENTITY_ACCESS_AND_ADMIN": {
        "ADMINISTRATION", "COMPLIANCE_AND_E_DISCOVERY", "DEVICE_MANAGEMENT",
        "IDENTITY_AND_ACCESS_MANAGEMENT", "IDENTITY_AND_AUTHENTICATION",
        "IDENTITY_AND_DEVICE_MANAGEMENT", "IDENTITY_AND_SIGN_IN",
        "MULTI_FACTOR_AUTHENTICATION", "FAMILY_AND_DEVICE_CONTROLS",
    },
    "WORKSPACE_AND_COLLABORATION": {
        "COLLABORATION", "COMMUNICATION", "CONTACTS", "FORMS_AND_SURVEYS",
        "NOTES", "PRODUCTIVITY", "SCHEDULING", "TASK_MANAGEMENT",
        "VIDEO_MEETINGS", "WORKSPACE_EXTENSIONS",
    },
    "CLOUD_INFRASTRUCTURE_AND_NETWORK": {
        "APPLICATION_HOSTING", "CLOUD_INFRASTRUCTURE", "COMPUTE", "CONTAINERS",
        "CONTENT_DELIVERY", "DNS_AND_NETWORKING", "NETWORKING",
        "SERVERLESS_COMPUTE", "WEB_HOSTING", "APPLICATION_HOSTING",
    },
    "STORAGE_DATABASE_AND_DATA": {
        "ARTIFACT_STORAGE", "CLOUD_STORAGE", "DATABASE", "DATA_PROCESSING",
        "DATA_WAREHOUSE", "MANAGED_DATABASES", "MIGRATION", "STORAGE",
    },
    "AI_ML_AND_INTELLIGENCE": {
        "CONVERSATIONAL_AI", "ENTERPRISE_SEARCH_AND_RAG", "GENERATIVE_AI",
        "GENERATIVE_AI_AND_ML", "GENERATIVE_AI_DEVELOPER_TOOLS", "IMAGE_ANALYSIS",
        "LANGUAGE_AI", "NOTEBOOKS_AND_ML", "PERSONALIZATION", "VIDEO_ANALYSIS",
    },
    "ANALYTICS_AND_OBSERVABILITY": {
        "ANALYTICS", "ANALYTICS_AND_TAGGING", "BUSINESS_INTELLIGENCE",
        "OBSERVABILITY", "VIDEO_ANALYTICS",
    },
    "MAPS_GEOSPATIAL_AND_TRAVEL": {
        "MAPS_AND_GEOSPATIAL", "MAPS_AND_IMAGERY", "MAPS_AND_LOCATION",
        "MAPS_AND_ROUTES", "TRAVEL", "TRAVEL_SEARCH",
    },
    "DEVELOPER_AND_APPLICATION_PLATFORM": {
        "APP_CONFIGURATION", "APP_DEVELOPMENT_AND_BACKEND", "APP_DISTRIBUTION",
        "APP_DISTRIBUTION_AND_REPORTING", "APP_PERFORMANCE",
        "APP_QUALITY_AND_CRASH_REPORTING", "APP_TESTING_AND_DISTRIBUTION",
        "AUTOMATION_AND_DEVELOPER_TOOLS", "CI_CD", "DEVELOPER_RESOURCES",
        "NO_CODE_APPLICATIONS", "PUSH_NOTIFICATIONS", "WEB_DEVELOPMENT",
        "WORKFLOW_ORCHESTRATION",
    },
    "ANDROID_AND_MOBILE": {
        "ANDROID_APP_SECURITY", "ANDROID_ENTERPRISE", "ANDROID_PLATFORM",
        "APP_ABUSE_PREVENTION", "GAMING",
    },
    "SECURITY_PRIVACY_AND_COMPLIANCE": {
        "IDENTITY_AND_ACCESS_MANAGEMENT", "KEY_MANAGEMENT", "NETWORK_SECURITY",
        "SECRETS_MANAGEMENT", "SECURITY", "SECURITY_AND_ABUSE_PREVENTION",
    },
    "ADVERTISING_COMMERCE_AND_MONETIZATION": {
        "ADVERTISING", "COMMERCE_AND_PRODUCT_FEEDS", "COMMERCE_DISCOVERY",
        "MOBILE_ADVERTISING", "PUBLISHER_MONETIZATION",
    },
    "SEARCH_PUBLISHING_AND_DISCOVERY": {
        "ARTS_AND_CULTURE", "BOOKS_AND_DISCOVERY", "BOOKS_AND_MEDIA", "NEWS",
        "PUBLISHING_AND_BLOGGING", "SEARCH", "SEO_AND_SEARCH_PERFORMANCE",
        "WEBSITE_BUILDER",
    },
    "MEDIA_VIDEO_AND_AUDIO": {
        "AUDIO_AND_MEDIA", "AUDIO_AND_SPEECH", "MEDIA", "VIDEO_AND_CHANNEL",
    },
    "BUSINESS_EDUCATION_AND_LOCAL": {
        "EDUCATION", "LOCAL_BUSINESS_PRESENCE",
    },
    "PAYMENTS_WALLET_AND_SUBSCRIPTIONS": {
        "DIGITAL_WALLET", "PAYMENTS", "SUBSCRIPTION_AND_STORAGE_PLAN",
    },
    "CONSUMER_DEVICES_AND_SMART_HOME": {
        "HARDWARE", "HARDWARE_COMMERCE", "SMART_HOME",
    },
    "LANGUAGE_ACCESSIBILITY_AND_PRODUCTIVITY": {
        "LANGUAGE_AND_TRANSLATION",
    },
}

CATEGORY_TO_DOMAIN: dict[str, str] = {}
for _domain_id, _categories in _CATEGORY_GROUPS.items():
    for _category in _categories:
        # Identity/security categories are intentionally assigned to the
        # security domain where they describe controls, not user directory data.
        if _category in {"IDENTITY_AND_ACCESS_MANAGEMENT", "APP_ABUSE_PREVENTION"}:
            CATEGORY_TO_DOMAIN[_category] = "SECURITY_PRIVACY_AND_COMPLIANCE"
        else:
            CATEGORY_TO_DOMAIN.setdefault(_category, _domain_id)


def list_google_domain_inventory() -> list[dict[str, Any]]:
    """Return every existing runtime offering with a Core domain assignment."""
    products = GoogleEcosystemService().catalog()
    inventory = []
    for product in products:
        category = str(product.get("category", ""))
        domain_id = CATEGORY_TO_DOMAIN.get(category, "SPECIALTY_AND_CROSS_PRODUCT")
        domain = DOMAIN_DEFINITIONS[domain_id]
        inventory.append({
            **product,
            "core_domain_id": domain_id,
            "core_domain_name": domain["name"],
            "domain_assignment": (
                "CATEGORY_RULE" if category in CATEGORY_TO_DOMAIN
                else "SPECIALTY_REVIEW_REQUIRED"
            ),
        })
    return inventory


def google_domain_summary() -> dict[str, Any]:
    """Return coverage counts and category gaps without claiming live support."""
    inventory = list_google_domain_inventory()
    counts = Counter(item["core_domain_id"] for item in inventory)
    categories = sorted({str(item.get("category", "")) for item in inventory})
    unmapped = sorted(category for category in categories if category not in CATEGORY_TO_DOMAIN)
    return {
        "success": True,
        "domain_count": len(DOMAIN_DEFINITIONS),
        "offering_count": len(inventory),
        "assigned_offering_count": len(inventory),
        "category_rule_count": len(CATEGORY_TO_DOMAIN),
        "specialty_review_categories": unmapped,
        "domains": [
            {
                "domain_id": domain_id,
                **definition,
                "offering_count": counts.get(domain_id, 0),
            }
            for domain_id, definition in DOMAIN_DEFINITIONS.items()
        ],
        "live_connections_verified": 0,
        "note": "Domain assignment is Core classification only; it is not API availability, entitlement, authorization or live connectivity.",
    }
