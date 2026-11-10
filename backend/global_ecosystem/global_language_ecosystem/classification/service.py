"""Classify requests into language ecosystem domains."""
from ..catalog import LANGUAGE_DOMAINS


def classify_language_domain(topic: str) -> str:
    normalized = topic.strip().lower().replace("-", "_").replace(" ", "_")
    aliases = {
        "translation": "translation",
        "translate": "translation",
        "localisation": "localization",
        "localization": "localization",
        "speech": "speech_and_audio",
        "audio": "speech_and_audio",
        "tts": "speech_and_audio",
        "asr": "speech_and_audio",
        "learning": "language_learning",
        "education": "language_learning",
        "linguistics": "linguistics",
        "indian": "indian_languages",
        "bharatiya": "indian_languages",
        "world": "global_languages",
        "global": "global_languages",
        "accessibility": "accessibility",
        "safety": "governance_and_safety",
    }
    result = aliases.get(normalized, normalized)
    if result not in LANGUAGE_DOMAINS:
        raise KeyError(f"unknown language domain: {topic}")
    return result
