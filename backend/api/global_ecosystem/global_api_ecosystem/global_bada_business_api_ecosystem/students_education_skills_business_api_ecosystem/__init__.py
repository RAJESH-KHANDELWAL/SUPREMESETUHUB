"""Students, Education & Skills domain package; classification only, not verified live listings."""
DOMAIN_ID = "students_education_skills"
DOMAIN_NAME = "Students, Education & Skills"
ADULT_RESTRICTED = False
DEFAULT_DISCOVERY_ENABLED = True
SUBCATEGORY_IDS: tuple[str, ...] = (
    "school_education",
    "higher_education",
    "vocational_education",
    "online_learning",
    "coaching_tuition",
    "test_preparation",
    "certifications",
    "diplomas",
    "degrees",
    "research",
    "scholarships",
    "student_projects",
    "internships",
    "apprenticeships",
    "campus_placements",
    "career_counselling",
    "digital_skills",
    "technical_skills",
    "business_skills",
    "language_learning",
    "financial_literacy",
    "entrepreneurship_education",
    "special_needs_learning",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
