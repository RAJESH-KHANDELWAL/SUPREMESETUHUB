"""DeepSeek provider API ecosystem metadata; not a live connector."""

PROVIDER_API_ECOSYSTEM = {
    "provider_id": "deepseek",
    "name": "GLOBAL DEEPSEEK API ECOSYSTEM",
    "families": ["AI", "DEVELOPER"],
    "scope": "Official DeepSeek Chat Completions, Responses, Search and Fetch APIs.",
    "api_base_url": "https://api.deepseek.com",
    "authentication": "Bearer API key via server-side DEEPSEEK_API_KEY",
    "models": ["deepseek-flash", "deepseek-v4-pro"],
    "api_families": [
        "CHAT_COMPLETIONS",
        "RESPONSES",
        "SEARCH",
        "FETCH",
    ],
    "status": "CONFIGURATION_READINESS_SCAFFOLD",
    "live_connection_verified": False,
}
