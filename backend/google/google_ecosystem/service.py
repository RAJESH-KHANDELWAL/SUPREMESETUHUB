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
    "google_meet": _product("Google Meet", "VIDEO_MEETINGS", "Google Meet REST API", availability="API_AVAILABLE_WITH_ELIGIBILITY_AND_SCOPES"),
    "google_calendar": _product("Google Calendar", "SCHEDULING", "Google Calendar API", scopes=["https://www.googleapis.com/auth/calendar.events"]),
    "google_contacts": _product("Google Contacts", "CONTACTS", "People API", scopes=["https://www.googleapis.com/auth/contacts.readonly"]),
    "google_voice": _product("Google Voice", "COMMUNICATION", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_CONSUMER_API"),
    "google_groups": _product("Google Groups", "COLLABORATION", "Admin SDK Directory API", availability="WORKSPACE_ADMIN_ELIGIBILITY_REQUIRED"),
    # Productivity and workspace
    "google_drive": _product("Google Drive", "STORAGE", "Google Drive API", scopes=["https://www.googleapis.com/auth/drive.file"]),
    "google_docs": _product("Google Docs", "PRODUCTIVITY", "Google Docs API", scopes=["https://www.googleapis.com/auth/documents"]),
    "google_sheets": _product("Google Sheets", "PRODUCTIVITY", "Google Sheets API", scopes=["https://www.googleapis.com/auth/spreadsheets"]),
    "google_slides": _product("Google Slides", "PRODUCTIVITY", "Google Slides API"),
    "google_forms": _product("Google Forms", "FORMS_AND_SURVEYS", "Google Forms API"),
    "google_sites": _product("Google Sites", "WEBSITE_BUILDER", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_CONTENT_MANAGEMENT_API"),
    "google_keep": _product("Google Keep", "NOTES", "Google Keep API", availability="WORKSPACE_ELIGIBILITY_REQUIRED"),
    "google_tasks": _product("Google Tasks", "TASK_MANAGEMENT", "Google Tasks API", scopes=["https://www.googleapis.com/auth/tasks.readonly"]),
    "google_jamboard": _product("Google Jamboard", "COLLABORATION", None, "PRODUCT_INFORMATION_ONLY", "DISCONTINUED"),
    "google_workspace_admin": _product("Google Workspace Admin", "ADMINISTRATION", "Admin SDK APIs", availability="WORKSPACE_ADMIN_ELIGIBILITY_REQUIRED"),
    "google_one": _product("Google One", "SUBSCRIPTION_AND_STORAGE_PLAN", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_GOOGLE_ONE_API", auth="Google account / plan management", notes="Membership and consumer plan controls are not exposed as a general public API for this backend."),
    # Cloud, developer, AI and data
    "google_cloud": _product("Google Cloud", "CLOUD_INFRASTRUCTURE", "Google Cloud APIs", "CLOUD_PROJECT_CREDENTIALS", auth="Workload Identity Federation or least-privilege service account", notes="Use a separate Cloud identity; do not reuse consumer Gmail OAuth as Cloud administrator credentials."),
    "firebase": _product("Firebase", "APP_DEVELOPMENT_AND_BACKEND", "Firebase APIs", "CLOUD_PROJECT_CREDENTIALS", auth="Firebase Authentication / Google Cloud IAM"),
    "google_maps_platform": _product("Google Maps Platform", "MAPS_AND_LOCATION", "Maps Platform APIs", "API_KEY_OR_OAUTH", "API_AVAILABLE_WITH_BILLING_AND_RESTRICTIONS", auth="Restricted API key or supported OAuth flow"),
    "google_places": _product("Google Places", "MAPS_AND_LOCATION", "Places API", "API_KEY_OR_OAUTH", "API_AVAILABLE_WITH_BILLING_AND_RESTRICTIONS"),
    "google_routes": _product("Google Routes", "MAPS_AND_LOCATION", "Routes API", "API_KEY_OR_OAUTH", "API_AVAILABLE_WITH_BILLING_AND_RESTRICTIONS"),
    "google_geocoding": _product("Google Geocoding", "MAPS_AND_LOCATION", "Geocoding API", "API_KEY_OR_OAUTH", "API_AVAILABLE_WITH_BILLING_AND_RESTRICTIONS"),
    "google_earth": _product("Google Earth", "MAPS_AND_GEOSPATIAL", None, "PRODUCT_INFORMATION_ONLY", "NO_GENERAL_PUBLIC_PRODUCT_CONTROL_API"),
    "google_search": _product("Google Search", "SEARCH", "Programmable Search Engine API", "API_KEY", "LIMITED_API_AND_CONFIGURATION"),
    "google_search_console": _product("Google Search Console", "SEO_AND_SEARCH_PERFORMANCE", "Search Console API"),
    "google_analytics": _product("Google Analytics", "ANALYTICS", "Google Analytics Data API", "USER_OAUTH_OR_CLOUD_IDENTITY", auth="OAuth 2.0 or service account where supported", scopes=["https://www.googleapis.com/auth/analytics.readonly"]),
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
    "google_photos": _product("Google Photos", "MEDIA", "Google Photos APIs", availability="LIMITED_API_AND_SCOPE_AVAILABILITY", notes="Current Photos API policies restrict supported use cases; validate the exact use case before enabling."),
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
