"""Catalog metadata for ElevenLabs; API integration is not implied."""

PROVIDER = {
    "id": "elevenlabs",
    "name": "ElevenLabs",
    "vendor": "ElevenLabs",
    "category": "audio_ai_provider",
    "api_endpoint": None,
    "credential_env": None,
    "models_or_services": ["Text to speech","Speech to text","Voice tools"],
    "integration_status": "catalog_only",
    "notes": "Audio AI platform; verify current API endpoint, auth and voice permissions before production use.",
}
