"""Family, Parenting & Community Support domain package; classification only, not verified live listings."""
DOMAIN_ID = "family_relationships_community"
DOMAIN_NAME = "Family, Parenting & Community Support"
ADULT_RESTRICTED = False
DEFAULT_DISCOVERY_ENABLED = True
SUBCATEGORY_IDS: tuple[str, ...] = (
    "personal_development",
    "parenting_education",
    "family_support",
    "caregiver_support",
    "elder_support",
    "community_groups",
    "friendship_communities",
    "life_skills",
    "wellbeing_education",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
