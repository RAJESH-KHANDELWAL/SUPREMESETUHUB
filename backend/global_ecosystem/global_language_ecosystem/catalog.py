"""Global language ecosystem domain catalog.

This package describes language capabilities and domain boundaries. It does not
provide translation models, speech inference, or external API connectivity.
"""
from __future__ import annotations

LANGUAGE_DOMAINS = {
    "language_data": ("language identifiers", "scripts", "dialects", "metadata"),
    "indian_languages": ("Hindi", "Bengali", "Tamil", "Telugu", "Marathi", "Gujarati", "Kannada", "Malayalam", "Punjabi", "Odia", "Assamese", "Urdu", "Sanskrit", "Kashmiri", "Konkani", "Manipuri", "Bodo", "Santali", "Dogri", "Maithili", "Sindhi", "other regional languages"),
    "global_languages": ("English", "Arabic", "Chinese", "French", "German", "Spanish", "Portuguese", "Russian", "Japanese", "Korean", "and other world languages"),
    "translation": ("text translation", "document translation", "website translation", "domain terminology"),
    "localization": ("locale formatting", "regional adaptation", "currencies", "dates", "numbers", "right-to-left layouts"),
    "speech_and_audio": ("speech recognition", "text to speech", "transcription", "subtitles", "captions"),
    "language_learning": ("courses", "vocabulary", "grammar", "assessment", "practice"),
    "linguistics": ("phonetics", "morphology", "syntax", "semantics", "corpora"),
    "accessibility": ("plain language", "screen-reader text", "captions", "multilingual accessibility"),
    "governance_and_safety": ("consent", "privacy", "quality review", "bias evaluation", "rights management"),
}

MATURITY_LEVELS = ("basic", "standard", "advanced", "enterprise", "supreme")
GEOGRAPHIC_SCOPES = ("local", "regional", "India", "international", "global")


def get_language_domains() -> dict[str, tuple[str, ...]]:
    """Return a defensive copy of the language-domain catalog."""
    return dict(LANGUAGE_DOMAINS)
