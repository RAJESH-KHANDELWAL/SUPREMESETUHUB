"""Machine-readable catalog entry for Google Gemini."""

PROVIDER = {
    "id": "google_gemini",
    "name": "Google Gemini",
    "vendor": "Google",
    "category": "ai_provider",
    "api_endpoint": "https://generativelanguage.googleapis.com",
    "credential_env": "GOOGLE_GEMINI_API_KEY",
    "models_or_services": ["gemini-2.5-pro","gemini-2.5-flash"],
    "integration_status": "scaffold",
    "notes": "Gemini API adapter boundary; use Google's official SDK or REST contract.",
}
