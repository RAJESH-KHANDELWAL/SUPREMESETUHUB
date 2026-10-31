"""Work, Jobs & Careers domain package; classification only, not verified live listings."""
DOMAIN_ID = "work_careers_employment"
DOMAIN_NAME = "Work, Jobs & Careers"
ADULT_RESTRICTED = False
DEFAULT_DISCOVERY_ENABLED = True
SUBCATEGORY_IDS: tuple[str, ...] = (
    "government_jobs",
    "private_sector_jobs",
    "public_sector_jobs",
    "international_jobs",
    "local_jobs",
    "remote_jobs",
    "hybrid_jobs",
    "full_time_jobs",
    "part_time_jobs",
    "contract_jobs",
    "temporary_jobs",
    "seasonal_jobs",
    "shift_work",
    "entry_level_jobs",
    "experienced_jobs",
    "executive_jobs",
    "career_changes",
    "return_to_work",
    "retirement_work",
    "career_guidance",
    "recruitment",
    "staffing",
    "placements",
)
def list_subcategories() -> list[dict[str, str]]:
    """Return stable subcategory IDs and human-readable labels."""
    return [{"id": value, "name": value.replace("_", " ").title(), "domain_id": DOMAIN_ID} for value in SUBCATEGORY_IDS]
