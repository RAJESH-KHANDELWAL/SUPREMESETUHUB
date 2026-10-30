"""Read-only discovery service for the cross-domain people and life taxonomy."""

from .people_life_catalog import CROSS_CUTTING_FACETS, PEOPLE_LIFE_DOMAINS


class PeopleLifeEcosystemService:
    ECOSYSTEM_ID = "global-people-work-life"
    VERSION = "1.0.0"

    def list_domains(self, include_adult: bool = False):
        items = [
            item for item in PEOPLE_LIFE_DOMAINS
            if include_adult or not item.get("adult_only")
        ]
        return {
            "success": True,
            "ecosystem_id": self.ECOSYSTEM_ID,
            "count": len(items),
            "domains": items,
            "facets": CROSS_CUTTING_FACETS,
        }

    def get_domain(self, domain_id: str, include_adult: bool = False):
        for item in PEOPLE_LIFE_DOMAINS:
            if item["id"] == domain_id and (include_adult or not item.get("adult_only")):
                return item
        return None

    def search_domains(self, query: str, include_adult: bool = False):
        needle = query.strip().casefold()
        if not needle:
            return []
        results = []
        for item in PEOPLE_LIFE_DOMAINS:
            if item.get("adult_only") and not include_adult:
                continue
            searchable = " ".join([item["id"], item["name"], *item["subcategories"]]).casefold()
            if needle in searchable:
                results.append(item)
        return results
