"""Machine-readable catalog entry for Anthropic Claude."""

PROVIDER = {
    "id": "anthropic_claude",
    "name": "Anthropic Claude",
    "vendor": "Anthropic",
    "category": "ai_provider",
    "api_endpoint": "https://api.anthropic.com",
    "credential_env": "ANTHROPIC_API_KEY",
    "models_or_services": ["claude-sonnet","claude-opus"],
    "integration_status": "scaffold",
    "notes": "Anthropic Messages API adapter boundary.",
}
