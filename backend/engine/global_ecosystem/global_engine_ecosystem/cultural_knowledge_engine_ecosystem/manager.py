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

    @staticmethod
    def _domain_search(package: Any):
        """Return a real search callable, never an empty-record placeholder."""
        search_knowledge = getattr(package, "search_knowledge", None)
        if callable(search_knowledge):
            return lambda query: search_knowledge(query)

        search_records = getattr(package, "search_records", None)
        records = getattr(package, "KNOWLEDGE_RECORDS", None)
        if records is None:
            records = getattr(package, "RECORDS", None)
        if callable(search_records) and records is not None:
            return lambda query: search_records(records, query)
        return None

    def search(self, query: str, domain: str | None = None) -> dict[str, Any]:
        needle = str(query or "").strip()
        if not needle:
            raise ValueError("CULTURAL_SEARCH_QUERY_REQUIRED")
        if domain and domain not in self.domains:
            raise KeyError(f"CULTURAL_DOMAIN_NOT_FOUND:{domain}")

        foundational = self.core.search(needle) if self.core is not None else []
        selected = {domain: self.domains[domain]} if domain else self.domains
        domain_result: list[dict[str, Any]] = []
        searched_domains: list[str] = []
        skipped_domains: list[str] = []

        for domain_id, package in selected.items():
            search_fn = self._domain_search(package)
            if search_fn is None:
                skipped_domains.append(domain_id)
                continue
            searched_domains.append(domain_id)
            domain_result.extend(
                {"domain": domain_id, "record": item}
                for item in search_fn(needle)
            )

        return {
            "query": needle,
            "foundational_matches": foundational,
            "domain_matches": domain_result,
            "domain_count_searched": len(searched_domains),
            "domains_searched": searched_domains,
            "domain_count_skipped": len(skipped_domains),
            "domains_skipped": skipped_domains,
            "content_status": (
                "PARTIAL_CORPUS"
                if domain_result or foundational
                else "NO_MATCH_OR_UNINDEXED_DOMAIN"
            ),
        }

    def status(self) -> dict[str, Any]:
        searchable_domains = [
            key for key, package in self.domains.items()
            if self._domain_search(package) is not None
        ]
        return {
            "engine": "CULTURAL_KNOWLEDGE_ENGINE",
            "status": "READY",
            "domains_registered": len(self.domains),
            "domains_searchable": len(searchable_domains),
            "domains_without_search_index": [
                key for key in self.domains if key not in searchable_domains
            ],
            "domains_with_dedicated_knowledge_index": [
                key for key, package in self.domains.items()
                if callable(getattr(package, "search_knowledge", None))
            ],
            "core_search_configured": self.core is not None,
            "capabilities": ["FOUNDATIONAL_KNOWLEDGE_SEARCH", "DOMAIN_DISCOVERY"],
            "corpus_completeness": "IN_PROGRESS",
        }
