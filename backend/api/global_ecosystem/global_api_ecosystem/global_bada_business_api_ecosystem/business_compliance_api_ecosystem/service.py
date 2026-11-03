from .catalog import list_india_requirements, get_india_requirement, list_jurisdictions

class BusinessComplianceService:
    ECOSYSTEM_ID = "business_compliance_api_ecosystem"

    def get_status(self):
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "status": "compliance_discovery_scaffold",
            "jurisdictions": list_jurisdictions(),
            "india_requirement_topics": len(list_india_requirements()),
            "coverage_note": "India has a starter topic catalogue. Other jurisdictions are framework-only; no country-specific legal checklist is implied.",
            "legal_safety": "Applicability depends on entity, activity, product, turnover, premises, employees, transaction and location. Verify current requirements with official authorities or qualified professionals."
        }

    def list_jurisdictions(self):
        return list_jurisdictions()

    def list_requirements(self, country_code="IN", query=None, area=None):
        if country_code.upper() != "IN":
            return None
        items = list_india_requirements()
        if area:
            items = [x for x in items if x["area"] == area]
        if query:
            q = query.strip().casefold()
            items = [x for x in items if q in x["id"].casefold() or q in x["name"].casefold() or any(q in v.casefold() for v in x["examples"] + x["applies_to"])]
        return items

    def get_requirement(self, requirement_id, country_code="IN"):
        if country_code.upper() != "IN":
            return None
        return get_india_requirement(requirement_id)
