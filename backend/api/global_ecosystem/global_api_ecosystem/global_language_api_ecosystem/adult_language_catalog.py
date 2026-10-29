"""Adult relationship, intimacy, consent, and sexual-health language support.

The catalog is educational and non-graphic. It covers vocabulary and translation
domains for consenting adults, healthcare, safety, and respectful communication.
It is not an erotic-content generator or a medical diagnosis service.
"""
from __future__ import annotations

from typing import Any

ADULT_LANGUAGE_DOMAINS: tuple[dict[str, str], ...] = (
    {"id": "adult_relationship_communication", "name": "Adult relationship communication", "scope": "Respectful communication, boundaries, expectations, and mutual understanding"},
    {"id": "consent_and_boundaries", "name": "Consent and boundaries", "scope": "Clear consent, voluntary agreement, refusal, changing one's mind, and personal boundaries"},
    {"id": "sexual_health_education", "name": "Sexual-health education", "scope": "Accurate, non-graphic educational terminology and general health information"},
    {"id": "reproductive_health", "name": "Reproductive health", "scope": "Reproductive anatomy, fertility, contraception, pregnancy, and family planning vocabulary"},
    {"id": "sti_testing_and_prevention", "name": "STI testing and prevention", "scope": "Testing, prevention, symptoms vocabulary, care access, and clinical communication"},
    {"id": "intimacy_and_wellbeing", "name": "Intimacy and wellbeing", "scope": "Emotional intimacy, comfort, trust, and non-judgmental communication"},
    {"id": "lgbtq_inclusive_health_language", "name": "LGBTQ-inclusive health language", "scope": "Respectful identity language and inclusive health communication"},
    {"id": "relationship_counselling", "name": "Relationship counselling language", "scope": "Conflict resolution, emotional needs, and counselling terminology"},
    {"id": "medical_interpreter_support", "name": "Medical interpreter support", "scope": "Patient-friendly terminology for discussion with qualified clinicians"},
    {"id": "abuse_and_crisis_support", "name": "Abuse and crisis-support terminology", "scope": "Recognizing coercion, seeking support, safety planning vocabulary, and referral language"},
    {"id": "privacy_and_digital_safety", "name": "Privacy and digital safety", "scope": "Intimate-image consent, privacy settings, online boundaries, and reporting abuse"},
    {"id": "adult_education_content_translation", "name": "Adult education content translation", "scope": "Translation of lawful, educational materials intended for adults, subject to policy and local law"},
)

def list_adult_language_domains(query: str | None = None) -> list[dict[str, str]]:
    """Return educational adult-language domains, optionally filtered by name or description."""
    needle = (query or "").strip().casefold()
    return [dict(item) for item in ADULT_LANGUAGE_DOMAINS if not needle or needle in item["id"].casefold() or needle in item["name"].casefold() or needle in item["scope"].casefold()]

def get_adult_language_summary() -> dict[str, Any]:
    """Return the adult language-support scope and safety boundaries."""
    return {
        "domain_count": len(ADULT_LANGUAGE_DOMAINS),
        "languages_available": "use the Global Language catalog; translation coverage varies by provider",
        "scope": "non-graphic education, consensual adult relationships, consent, reproductive and sexual health",
        "provider_status": "CATALOG_ONLY",
        "medical_advice": "general educational information only; consult qualified health professionals for personal medical advice",
    }
