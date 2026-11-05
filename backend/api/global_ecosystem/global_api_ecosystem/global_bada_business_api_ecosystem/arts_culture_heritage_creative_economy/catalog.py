"""Arts, culture, heritage and creative-economy taxonomy."""

CATEGORIES = [
    {"id": "visual_fine_arts", "name": "Visual Arts & Fine Arts", "channels": ["offline", "hybrid", "online"], "subcategories": ["painting", "sculpture", "drawing", "printmaking", "illustration", "ceramics_art", "installation_art", "public_art"]},
    {"id": "performing_arts", "name": "Performing Arts & Theatre", "channels": ["offline", "hybrid"], "subcategories": ["theatre", "drama", "opera", "puppetry", "circus_arts", "contemporary_performance", "stagecraft"]},
    {"id": "music_dance_traditions", "name": "Music, Dance & Traditional Performance", "channels": ["offline", "hybrid", "online"], "subcategories": ["classical_music", "folk_music", "contemporary_music", "classical_dance", "folk_dance", "traditional_instruments", "music_heritage"]},
    {"id": "museums_galleries", "name": "Museums, Galleries & Exhibition Institutions", "channels": ["offline", "hybrid"], "subcategories": ["art_museums", "history_museums", "science_culture_museums", "public_galleries", "curatorial_services", "collections_management"]},
    {"id": "libraries_archives", "name": "Libraries, Archives & Documentation", "channels": ["offline", "hybrid", "online"], "subcategories": ["public_libraries", "special_collections", "manuscript_libraries", "historical_archives", "oral_history_archives", "document_preservation"]},
    {"id": "cultural_heritage_sites", "name": "Cultural Heritage, Monuments & Sites", "channels": ["offline", "hybrid", "online"], "subcategories": ["monuments", "archaeological_sites", "historic_buildings", "cultural_landscapes", "sacred_heritage_sites", "heritage_interpretation"]},
    {"id": "heritage_conservation", "name": "Heritage Conservation & Restoration", "channels": ["offline", "hybrid"], "subcategories": ["monument_conservation", "art_restoration", "manuscript_conservation", "heritage_architecture", "conservation_science", "preventive_conservation"]},
    {"id": "handicrafts_traditional_crafts", "name": "Handicrafts & Traditional Craft Industries", "channels": ["offline", "hybrid", "online"], "subcategories": ["textile_crafts", "wood_crafts", "metal_crafts", "stone_crafts", "pottery_crafts", "jewellery_crafts", "artisan_cooperatives"]},
    {"id": "folk_indigenous_arts", "name": "Folk, Indigenous & Community Arts", "channels": ["offline", "hybrid", "online"], "subcategories": ["folk_painting", "tribal_art", "community_performance", "indigenous_crafts", "living_heritage", "community_cultural_centres"]},
    {"id": "cultural_institutions", "name": "Cultural Institutions & Organisations", "channels": ["offline", "hybrid", "online"], "subcategories": ["arts_councils", "cultural_foundations", "academies", "heritage_trusts", "artist_associations", "cultural_nonprofits"]},
    {"id": "cultural_events_festivals", "name": "Cultural Events, Festivals & Exhibitions", "channels": ["offline", "hybrid"], "subcategories": ["arts_festivals", "heritage_festivals", "literary_festivals", "craft_fairs", "museum_exhibitions", "community_celebrations"]},
    {"id": "language_literature_oral_traditions", "name": "Languages, Literature & Oral Traditions", "channels": ["offline", "hybrid", "online"], "subcategories": ["regional_literature", "oral_storytelling", "poetry", "translation_heritage_texts", "endangered_languages", "folklore_documentation"]},
    {"id": "arts_education_training", "name": "Arts Education, Training & Apprenticeships", "channels": ["offline", "hybrid", "online"], "subcategories": ["fine_arts_education", "music_training", "dance_training", "craft_apprenticeships", "museum_learning", "heritage_skills_training"]},
    {"id": "digital_cultural_preservation", "name": "Digital Culture, Archives & Preservation", "channels": ["online", "hybrid"], "subcategories": ["digital_archives", "3d_heritage_digitisation", "virtual_museums", "digital_collections", "cultural_data_standards", "digital_storytelling"]},
    {"id": "creative_economy_enterprise", "name": "Creative Economy & Cultural Entrepreneurship", "channels": ["offline", "hybrid", "online"], "subcategories": ["artist_enterprises", "artisan_businesses", "creative_cooperatives", "cultural_enterprise_support", "ethical_craft_markets", "creative_commissioning"]},
    {"id": "cultural_policy_research", "name": "Cultural Policy, Research & Impact", "channels": ["offline", "hybrid", "online"], "subcategories": ["cultural_policy", "heritage_research", "audience_research", "cultural_economics", "social_impact_assessment", "intangible_heritage_inventory"]},
]


def list_categories():
    """Return defensive copies of all category records."""
    return [dict(item, channels=list(item["channels"]), subcategories=list(item["subcategories"])) for item in CATEGORIES]


def get_category(category_id: str):
    """Return a category by stable identifier, or None."""
    for item in CATEGORIES:
        if item["id"] == category_id:
            return dict(item, channels=list(item["channels"]), subcategories=list(item["subcategories"]))
    return None


def validate_catalog():
    ids = [item["id"] for item in CATEGORIES]
    duplicates = sorted({item_id for item_id in ids if ids.count(item_id) > 1})
    return {"valid": not duplicates, "category_count": len(CATEGORIES), "duplicate_ids": duplicates}
