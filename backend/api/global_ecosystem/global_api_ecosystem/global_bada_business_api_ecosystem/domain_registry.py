"""Central India and Global work/business domain registry."""
from .work_careers_employment import DOMAIN_ID as WORK_ID, DOMAIN_NAME as WORK_NAME, SUBCATEGORY_IDS as WORK_SUBS
from .freelance_gig_independent_work import DOMAIN_ID as FREELANCE_ID, DOMAIN_NAME as FREELANCE_NAME, SUBCATEGORY_IDS as FREELANCE_SUBS
from .students_education_skills import DOMAIN_ID as STUDENTS_ID, DOMAIN_NAME as STUDENTS_NAME, SUBCATEGORY_IDS as STUDENTS_SUBS
from .business_companies_trade import DOMAIN_ID as BUSINESS_ID, DOMAIN_NAME as BUSINESS_NAME, SUBCATEGORY_IDS as BUSINESS_SUBS
from .entrepreneurship_startups import DOMAIN_ID as STARTUP_ID, DOMAIN_NAME as STARTUP_NAME, SUBCATEGORY_IDS as STARTUP_SUBS
from .home_homemaker_care_economy import DOMAIN_ID as HOME_ID, DOMAIN_NAME as HOME_NAME, SUBCATEGORY_IDS as HOME_SUBS
from .industries_professional_services import DOMAIN_ID as INDUSTRY_ID, DOMAIN_NAME as INDUSTRY_NAME, SUBCATEGORY_IDS as INDUSTRY_SUBS
from .family_relationships_community import DOMAIN_ID as FAMILY_ID, DOMAIN_NAME as FAMILY_NAME, SUBCATEGORY_IDS as FAMILY_SUBS
from .adult_18_plus_lawful_industry import DOMAIN_ID as ADULT_ID, DOMAIN_NAME as ADULT_NAME, SUBCATEGORY_IDS as ADULT_SUBS
from .services_platforms_integrations import DOMAIN_ID as PLATFORM_ID, DOMAIN_NAME as PLATFORM_NAME, SUBCATEGORY_IDS as PLATFORM_SUBS
from .investment_finance_support import DOMAIN_ID as FINANCE_ID, DOMAIN_NAME as FINANCE_NAME, SUBCATEGORY_IDS as FINANCE_SUBS
from .public_nonprofit_social_impact import DOMAIN_ID as PUBLIC_ID, DOMAIN_NAME as PUBLIC_NAME, SUBCATEGORY_IDS as PUBLIC_SUBS

_DOMAIN_DEFINITIONS = (
    (WORK_ID, WORK_NAME, WORK_SUBS, False),
    (FREELANCE_ID, FREELANCE_NAME, FREELANCE_SUBS, False),
    (STUDENTS_ID, STUDENTS_NAME, STUDENTS_SUBS, False),
    (BUSINESS_ID, BUSINESS_NAME, BUSINESS_SUBS, False),
    (STARTUP_ID, STARTUP_NAME, STARTUP_SUBS, False),
    (HOME_ID, HOME_NAME, HOME_SUBS, False),
    (INDUSTRY_ID, INDUSTRY_NAME, INDUSTRY_SUBS, False),
    (FAMILY_ID, FAMILY_NAME, FAMILY_SUBS, False),
    (ADULT_ID, ADULT_NAME, ADULT_SUBS, True),
    (PLATFORM_ID, PLATFORM_NAME, PLATFORM_SUBS, False),
    (FINANCE_ID, FINANCE_NAME, FINANCE_SUBS, False),
    (PUBLIC_ID, PUBLIC_NAME, PUBLIC_SUBS, False),
)

DOMAIN_REGISTRY = tuple({
    "id": domain_id, "name": name, "subcategory_ids": tuple(subcategories),
    "subcategory_count": len(subcategories), "adult_only": adult_only,
    "default_discovery_enabled": not adult_only, "coverage_scope": ("india", "global"),
    "registry_status": "taxonomy_only",
} for domain_id, name, subcategories, adult_only in _DOMAIN_DEFINITIONS)

def list_domains(include_adult=False):
    return [{**item, "subcategory_ids": list(item["subcategory_ids"]), "coverage_scope": list(item["coverage_scope"])} for item in DOMAIN_REGISTRY if include_adult or not item["adult_only"]]

def get_domain(domain_id, include_adult=False):
    for item in DOMAIN_REGISTRY:
        if item["id"] == domain_id and (include_adult or not item["adult_only"]):
            return {**item, "subcategory_ids": list(item["subcategory_ids"]), "coverage_scope": list(item["coverage_scope"])}
    return None

def search_domains(query, include_adult=False):
    needle = query.strip().casefold()
    if not needle:
        return []
    found = []
    for item in DOMAIN_REGISTRY:
        if item["adult_only"] and not include_adult:
            continue
        for subcategory in item["subcategory_ids"]:
            if needle in item["id"].casefold() or needle in item["name"].casefold() or needle in subcategory.casefold():
                found.append({"domain_id": item["id"], "domain_name": item["name"], "subcategory_id": subcategory, "subcategory_name": subcategory.replace("_", " ").title()})
    return found

def validate_domain_registry():
    ids = [item["id"] for item in DOMAIN_REGISTRY]
    duplicate_ids = sorted({value for value in ids if ids.count(value) > 1})
    duplicate_subcategories = {item["id"]: sorted({value for value in item["subcategory_ids"] if item["subcategory_ids"].count(value) > 1}) for item in DOMAIN_REGISTRY if len(item["subcategory_ids"]) != len(set(item["subcategory_ids"]))}
    empty_domains = [item["id"] for item in DOMAIN_REGISTRY if not item["subcategory_ids"]]
    adult_ids = {item["id"] for item in DOMAIN_REGISTRY if item["adult_only"]}
    default_ids = {item["id"] for item in list_domains()}
    adult_excluded = not bool(adult_ids & default_ids)
    return {"registry_status": "taxonomy_only", "domain_count": len(DOMAIN_REGISTRY), "subcategory_count": sum(item["subcategory_count"] for item in DOMAIN_REGISTRY), "adult_domain_count": len(adult_ids), "duplicate_domain_ids": duplicate_ids, "duplicate_subcategories": duplicate_subcategories, "empty_domains": empty_domains, "adult_excluded_by_default": adult_excluded, "structurally_valid": not duplicate_ids and not duplicate_subcategories and not empty_domains and adult_excluded, "live_data_verified": False, "worldwide_exhaustiveness_claimed": False}
