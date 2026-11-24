"""Global work and business coverage across delivery and work modes.

Taxonomy only: this is not a directory of verified employers or live vacancies.
"""
from ..business_catalog import BUSINESS_CATEGORIES

DELIVERY_MODES = ("offline", "online", "hybrid")
WORK_MODES = ("employee", "freelance", "gig", "contract", "temporary", "internship", "apprenticeship", "self_employed", "business_owner", "volunteer", "seasonal", "project_based", "remote", "on_site")
BUSINESS_SIZES = ("individual", "home_based", "micro", "small", "medium", "large", "enterprise", "multinational")
MATURITY_LEVELS = ("traditional", "established", "emerging", "future")
GEOGRAPHY_LEVELS = ("global", "country", "state_or_province", "city", "district", "neighbourhood", "rural_locality")
AUDIENCE_GROUPS = ("individuals", "students", "job_seekers", "employees", "workers", "freelancers", "self_employed", "entrepreneurs", "business_owners", "homemakers", "parents", "caregivers", "professionals", "businesses", "institutions")

def get_sector_facets():
    return {
        "delivery_modes": list(DELIVERY_MODES), "work_modes": list(WORK_MODES),
        "business_sizes": list(BUSINESS_SIZES), "maturity_levels": list(MATURITY_LEVELS),
        "geography_levels": list(GEOGRAPHY_LEVELS), "audience_groups": list(AUDIENCE_GROUPS),
    }

def get_sector(sector_id):
    item = next((row for row in BUSINESS_CATEGORIES if row["id"] == sector_id), None)
    if item is None:
        return None
    result = dict(item)
    result.update({
        "delivery_modes": list(item.get("modes", DELIVERY_MODES)),
        "classification": "taxonomy_only",
    })
    if result.get("adult_only"):
        result["minimum_age"] = 18
        result["safeguards"] = ["adults_only", "documented_informed_consent", "privacy_and_data_protection", "jurisdictional_legal_compliance", "no_minors", "no_coercion_or_exploitation"]
    return result

def list_sectors(channel=None, include_adult=False):
    if channel is not None and channel not in DELIVERY_MODES:
        raise ValueError("channel must be offline, online, or hybrid")
    result = []
    for row in BUSINESS_CATEGORIES:
        if row.get("adult_only") and not include_adult:
            continue
        if channel and channel not in row.get("modes", DELIVERY_MODES):
            continue
        result.append(get_sector(row["id"]))
    return result
