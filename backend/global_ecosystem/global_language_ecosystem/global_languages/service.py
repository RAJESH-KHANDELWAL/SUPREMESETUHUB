"""Global language families and coverage categories."""
LANGUAGE_FAMILIES = {
    "indo_european": ("English", "Hindi", "Spanish", "French", "German", "Portuguese", "Russian", "Persian"),
    "sino_tibetan": ("Mandarin Chinese", "Cantonese", "Tibetan", "Burmese"),
    "afro_asiatic": ("Arabic", "Hebrew", "Amharic", "Hausa"),
    "japonic_and_koreanic": ("Japanese", "Korean"),
    "austronesian": ("Indonesian", "Malay", "Filipino", "Javanese"),
    "dravidian": ("Tamil", "Telugu", "Kannada", "Malayalam"),
    "other_families_and_languages": ("Turkish", "Thai", "Vietnamese", "Swahili", "and other language communities"),
}


def get_global_language_coverage() -> dict[str, tuple[str, ...]]:
    return dict(LANGUAGE_FAMILIES)
