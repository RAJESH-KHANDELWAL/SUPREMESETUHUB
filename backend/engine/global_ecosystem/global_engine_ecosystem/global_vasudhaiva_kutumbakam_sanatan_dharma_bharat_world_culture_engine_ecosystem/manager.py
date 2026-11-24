"""Coordinates CORE, domain catalogues and persistence-backed discovery."""
from __future__ import annotations
from typing import Any
from backend.core.global_ecosystem.global_core_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_core_ecosystem.service import GlobalCulturalCore
from .discovery import normalize_query

class GlobalCulturalEngine:
    def __init__(self, core: GlobalCulturalCore | None = None) -> None:
        self.core = core or GlobalCulturalCore()

    def search(self, query: str, domain: str | None = None) -> dict[str, Any]:
        needle = normalize_query(query)
        if not needle:
            raise ValueError("CULTURAL_SEARCH_QUERY_REQUIRED")
        domains = self.core.domains()
        known = {item["id"] for item in domains}
        if domain and domain not in known:
            raise KeyError(f"CULTURAL_DOMAIN_NOT_FOUND:{domain}")
        selected = [item for item in domains if domain is None or item["id"] == domain]
        matches = []
        for item in selected:
            package = __import__("backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem", fromlist=["CULTURAL_DOMAINS"]).CULTURAL_DOMAINS[item["id"]]
            search_fn = getattr(package, "search_knowledge", None)
            if callable(search_fn):
                for record in search_fn(needle):
                    matches.append({"domain": item["id"], "record": record})
            else:
                records = getattr(package, "KNOWLEDGE_RECORDS", ())
                for record in records:
                    text = " ".join(str(v) for v in record.values()) if isinstance(record, dict) else str(record)
                    if needle.casefold() in text.casefold():
                        matches.append({"domain": item["id"], "record": record})
        return {"query": needle, "domains_searched": [item["id"] for item in selected],
                "domain_matches": matches, "foundational_matches": self.core.search_foundation(needle),
                "content_status": "MATCHES_FOUND" if matches else "PARTIAL_CORPUS_NO_DOMAIN_MATCH"}

    def status(self) -> dict[str, Any]:
        return {"name": "GLOBAL_CULTURAL_KNOWLEDGE_ENGINE", "status": "READY",
                "registered_domain_count": len(self.core.domains()),
                "capabilities": ["DOMAIN_DISCOVERY", "FOUNDATIONAL_SEARCH", "EVIDENCE_AWARE_ROUTING"],
                "corpus_status": "IN_PROGRESS"}
