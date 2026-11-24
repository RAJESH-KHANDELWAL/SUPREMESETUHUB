"""ENGINE orchestration for discovery across the cultural knowledge ecosystem."""
from __future__ import annotations
from typing import Any
from backend.core.global_ecosystem.global_core_ecosystem.cultural_knowledge_core_ecosystem.service import CulturalKnowledgeCoreService
from backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem import CULTURAL_DOMAINS

class CulturalKnowledgeEngineManager:
    """Coordinates domain search and core knowledge without owning API or storage."""
    def __init__(self, core: CulturalKnowledgeCoreService | None = None) -> None:
        self.core = core or CulturalKnowledgeCoreService()

    def search(self, query: str, domain: str | None = None) -> dict[str, Any]:
        needle = str(query or "").strip()
        if not needle:
            raise ValueError("CULTURAL_SEARCH_QUERY_REQUIRED")
        if domain and domain not in CULTURAL_DOMAINS:
            raise KeyError(f"CULTURAL_DOMAIN_NOT_FOUND:{domain}")
        foundational = self.core.search(needle)
        domain_result: list[dict[str, Any]] = []
        selected = {domain: CULTURAL_DOMAINS[domain]} if domain else CULTURAL_DOMAINS
        for domain_id, package in selected.items():
            # Rich domains may expose a dedicated knowledge index; use it first.
            knowledge_search = getattr(package, "search_knowledge", None)
            if callable(knowledge_search):
                domain_result.extend(
                    {"domain": domain_id, "record": item}
                    for item in knowledge_search(needle)
                )
                continue
            # Taxonomy-only domains still expose a validated record search
            # contract. They return no fabricated records when no corpus is loaded.
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
            "domains_registered": len(CULTURAL_DOMAINS),
            "domains_with_dedicated_knowledge_index": [
                key for key, package in CULTURAL_DOMAINS.items()
                if callable(getattr(package, "search_knowledge", None))
            ],
            "capabilities": ["FOUNDATIONAL_KNOWLEDGE_SEARCH", "DOMAIN_DISCOVERY"],
            "corpus_completeness": "IN_PROGRESS",
        }
