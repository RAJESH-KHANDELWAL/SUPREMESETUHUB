"""Google API ecosystem metadata and child catalog access."""
from __future__ import annotations

GOOGLE_API_ECOSYSTEM = {
    "provider_id": "google",
    "name": "GOOGLE API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "platforms": [
        "Google Workspace", "Google Cloud", "Google Maps Platform",
        "Google Play", "Google Search Console", "Google Analytics", "Firebase",
        "Google Ads", "Google Business Profile", "YouTube",
    ],
    "api_families": [
        "gmail", "drive", "calendar", "contacts", "sheets", "docs", "slides",
        "forms", "chat", "meet", "admin_sdk", "people", "youtube", "maps",
        "business_profile", "ads", "analytics", "search_console", "cloud",
        "firebase", "identity_oauth", "vertex_ai", "gemini",
    ],
    "children": [
        {"id": "gmail", "name": "GOOGLE GMAIL API ECOSYSTEM", "folder": "google_gmail_api_ecosystem", "status": "adapter_scaffold"},
        {"id": "drive", "name": "GOOGLE DRIVE API ECOSYSTEM", "folder": "google_drive_api_ecosystem", "status": "catalog_only"},
        {"id": "calendar", "name": "GOOGLE CALENDAR API ECOSYSTEM", "folder": "google_calendar_api_ecosystem", "status": "catalog_only"},
        {"id": "contacts", "name": "GOOGLE CONTACTS API ECOSYSTEM", "folder": "google_contacts_api_ecosystem", "status": "catalog_only"},
        {"id": "sheets", "name": "GOOGLE SHEETS API ECOSYSTEM", "folder": "google_sheets_api_ecosystem", "status": "catalog_only"},
        {"id": "docs", "name": "GOOGLE DOCS API ECOSYSTEM", "folder": "google_docs_api_ecosystem", "status": "catalog_only"},
        {"id": "slides", "name": "GOOGLE SLIDES API ECOSYSTEM", "folder": "google_slides_api_ecosystem", "status": "catalog_only"},
        {"id": "forms", "name": "GOOGLE FORMS API ECOSYSTEM", "folder": "google_forms_api_ecosystem", "status": "catalog_only"},
        {"id": "chat", "name": "GOOGLE CHAT API ECOSYSTEM", "folder": "google_chat_api_ecosystem", "status": "catalog_only"},
        {"id": "meet", "name": "GOOGLE MEET API ECOSYSTEM", "folder": "google_meet_api_ecosystem", "status": "catalog_only"},
        {"id": "admin_sdk", "name": "GOOGLE ADMIN SDK API ECOSYSTEM", "folder": "google_admin_sdk_api_ecosystem", "status": "catalog_only"},
        {"id": "people", "name": "GOOGLE PEOPLE API ECOSYSTEM", "folder": "google_people_api_ecosystem", "status": "catalog_only"},
        {"id": "youtube", "name": "GOOGLE YOUTUBE API ECOSYSTEM", "folder": "google_youtube_api_ecosystem", "status": "catalog_only"},
        {"id": "maps", "name": "GOOGLE MAPS PLATFORM API ECOSYSTEM", "folder": "google_maps_platform_api_ecosystem", "status": "catalog_only"},
        {"id": "business_profile", "name": "GOOGLE BUSINESS PROFILE API ECOSYSTEM", "folder": "google_business_profile_api_ecosystem", "status": "catalog_only"},
        {"id": "ads", "name": "GOOGLE ADS API ECOSYSTEM", "folder": "google_ads_api_ecosystem", "status": "catalog_only"},
        {"id": "analytics", "name": "GOOGLE ANALYTICS API ECOSYSTEM", "folder": "google_analytics_api_ecosystem", "status": "catalog_only"},
        {"id": "search_console", "name": "GOOGLE SEARCH CONSOLE API ECOSYSTEM", "folder": "google_search_console_api_ecosystem", "status": "catalog_only"},
        {"id": "cloud", "name": "GOOGLE CLOUD API ECOSYSTEM", "folder": "google_cloud_api_ecosystem", "status": "catalog_only"},
        {"id": "firebase", "name": "GOOGLE FIREBASE API ECOSYSTEM", "folder": "google_firebase_api_ecosystem", "status": "catalog_only"},
        {"id": "identity_oauth", "name": "GOOGLE IDENTITY AND OAUTH API ECOSYSTEM", "folder": "google_identity_oauth_api_ecosystem", "status": "catalog_only"},
        {"id": "vertex_ai", "name": "GOOGLE VERTEX AI API ECOSYSTEM", "folder": "google_vertex_ai_api_ecosystem", "status": "catalog_only"},
        {"id": "gemini", "name": "GOOGLE GEMINI API ECOSYSTEM", "folder": "google_gemini_api_ecosystem", "status": "adapter_scaffold"},
    ],
    "related_ecosystems": [
        "GLOBAL AI API ECOSYSTEM", "GLOBAL CLOUD API ECOSYSTEM",
        "GLOBAL COMMUNICATION API ECOSYSTEM", "GLOBAL STORAGE API ECOSYSTEM",
        "GLOBAL SECURITY API ECOSYSTEM", "GLOBAL DEVELOPER API ECOSYSTEM",
    ],
    "adapter_path": "backend/integrations/providers/google.py",
    "credential_source": "environment_or_managed_secret_store",
}


def list_google_api_ecosystems() -> dict[str, object]:
    """List child Google API catalogs; this does not assert live connectivity."""
    children = [dict(item) for item in GOOGLE_API_ECOSYSTEM["children"]]
    return {
        "success": True,
        "provider": GOOGLE_API_ECOSYSTEM["name"],
        "status": GOOGLE_API_ECOSYSTEM["status"],
        "live_connection_verified": False,
        "count": len(children),
        "ecosystems": children,
    }
