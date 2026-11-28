"""Coordinates cultural-domain discovery without importing the CORE layer."""
from __future__ import annotations
from typing import Any
from backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem import CULTURAL_DOMAINS
from backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem.service import CulturalKnowledgeDomainService
from .discovery import normalize_query

class GlobalCulturalEngine:
    def __init__(self, domain_service: CulturalKnowledgeDomainService | None = None, *, core: Any = None) -> None:
        # The legacy injection keyword remains supported without a CORE import.
        self.core = domain_service or core or CulturalKnowledgeDomainService()

    def search(self, query: str, domain: str | None = None) -> dict[str, Any]:
        needle = normalize_query(query)
        if not needle:
            raise ValueError("CULTURAL_SEARCH_QUERY_REQUIRED")
        known = set(CULTURAL_DOMAINS)
        if domain and domain not in known:
            raise KeyError(f"CULTURAL_DOMAIN_NOT_FOUND:{domain}")
        selected = [key for key in CULTURAL_DOMAINS if domain is None or key == domain]
        matches = []
        for domain_id in selected:
            package = CULTURAL_DOMAINS[domain_id]
            search_fn = getattr(package, "search_knowledge", None)
            if callable(search_fn):
                for record in search_fn(needle):
                    matches.append({"domain": domain_id, "record": record})
            else:
                records = getattr(package, "KNOWLEDGE_RECORDS", ())
                for record in records:
                    value = " ".join(str(v) for v in record.values()) if isinstance(record, dict) else str(record)
                    if needle.casefold() in value.casefold():
                        matches.append({"domain": domain_id, "record": record})
        foundation = self.core.search(needle)
        return {"query": needle, "domains_searched": selected, "domain_matches": matches,
                "foundational_matches": foundation,
                "content_status": "MATCHES_FOUND" if matches or foundation else "PARTIAL_CORPUS_NO_DOMAIN_MATCH"}

    def status(self) -> dict[str, Any]:
        return {"name": "GLOBAL_CULTURAL_KNOWLEDGE_ENGINE", "status": "READY",
                "registered_domain_count": len(CULTURAL_DOMAINS),
                "capabilities": ["DOMAIN_DISCOVERY", "FOUNDATIONAL_SEARCH", "EVIDENCE_AWARE_ROUTING"],
                "corpus_status": "IN_PROGRESS"}
