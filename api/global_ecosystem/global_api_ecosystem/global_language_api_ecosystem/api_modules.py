"""Registry of API modules exposed by the Global Language API Ecosystem.

This registry describes module boundaries and route contracts. A catalog entry
does not imply that an external translation, speech, or AI provider is connected.
"""
from __future__ import annotations

from typing import Any

API_MODULES: tuple[dict[str, Any], ...] = (
    {"id": "language_catalog", "name": "Language Catalog API", "category": "catalog", "base_path": "/languages", "methods": ["GET"], "purpose": "Search language records, identifiers, and language families.", "status": "CATALOG_READY"},
    {"id": "locale_region", "name": "Locale and Region API", "category": "catalog", "base_path": "/locales", "methods": ["GET"], "purpose": "Resolve language and regional locale variants.", "status": "CATALOG_READY"},
    {"id": "language_detection", "name": "Language Detection API", "category": "language_intelligence", "base_path": "/detect", "methods": ["POST"], "purpose": "Identify the likely language of supplied text when a detection engine is configured.", "status": "CONTRACT_ONLY"},
    {"id": "translation", "name": "Translation API", "category": "language_intelligence", "base_path": "/translate", "methods": ["POST"], "purpose": "Translate text between supported source and target languages through a verified provider.", "status": "PROVIDER_REQUIRED"},
    {"id": "transliteration", "name": "Transliteration API", "category": "language_intelligence", "base_path": "/transliterate", "methods": ["POST"], "purpose": "Convert text between supported writing systems without claiming semantic translation.", "status": "CONTRACT_ONLY"},
    {"id": "script_catalog", "name": "Script API", "category": "catalog", "base_path": "/scripts", "methods": ["GET"], "purpose": "Catalog writing systems and script metadata.", "status": "CATALOG_PLANNED"},
    {"id": "dictionary", "name": "Dictionary API", "category": "language_resources", "base_path": "/dictionary", "methods": ["GET"], "purpose": "Look up definitions, senses, pronunciation, and usage when licensed lexical data is connected.", "status": "DATASET_REQUIRED"},
    {"id": "speech", "name": "Speech API", "category": "language_intelligence", "base_path": "/speech", "methods": ["POST"], "purpose": "Provide speech-to-text and text-to-speech through configured speech engines.", "status": "PROVIDER_REQUIRED"},
    {"id": "adult_language", "name": "Adult Language API", "category": "specialized_language", "base_path": "/adult-language", "methods": ["GET"], "purpose": "Non-graphic adult communication, consent, relationship, sexual-health education, mature register, and language guidance.", "status": "EDUCATIONAL_CATALOG_READY"},
    {"id": "language_search", "name": "Language Search API", "category": "discovery", "base_path": "/languages", "methods": ["GET"], "purpose": "Search catalog records by language name, code, family, or locale.", "status": "CATALOG_READY"},
)

def list_api_modules(category: str | None = None, status: str | None = None) -> list[dict[str, Any]]:
    """Return API module metadata, optionally filtered by category or status."""
    category_filter = (category or "").strip().casefold()
    status_filter = (status or "").strip().casefold()
    return [
        dict(item)
        for item in API_MODULES
        if (not category_filter or item["category"].casefold() == category_filter)
        and (not status_filter or item["status"].casefold() == status_filter)
    ]

def get_api_module_summary() -> dict[str, Any]:
    """Summarize module readiness without overstating live provider capability."""
    ready = sum(item["status"].endswith("_READY") for item in API_MODULES)
    return {
        "module_count": len(API_MODULES),
        "catalog_ready_count": ready,
        "provider_integrations_live": False,
        "note": "Module registry is architectural metadata; provider-backed operations require separately configured and verified engines.",
    }
