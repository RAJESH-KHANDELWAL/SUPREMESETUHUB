"""Read-only taxonomy service for search, listing and category detail."""
from .catalog import CATEGORIES

class AdultWellnessEcosystemService:
    ECOSYSTEM_ID = "adult_sexual_wellness"

    def list_categories(self, *, coverage: str | None = None, query: str | None = None):
        items = list(CATEGORIES)
        if coverage:
            items = [x for x in items if coverage in x.coverage]
        if query:
            q = query.strip().casefold()
            items = [x for x in items if q in x.id.casefold() or q in x.name.casefold() or any(q in s.casefold() for s in x.subdomains)]
        return [self._serialize(x) for x in items]

    def get_category(self, category_id: str):
        for item in CATEGORIES:
            if item.id == category_id:
                return self._serialize(item)
        return None

    def get_status(self):
        return {"success": True, "ecosystem_id": self.ECOSYSTEM_ID, "status": "taxonomy_scaffold", "category_count": len(CATEGORIES), "coverage": ["india", "global"], "age_restriction": "18+", "live_provider_integrations": False}

    @staticmethod
    def _serialize(x):
        return {"id": x.id, "name": x.name, "folder": x.folder, "subdomains": list(x.subdomains), "coverage": list(x.coverage), "channels": list(x.channels), "age_restriction": x.age_restriction, "status": x.status}
