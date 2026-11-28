from .rules_catalog import list_rules, get_rule
from .catalog import (list_india_requirements, get_india_requirement, list_jurisdictions, list_india_subnational_jurisdictions, get_india_subnational_jurisdiction, get_jurisdiction)

class BusinessComplianceService:
    ECOSYSTEM_ID = "business_compliance_api_ecosystem"

    def get_status(self):
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "status": "compliance_discovery_scaffold",
            "jurisdictions": list_jurisdictions(),
            "country_master_count": len(list_jurisdictions()),
            "country_codes_with_curated_starter_dataset": ["IN"],
            "india_requirement_topics": len(list_india_requirements()),
            "india_compliance_rule_records": len(list_rules("IN")),
            "rajasthan_state_rule_records": len([x for x in list_rules("IN", subdivision_code="RJ") if x["subdivision_code"] == "RJ"]),
            "rules_source_status": "official_portal_links_added_rule_text_not_fully_reviewed",
            "india_subdivision_count": len(list_india_subnational_jurisdictions()),
            "india_state_count": len(list_india_subnational_jurisdictions("state")),
            "india_union_territory_count": len(list_india_subnational_jurisdictions("union_territory")),
            "coverage_note": "India has a starter topic catalogue. Other jurisdictions are framework-only; no country-specific legal checklist is implied.",
            "legal_safety": "Applicability depends on entity, activity, product, turnover, premises, employees, transaction and location. Verify current requirements with official authorities or qualified professionals."
        }

    def list_jurisdictions(self):
        return list_jurisdictions()

    def get_jurisdiction(self, country_code):
        return get_jurisdiction(country_code)

    def list_india_subdivisions(self, subdivision_type=None):
        return list_india_subnational_jurisdictions(subdivision_type)

    def get_india_subdivision(self, subdivision_code):
        return get_india_subnational_jurisdiction(subdivision_code)

    def list_requirements(self, country_code="IN", query=None, area=None, subdivision_code=None):
        if country_code.upper() != "IN":
            return None
        if subdivision_code and not get_india_subnational_jurisdiction(subdivision_code):
            return None
        items = list_india_requirements()
        if area:
            items = [x for x in items if x["area"] == area]
        if query:
            q = query.strip().casefold()
            items = [x for x in items if q in x["id"].casefold() or q in x["name"].casefold() or any(q in v.casefold() for v in x["examples"] + x["applies_to"])]
        return items

    def list_compliance_rules(self, country_code="IN", area=None, applicability_status=None, source_verification_status=None, subdivision_code=None):
        if country_code.upper() not in {item["country_code"] for item in list_jurisdictions()}:
            return None
        if country_code.upper() != "IN":
            return None
        if subdivision_code and not get_india_subnational_jurisdiction(subdivision_code):
            return None
        return list_rules(country_code, area, applicability_status, source_verification_status, subdivision_code)

    def get_compliance_rule(self, rule_id, country_code="IN", subdivision_code=None):
        if country_code.upper() != "IN":
            return None
        if subdivision_code and not get_india_subnational_jurisdiction(subdivision_code):
            return None
        return get_rule(rule_id, country_code, subdivision_code)

    def get_requirement(self, requirement_id, country_code="IN"):
        if country_code.upper() != "IN":
            return None
        return get_india_requirement(requirement_id)
