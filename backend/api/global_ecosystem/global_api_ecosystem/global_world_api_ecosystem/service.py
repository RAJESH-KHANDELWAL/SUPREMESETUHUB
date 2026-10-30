"""Read-only global taxonomy discovery service."""
from .catalog import DOMAINS, ECOSYSTEM_LINKS, FACETS


class GlobalWorldService:
    ecosystem_id = "global-world-a-z"
    version = "1.0.0"

    @staticmethod
    def _visible(include_adult: bool) -> list[dict]:
        return [item for item in DOMAINS if include_adult or not item.get("adult_only")]

    def status(self) -> dict:
        return {
            "success": True,
            "ecosystem": "SUPREMESETUHUB GLOBAL WORLD A-Z ECOSYSTEM",
            "ecosystem_id": self.ecosystem_id,
            "version": self.version,
            "status": "CATALOG_ONLY",
            "live_global_directory": False,
            "domain_count": len(DOMAINS),
            "adult_domains_separately_classified": sum(1 for item in DOMAINS if item.get("adult_only")),
            "provider_connections_verified": False,
            "note": "A taxonomy is not an exhaustive live registry. Provider listings, availability, legal eligibility and integrations require separate verification.",
        }

    def list_domains(self, include_adult: bool = False) -> dict:
        items = self._visible(include_adult)
        return {"success": True, "ecosystem_id": self.ecosystem_id, "count": len(items), "domains": items, "facets": FACETS, "ecosystems": list(ECOSYSTEM_LINKS)}

    def get_domain(self, domain_id: str, include_adult: bool = False):
        return next((item for item in self._visible(include_adult) if item["id"] == domain_id), None)

    def search_domains(self, query: str, include_adult: bool = False) -> list[dict]:
        term = query.strip().casefold()
        if not term:
            return []
        return [item for item in self._visible(include_adult) if term in (item["id"] + " " + item["name"] + " " + " ".join(item["groups"])).casefold()]
