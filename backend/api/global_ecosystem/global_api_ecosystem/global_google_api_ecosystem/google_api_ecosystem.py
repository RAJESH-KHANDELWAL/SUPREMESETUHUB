"""Google provider-owned API ecosystem metadata.

Catalog metadata only. This module does not authenticate or make network requests.
"""
from __future__ import annotations

GOOGLE_API_ECOSYSTEM = {
    "provider_id": "google",
    "name": "GOOGLE API ECOSYSTEM",
    "status": "CATALOG_ONLY_UNLESS_ADAPTER_TESTS_PASS",
    "live_connection_verified": False,
    "platforms": [
        "Google Workspace", "Google Play", "Google Cloud Console",
        "Google Maps Platform", "Google Search Console", "Google Analytics",
        "Firebase"
    ],
    "api_families": [
        "identity_oauth", "workspace", "gmail", "calendar", "drive",
        "docs_sheets", "maps", "analytics", "search_console", "youtube",
        "cloud", "firebase", "vertex_ai_gemini", "cloud_dns", "iam"
    ],
    "related_ecosystems": [
        "AI", "CLOUD", "COMMUNICATION", "DATABASE", "DEVELOPER",
        "DNS", "SECURITY", "STORAGE", "WEB", "WEBSITE"
    ],
    "adapter_path": "backend/integrations/providers/google.py",
    "credential_source": "environment_or_managed_secret_store",
}
