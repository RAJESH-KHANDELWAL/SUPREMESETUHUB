"""Coverage-oriented grouping of Indian languages.

The groups are catalog categories, not a claim of exhaustive dialect coverage.
"""
INDIAN_LANGUAGE_GROUPS = {
    "scheduled_languages": ("Assamese", "Bengali", "Bodo", "Dogri", "Gujarati", "Hindi", "Kannada", "Kashmiri", "Konkani", "Maithili", "Malayalam", "Manipuri", "Marathi", "Nepali", "Odia", "Punjabi", "Sanskrit", "Santali", "Sindhi", "Tamil", "Telugu", "Urdu"),
    "regional_and_community_languages": ("Bhili", "Gondi", "Tulu", "Bhojpuri", "Rajasthani varieties", "Haryanvi", "Chhattisgarhi", "Garhwali", "Kumaoni", "other regional and tribal languages"),
    "scripts_and_variants": ("Devanagari", "Bengali-Assamese", "Gujarati", "Gurmukhi", "Kannada", "Malayalam", "Meitei Mayek", "Odia", "Ol Chiki", "Perso-Arabic", "Tamil", "Telugu"),
}


def get_indian_language_groups() -> dict[str, tuple[str, ...]]:
    return dict(INDIAN_LANGUAGE_GROUPS)
