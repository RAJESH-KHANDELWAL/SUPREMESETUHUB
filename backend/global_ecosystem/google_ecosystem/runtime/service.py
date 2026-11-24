"""Central registry for Google products and integration boundaries.

Catalog entries are metadata only: they do not imply credentials, consent, or live
connectivity. Product availability and APIs can change; verify official docs before
enabling a provider adapter.
"""
from __future__ import annotations

import os
from typing import Any


def _product(name: str, category: str, api: str | None = None,
             integration_mode: str = "USER_OAUTH",
             availability: str = "API_AVAILABLE",
             auth: str = "Google OAuth 2.0",
             scopes: list[str] | None = None,
             notes: str | None = None) -> dict[str, Any]:
    item: dict[str, Any] = {
        "name": name,
        "category": category,
        "api": api,
        "auth": auth,
        "scopes": scopes or [],
        "integration_mode": integration_mode,
        "availability": availability,
    }
    if notes:
        item["notes"] = notes
    return item


GOOGLE_PRODUCTS: dict[str, dict[str, Any]] = {
    # Communication and collaboration
    "gmail": _product("Gmail", "COMMUNICATION", "Gmail API", scopes=["https://www.googleapis.com/auth/gmail.readonly"]),
    "google_chat": _product("Google Chat", "COMMUNICATION", "Google Chat API"),
    "meet": _product("Google Meet", "VIDEO_MEETINGS", "Google Meet REST API", availability="API_AVAILABLE_WITH_ELIGIBILITY_AND_SCOPES"),
    "calendar": _product("Google Calendar", "SCHEDULING", "Google Calendar API", scopes=["https://www.googleapis.com/auth/calendar.events"]),
    "contacts": _product("Google Contacts", "CONTACTS", "People API", scopes=["https://www.googleapis.com/auth/contacts.readonly"]),
    "google_voice": _product("Google Voice", "COMMUNICATION", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_CONSUMER_API"),
    "google_groups": _product("Google Groups", "COLLABORATION", "Admin SDK Directory API", availability="WORKSPACE_ADMIN_ELIGIBILITY_REQUIRED"),
    # Productivity and workspace
    "drive": _product("Google Drive", "STORAGE", "Google Drive API", scopes=["https://www.googleapis.com/auth/drive.file"]),
    "docs": _product("Google Docs", "PRODUCTIVITY", "Google Docs API", scopes=["https://www.googleapis.com/auth/documents"]),
    "sheets": _product("Google Sheets", "PRODUCTIVITY", "Google Sheets API", scopes=["https://www.googleapis.com/auth/spreadsheets"]),
    "google_slides": _product("Google Slides", "PRODUCTIVITY", "Google Slides API"),
    "google_forms": _product("Google Forms", "FORMS_AND_SURVEYS", "Google Forms API"),
    "google_sites": _product("Google Sites", "WEBSITE_BUILDER", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_CONTENT_MANAGEMENT_API"),
    "google_keep": _product("Google Keep", "NOTES", "Google Keep API", availability="WORKSPACE_ELIGIBILITY_REQUIRED"),
    "tasks": _product("Google Tasks", "TASK_MANAGEMENT", "Google Tasks API", scopes=["https://www.googleapis.com/auth/tasks.readonly"]),
    "google_jamboard": _product("Google Jamboard", "COLLABORATION", None, "PRODUCT_INFORMATION_ONLY", "DISCONTINUED"),
    "google_workspace_admin": _product("Google Workspace Admin", "ADMINISTRATION", "Admin SDK APIs", availability="WORKSPACE_ADMIN_ELIGIBILITY_REQUIRED"),
    "google_one": _product("Google One", "SUBSCRIPTION_AND_STORAGE_PLAN", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_GOOGLE_ONE_API", auth="Google account / plan management", notes="Membership and consumer plan controls are not exposed as a general public API for this backend."),
    # Cloud, developer, AI and data
    "cloud": _product("Google Cloud", "CLOUD_INFRASTRUCTURE", "Google Cloud APIs", "CLOUD_PROJECT_CREDENTIALS", auth="Workload Identity Federation or least-privilege service account", notes="Use a separate Cloud identity; do not reuse consumer Gmail OAuth as Cloud administrator credentials."),
    "firebase": _product("Firebase", "APP_DEVELOPMENT_AND_BACKEND", "Firebase APIs", "CLOUD_PROJECT_CREDENTIALS", auth="Firebase Authentication / Google Cloud IAM"),
    "maps": _product("Google Maps Platform", "MAPS_AND_LOCATION", "Maps Platform APIs", "API_KEY_OR_OAUTH", "API_AVAILABLE_WITH_BILLING_AND_RESTRICTIONS", auth="Restricted API key or supported OAuth flow"),
    "google_places": _product("Google Places", "MAPS_AND_LOCATION", "Places API", "API_KEY_OR_OAUTH", "API_AVAILABLE_WITH_BILLING_AND_RESTRICTIONS"),
    "google_routes": _product("Google Routes", "MAPS_AND_LOCATION", "Routes API", "API_KEY_OR_OAUTH", "API_AVAILABLE_WITH_BILLING_AND_RESTRICTIONS"),
    "google_geocoding": _product("Google Geocoding", "MAPS_AND_LOCATION", "Geocoding API", "API_KEY_OR_OAUTH", "API_AVAILABLE_WITH_BILLING_AND_RESTRICTIONS"),
    "google_earth": _product("Google Earth", "MAPS_AND_GEOSPATIAL", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_PRODUCT_CONTROL_API"),
    "google_search": _product("Google Search", "SEARCH", "Programmable Search Engine API", "API_KEY", "LIMITED_API_AND_CONFIGURATION"),
    "google_search_console": _product("Google Search Console", "SEO_AND_SEARCH_PERFORMANCE", "Search Console API"),
    "analytics": _product("Google Analytics", "ANALYTICS", "Google Analytics Data API", "USER_OAUTH_OR_CLOUD_IDENTITY", auth="OAuth 2.0 or service account where supported", scopes=["https://www.googleapis.com/auth/analytics.readonly"]),
    "google_tag_manager": _product("Google Tag Manager", "ANALYTICS_AND_TAGGING", "Tag Manager API"),
    "google_ads": _product("Google Ads", "ADVERTISING", "Google Ads API", availability="DEVELOPER_TOKEN_AND_ACCOUNT_ELIGIBILITY_REQUIRED"),
    "google_ad_manager": _product("Google Ad Manager", "ADVERTISING", "Google Ad Manager API", availability="ACCOUNT_ELIGIBILITY_REQUIRED"),
    "google_play_console": _product("Google Play Console", "APP_DISTRIBUTION", "Google Play Developer APIs", availability="DEVELOPER_ACCOUNT_AND_API_ACCESS_REQUIRED"),
    "google_play_services": _product("Google Play services", "ANDROID_PLATFORM", None, "SDK_INTEGRATION", "ANDROID_APP_SDK"),
    "google_gemini": _product("Gemini", "GENERATIVE_AI", "Gemini API", "API_KEY_OR_CLOUD_IDENTITY", availability="API_AVAILABLE_WITH_PROJECT_AND_POLICY_REQUIREMENTS"),
    "vertex_ai": _product("Vertex AI", "GENERATIVE_AI_AND_ML", "Vertex AI API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_ai_studio": _product("Google AI Studio", "GENERATIVE_AI_DEVELOPER_TOOLS", "Gemini API", "API_KEY_OR_CLOUD_IDENTITY"),
    "google_colab": _product("Google Colab", "NOTEBOOKS_AND_ML", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_SESSION_CONTROL_API"),
    "bigquery": _product("BigQuery", "DATA_WAREHOUSE", "BigQuery API", "CLOUD_PROJECT_CREDENTIALS"),
    "look_studio": _product("Looker Studio", "BUSINESS_INTELLIGENCE", None, "PRODUCT_INFORMATION_ONLY", "LIMITED_PUBLIC_API"),
    "looker": _product("Looker", "BUSINESS_INTELLIGENCE", "Looker API", availability="LICENSE_AND_INSTANCE_REQUIRED"),
    "google_cloud_storage": _product("Cloud Storage", "CLOUD_STORAGE", "Cloud Storage JSON API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_cloud_dns": _product("Cloud DNS", "DNS_AND_NETWORKING", "Cloud DNS API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_compute_engine": _product("Compute Engine", "COMPUTE", "Compute Engine API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_kubernetes_engine": _product("Google Kubernetes Engine", "CONTAINERS", "Google Kubernetes Engine API", "CLOUD_PROJECT_CREDENTIALS"),
    "cloud_run": _product("Cloud Run", "SERVERLESS_COMPUTE", "Cloud Run API", "CLOUD_PROJECT_CREDENTIALS"),
    "cloud_functions": _product("Cloud Functions", "SERVERLESS_COMPUTE", "Cloud Functions API", "CLOUD_PROJECT_CREDENTIALS"),
    "cloud_sql": _product("Cloud SQL", "MANAGED_DATABASES", "Cloud SQL Admin API", "CLOUD_PROJECT_CREDENTIALS"),
    "pub_sub": _product("Pub/Sub", "MESSAGING_AND_EVENTS", "Pub/Sub API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_workspace_marketplace": _product("Google Workspace Marketplace", "WORKSPACE_EXTENSIONS", "Google Workspace Marketplace APIs", availability="PUBLISHER_AND_APP_ELIGIBILITY_REQUIRED"),
    # Media and consumer services
    "youtube": _product("YouTube", "VIDEO_AND_CHANNEL", "YouTube Data API", auth="OAuth 2.0 or API key depending on operation", scopes=["https://www.googleapis.com/auth/youtube.readonly"]),
    "youtube_analytics": _product("YouTube Analytics", "VIDEO_ANALYTICS", "YouTube Analytics API", scopes=["https://www.googleapis.com/auth/yt-analytics.readonly"]),
    "photos": _product("Google Photos", "MEDIA", "Google Photos APIs", availability="LIMITED_API_AND_SCOPE_AVAILABILITY", notes="Current Photos API policies restrict supported use cases; validate the exact use case before enabling."),
    "google_play_books": _product("Google Play Books", "BOOKS_AND_MEDIA", "Google Books API", availability="API_AVAILABLE_WITH_PRODUCT_SPECIFIC_LIMITS"),
    "google_news": _product("Google News", "NEWS", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_NEWS_READER_API"),
    "google_shopping": _product("Google Shopping", "COMMERCE_DISCOVERY", "Content API for Shopping / Merchant API", availability="MERCHANT_ACCOUNT_AND_API_ELIGIBILITY_REQUIRED"),
    "google_business_profile": _product("Google Business Profile", "LOCAL_BUSINESS_PRESENCE", "Business Profile APIs", availability="PROJECT_APPROVAL_AND_ACCOUNT_ELIGIBILITY_REQUIRED"),
    "google_translate": _product("Google Cloud Translation", "LANGUAGE_AND_TRANSLATION", "Cloud Translation API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_speech": _product("Google Cloud Speech-to-Text", "AUDIO_AND_SPEECH", "Cloud Speech-to-Text API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_text_to_speech": _product("Google Cloud Text-to-Speech", "AUDIO_AND_SPEECH", "Cloud Text-to-Speech API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_vision": _product("Google Cloud Vision", "IMAGE_ANALYSIS", "Cloud Vision API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_document_ai": _product("Google Cloud Document AI", "DOCUMENT_PROCESSING", "Document AI API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_recaptcha": _product("Google reCAPTCHA", "SECURITY_AND_ABUSE_PREVENTION", "reCAPTCHA APIs", "API_KEY_OR_CLOUD_IDENTITY"),
    "google_safe_browsing": _product("Google Safe Browsing", "SECURITY", "Safe Browsing API", "API_KEY"),
    "google_identity": _product("Google Identity Services", "IDENTITY_AND_SIGN_IN", "Google Identity Services", "OAUTH_OR_IDENTITY_SDK"),
    "google_authenticator": _product("Google Authenticator", "MULTI_FACTOR_AUTHENTICATION", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_DEVICE_MANAGEMENT_API"),
    "google_wallet": _product("Google Wallet", "DIGITAL_WALLET", "Google Wallet API", availability="ISSUER_AND_INTEGRATION_ELIGIBILITY_REQUIRED"),
    "google_pay": _product("Google Pay", "PAYMENTS", "Google Pay APIs", availability="MERCHANT_AND_REGION_ELIGIBILITY_REQUIRED"),
    "google_flights": _product("Google Flights", "TRAVEL_SEARCH", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_FLIGHTS_SEARCH_API"),
    "google_travel": _product("Google Travel", "TRAVEL", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_TRAVEL_CONTROL_API"),
    # Additional Workspace, education, developer, and publishing services
    "google_classroom": _product("Google Classroom", "EDUCATION", "Google Classroom API", availability="EDUCATION_ACCOUNT_AND_SCOPE_REQUIREMENTS"),
    "google_assignments": _product("Google Assignments", "EDUCATION", "Google Classroom API", availability="EDUCATION_PARTNER_ELIGIBILITY_REQUIRED"),
    "google_appsheet": _product("AppSheet", "NO_CODE_APPLICATIONS", "AppSheet API", availability="PLAN_AND_ACCOUNT_ELIGIBILITY_REQUIRED"),
    "google_apps_script": _product("Google Apps Script", "AUTOMATION_AND_DEVELOPER_TOOLS", "Apps Script API"),
    "google_blogger": _product("Blogger", "PUBLISHING_AND_BLOGGING", "Blogger API v3"),
    "google_books": _product("Google Books", "BOOKS_AND_DISCOVERY", "Books API"),
    "google_fonts": _product("Google Fonts", "WEB_DEVELOPMENT", "Google Fonts Developer API"),
    "google_developers": _product("Google Developers", "DEVELOPER_RESOURCES", None, "PRODUCT_INFORMATION_ONLY", "DOCUMENTATION_AND_PORTAL"),
    "google_play_console_reporting": _product("Google Play Console Reporting", "APP_DISTRIBUTION_AND_REPORTING", "Google Play Developer Reporting API", availability="DEVELOPER_ACCOUNT_AND_API_ACCESS_REQUIRED"),
    "google_android_management": _product("Android Management API", "ANDROID_ENTERPRISE", "Android Management API", availability="ENTERPRISE_AND_POLICY_REQUIREMENTS"),
    "google_play_integrity": _product("Play Integrity", "ANDROID_APP_SECURITY", "Play Integrity API", availability="APP_AND_PROJECT_CONFIGURATION_REQUIRED"),
    "google_cloud_identity": _product("Cloud Identity", "IDENTITY_AND_DEVICE_MANAGEMENT", "Cloud Identity API", "CLOUD_PROJECT_CREDENTIALS", availability="ORGANIZATION_ADMIN_ELIGIBILITY_REQUIRED"),
    "google_vault": _product("Google Vault", "COMPLIANCE_AND_E_DISCOVERY", "Google Vault API", availability="WORKSPACE_EDITION_AND_ADMIN_ELIGIBILITY_REQUIRED"),
    "google_endpoint_management": _product("Google Endpoint Management", "DEVICE_MANAGEMENT", "Google Workspace Admin SDK", availability="WORKSPACE_ADMIN_ELIGIBILITY_REQUIRED"),
    "google_workspace_migrate": _product("Google Workspace Migrate", "MIGRATION", None, "PRODUCT_INFORMATION_ONLY", "MIGRATION_TOOL_AND_ELIGIBILITY"),
    # Firebase products
    "firebase_authentication": _product("Firebase Authentication", "IDENTITY_AND_AUTHENTICATION", "Firebase Authentication APIs", "CLOUD_PROJECT_CREDENTIALS"),
    "cloud_firestore": _product("Cloud Firestore", "DATABASE", "Cloud Firestore API", "CLOUD_PROJECT_CREDENTIALS"),
    "firebase_realtime_database": _product("Firebase Realtime Database", "DATABASE", "Firebase Realtime Database API", "CLOUD_PROJECT_CREDENTIALS"),
    "firebase_hosting": _product("Firebase Hosting", "WEB_HOSTING", "Firebase Hosting API", "CLOUD_PROJECT_CREDENTIALS"),
    "firebase_app_distribution": _product("Firebase App Distribution", "APP_TESTING_AND_DISTRIBUTION", "Firebase App Distribution API", "CLOUD_PROJECT_CREDENTIALS"),
    "firebase_crashlytics": _product("Firebase Crashlytics", "APP_QUALITY_AND_CRASH_REPORTING", "Firebase APIs", "CLOUD_PROJECT_CREDENTIALS", "API_AVAILABLE_WITH_PRODUCT_SPECIFIC_LIMITS"),
    "firebase_remote_config": _product("Firebase Remote Config", "APP_CONFIGURATION", "Remote Config REST API", "CLOUD_PROJECT_CREDENTIALS"),
    "firebase_performance": _product("Firebase Performance Monitoring", "APP_PERFORMANCE", "Firebase APIs", "CLOUD_PROJECT_CREDENTIALS", "API_AVAILABLE_WITH_PRODUCT_SPECIFIC_LIMITS"),
    "firebase_cloud_messaging": _product("Firebase Cloud Messaging", "PUSH_NOTIFICATIONS", "FCM HTTP v1 API", "CLOUD_PROJECT_CREDENTIALS"),
    "firebase_app_check": _product("Firebase App Check", "APP_ABUSE_PREVENTION", "Firebase App Check APIs", "CLOUD_PROJECT_CREDENTIALS"),
    # Google Cloud infrastructure, operations, security, and data
    "google_cloud_iam": _product("Cloud IAM", "IDENTITY_AND_ACCESS_MANAGEMENT", "Cloud IAM API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_secret_manager": _product("Secret Manager", "SECRETS_MANAGEMENT", "Secret Manager API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_cloud_kms": _product("Cloud Key Management Service", "KEY_MANAGEMENT", "Cloud KMS API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_cloud_logging": _product("Cloud Logging", "OBSERVABILITY", "Cloud Logging API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_cloud_monitoring": _product("Cloud Monitoring", "OBSERVABILITY", "Cloud Monitoring API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_cloud_build": _product("Cloud Build", "CI_CD", "Cloud Build API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_artifact_registry": _product("Artifact Registry", "ARTIFACT_STORAGE", "Artifact Registry API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_cloud_armor": _product("Cloud Armor", "NETWORK_SECURITY", "Cloud Armor API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_cloud_cdn": _product("Cloud CDN", "CONTENT_DELIVERY", "Compute Engine API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_cloud_load_balancing": _product("Cloud Load Balancing", "NETWORKING", "Compute Engine API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_cloud_vpc": _product("Virtual Private Cloud", "NETWORKING", "Compute Engine API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_dataflow": _product("Dataflow", "DATA_PROCESSING", "Dataflow API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_dataproc": _product("Dataproc", "DATA_PROCESSING", "Dataproc API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_cloud_composer": _product("Cloud Composer", "WORKFLOW_ORCHESTRATION", "Cloud Composer API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_app_engine": _product("App Engine", "APPLICATION_HOSTING", "App Engine Admin API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_vertex_ai_search": _product("Vertex AI Search", "ENTERPRISE_SEARCH_AND_RAG", "Vertex AI Search API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_dialogflow": _product("Dialogflow", "CONVERSATIONAL_AI", "Dialogflow API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_natural_language": _product("Cloud Natural Language AI", "LANGUAGE_AI", "Cloud Natural Language API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_video_intelligence": _product("Cloud Video Intelligence", "VIDEO_ANALYSIS", "Cloud Video Intelligence API", "CLOUD_PROJECT_CREDENTIALS"),
    "google_recommendations_ai": _product("Recommendations AI", "PERSONALIZATION", "Recommendations AI API", "CLOUD_PROJECT_CREDENTIALS", "PRODUCT_NAME_AND_API_AVAILABILITY_MAY_CHANGE"),
    # Ads, measurement, maps, and commerce
    "google_adsense": _product("Google AdSense", "PUBLISHER_MONETIZATION", "AdSense Management API", availability="PUBLISHER_ACCOUNT_AND_API_ACCESS_REQUIRED"),
    "google_admob": _product("Google AdMob", "MOBILE_ADVERTISING", "AdMob API", availability="PUBLISHER_ACCOUNT_AND_API_ACCESS_REQUIRED"),
    "google_merchant_center": _product("Google Merchant Center", "COMMERCE_AND_PRODUCT_FEEDS", "Merchant API", availability="MERCHANT_ACCOUNT_AND_API_ELIGIBILITY_REQUIRED"),
    "google_street_view": _product("Street View", "MAPS_AND_IMAGERY", "Street View APIs", "API_KEY_OR_OAUTH", "API_AVAILABLE_WITH_BILLING_AND_RESTRICTIONS"),
    "google_maps_elevation": _product("Google Maps Elevation", "MAPS_AND_GEOSPATIAL", "Elevation API", "API_KEY_OR_OAUTH", "API_AVAILABLE_WITH_BILLING_AND_RESTRICTIONS"),
    "google_maps_time_zone": _product("Google Maps Time Zone", "MAPS_AND_GEOSPATIAL", "Time Zone API", "API_KEY_OR_OAUTH", "API_AVAILABLE_WITH_BILLING_AND_RESTRICTIONS"),
    "google_maps_directions_legacy": _product("Google Maps Directions (legacy)", "MAPS_AND_ROUTES", "Directions API (Legacy)", "API_KEY_OR_OAUTH", "LEGACY_API_USE_NEW_ROUTES_API_FOR_NEW_WORK"),
    # Consumer and information products with limited or no general public API
    "google_art_and_culture": _product("Google Arts & Culture", "ARTS_AND_CULTURE", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_CONTENT_MANAGEMENT_API"),
    "google_podcasts": _product("Google Podcasts", "AUDIO_AND_MEDIA", None, "PRODUCT_INFORMATION_ONLY", "DISCONTINUED"),
    "google_duo": _product("Google Duo", "COMMUNICATION", None, "PRODUCT_INFORMATION_ONLY", "REPLACED_BY_GOOGLE_MEET"),
    "google_play_games": _product("Google Play Games", "GAMING", "Google Play Games Services API", availability="GAME_AND_PROJECT_ELIGIBILITY_REQUIRED"),
    "google_family_link": _product("Google Family Link", "FAMILY_AND_DEVICE_CONTROLS", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_PARENTAL_CONTROL_API"),
    "google_store": _product("Google Store", "HARDWARE_COMMERCE", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_RETAIL_ORDER_API"),
    "google_pixel": _product("Google Pixel", "HARDWARE", None, "PRODUCT_INFORMATION_ONLY", "DEVICE_PRODUCT_INFORMATION"),
    "google_nest": _product("Google Nest", "SMART_HOME", "Google Home APIs (eligible device/project use cases)", "OAUTH_OR_DEVICE_API", "API_AVAILABLE_WITH_DEVICE_AND_PROJECT_ELIGIBILITY"),
}


class GoogleEcosystemService:
    """Expose safe product metadata without claiming live connectivity."""

    def catalog(self) -> list[dict[str, Any]]:
        return [{"id": key, **value} for key, value in GOOGLE_PRODUCTS.items()]

    def status(self) -> dict[str, Any]:
        oauth_configured = all(os.getenv(name, "").strip() for name in (
            "GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET", "GOOGLE_REDIRECT_URI"
        ))
        cloud_configured = bool(
            os.getenv("GOOGLE_CLOUD_PROJECT", "").strip()
            and (
                os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "").strip()
                or os.getenv("GOOGLE_CLOUD_CREDENTIALS_JSON", "").strip()
                or os.getenv("GOOGLE_CLOUD_WORKLOAD_IDENTITY_PROVIDER", "").strip()
            )
        )
        return {
            "success": True,
            "ecosystem": "google_ecosystem",
            "status": "REGISTRY_READY",
            "product_count": len(GOOGLE_PRODUCTS),
            "google_oauth_app_configured": oauth_configured,
            "google_cloud_identity_configured": cloud_configured,
            "live_connection_verified": False,
            "oauth_flow_status": "PENDING_IMPLEMENTATION",
            "token_storage_status": "NOT_IMPLEMENTED",
            "products": [
                {"id": product_id, "name": product["name"],
                 "availability": product["availability"],
                 "integration_mode": product["integration_mode"], "connected": False}
                for product_id, product in GOOGLE_PRODUCTS.items()
            ],
            "security_note": (
                "This is a service catalog, not proof of connection. No Google token is "
                "stored or returned. Live integrations require consent, secure token "
                "storage, least-privilege access, and end-to-end verification."
            ),
        }

    def get_product(self, product_id: str) -> dict[str, Any] | None:
        key = product_id.strip().lower()
        product = GOOGLE_PRODUCTS.get(key)
        return {"id": key, **product} if product is not None else None
