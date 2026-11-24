"""ENGINE orchestration for the global cultural knowledge ecosystem."""
from __future__ import annotations

from typing import Any

from backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem import (
    CULTURAL_DOMAINS,
    search_knowledge,
)
from .discovery import normalize_query


class _CulturalKnowledgePort:
    """Read-only domain-layer port; ENGINE does not import CORE implementation."""

    def domains(self) -> list[dict[str, str]]:
        return [
            {"id": domain_id, "name": domain_id.replace("_", " ").title()}
            for domain_id in CULTURAL_DOMAINS
        ]

    def search_foundation(self, query: str) -> list[dict[str, Any]]:
        return search_knowledge(query)


class GlobalCulturalEngine:
    def __init__(self, core: Any | None = None) -> None:
        self.core = core or _CulturalKnowledgePort()

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
            package = CULTURAL_DOMAINS[item["id"]]
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
        return {
            "query": needle,
            "domains_searched": [item["id"] for item in selected],
            "domain_matches": matches,
            "foundational_matches": self.core.search_foundation(needle),
            "content_status": "MATCHES_FOUND" if matches else "PARTIAL_CORPUS_NO_DOMAIN_MATCH",
        }

    def status(self) -> dict[str, Any]:
        return {
            "name": "GLOBAL_CULTURAL_KNOWLEDGE_ENGINE",
            "status": "READY",
            "registered_domain_count": len(self.core.domains()),
            "capabilities": ["DOMAIN_DISCOVERY", "FOUNDATIONAL_SEARCH", "EVIDENCE_AWARE_ROUTING"],
            "corpus_status": "IN_PROGRESS",
        }


__all__ = ["GlobalCulturalEngine"]
