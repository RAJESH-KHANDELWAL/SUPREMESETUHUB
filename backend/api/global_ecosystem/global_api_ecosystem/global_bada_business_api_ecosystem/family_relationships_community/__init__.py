"""Individuals, Couples, Family & Community domain package; classification only, not verified live listings."""
DOMAIN_ID = "family_relationships_community"
DOMAIN_NAME = "Individuals, Couples, Family & Community"
ADULT_RESTRICTED = false
DEFAULT_DISCOVERY_ENABLED = true
SUBCATEGORY_IDS: tuple[str, ...] = (
    "personal_development",
    "relationship_education",
    "couple_communication",
    "marriage_education",
    "parenting_education",
    "family_support",
    "caregiver_support",
    "elder_support",
    "community_groups",
    "friendship_communities",
    "life_skills",
    "conflict_resolution",
    "professional_counselling_directory",
    "wellbeing_education",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
