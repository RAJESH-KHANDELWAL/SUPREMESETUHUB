"""Regional scope categories from local communities to global operations."""
SCOPES = {
    "india": ("national", "state", "union_territory", "district", "community", "tribal_and_indigenous"),
    "south_asia": ("cross_border_languages", "diaspora_communities"),
    "global": ("country", "territory", "multilingual_region", "diaspora", "international_organization"),
}

def get_regional_language_scopes() -> dict[str, tuple[str, ...]]:
    return dict(SCOPES)
