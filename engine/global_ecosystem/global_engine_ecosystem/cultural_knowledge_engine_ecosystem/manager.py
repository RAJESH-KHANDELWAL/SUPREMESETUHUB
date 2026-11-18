"""ENGINE orchestration for discovery across the cultural knowledge ecosystem.

Concrete CORE services and domain packages are supplied by the composition root.
The ENGINE depends only on a neutral contract and standard-library abstractions.
"""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from backend.contracts.cultural_knowledge import CulturalKnowledgeSearch


class CulturalKnowledgeEngineManager:
    """Coordinates injected knowledge capabilities without owning CORE or taxonomy."""

    def __init__(
        self,
        core: CulturalKnowledgeSearch | None = None,
        domains: Mapping[str, Any] | None = None,
    ) -> None:
        self.core = core
        self.domains = dict(domains or {})

    def search(self, query: str, domain: str | None = None) -> dict[str, Any]:
        needle = str(query or "").strip()
        if not needle:
            raise ValueError("CULTURAL_SEARCH_QUERY_REQUIRED")
        if domain and domain not in self.domains:
            raise KeyError(f"CULTURAL_DOMAIN_NOT_FOUND:{domain}")

        foundational = self.core.search(needle) if self.core is not None else []
        domain_result: list[dict[str, Any]] = []
        selected = {domain: self.domains[domain]} if domain else self.domains
        for domain_id, package in selected.items():
            knowledge_search = getattr(package, "search_knowledge", None)
            if callable(knowledge_search):
                domain_result.extend(
                    {"domain": domain_id, "record": item}
                    for item in knowledge_search(needle)
                )
                continue
            search_fn = getattr(package, "search_records", None)
            if callable(search_fn):
                domain_result.extend(
                    {"domain": domain_id, "record": item}
                    for item in search_fn((), needle)
                )

        return {
            "query": needle,
            "foundational_matches": foundational,
            "domain_matches": domain_result,
            "domain_count_searched": len(selected),
            "content_status": "PARTIAL_CORPUS" if domain_result or foundational else "NO_MATCH",
        }

    def status(self) -> dict[str, Any]:
        return {
            "engine": "CULTURAL_KNOWLEDGE_ENGINE",
            "status": "READY",
            "domains_registered": len(self.domains),
            "domains_with_dedicated_knowledge_index": [
                key for key, package in self.domains.items()
                if callable(getattr(package, "search_knowledge", None))
            ],
            "core_search_configured": self.core is not None,
            "capabilities": ["FOUNDATIONAL_KNOWLEDGE_SEARCH", "DOMAIN_DISCOVERY"],
            "corpus_completeness": "IN_PROGRESS",
        }
