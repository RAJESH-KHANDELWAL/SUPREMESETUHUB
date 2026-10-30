"""Read-only taxonomy discovery service."""

from .catalog import DOMAINS, FACETS


class PeopleLifeService:
    ecosystem_id = "global-people-life"

    @staticmethod
    def _visible(include_adult: bool) -> list[dict]:
        return [d for d in DOMAINS if include_adult or not d.get("adult_only")]

    def list_domains(self, include_adult: bool = False) -> dict:
        domains = self._visible(include_adult)
        return {"success": True, "ecosystem_id": self.ecosystem_id,
                "count": len(domains), "domains": domains, "facets": FACETS}

    def get_domain(self, domain_id: str, include_adult: bool = False):
        return next((d for d in self._visible(include_adult) if d["id"] == domain_id), None)

    def search_domains(self, query: str, include_adult: bool = False) -> list[dict]:
        term = query.strip().casefold()
        if not term:
            return []
        return [d for d in self._visible(include_adult)
                if term in (d["id"] + " " + d["name"] + " " + " ".join(d["groups"])).casefold()]
