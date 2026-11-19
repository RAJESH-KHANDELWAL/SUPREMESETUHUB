"""Coverage tests for the cultural knowledge ENGINE domain search contract."""
from types import SimpleNamespace

from backend.engine.global_ecosystem.global_engine_ecosystem.cultural_knowledge_engine_ecosystem import (
    CulturalKnowledgeEngineManager,
)
from backend.global_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_ecosystem import (
    CULTURAL_DOMAINS,
)


def test_registered_domains_are_not_misreported_as_searched():
    manager = CulturalKnowledgeEngineManager(domains=CULTURAL_DOMAINS)

    status = manager.status()
    result = manager.search("Maha Upanishad")

    assert status["domains_registered"] == 13
    assert status["domains_searchable"] == 1
    assert len(status["domains_without_search_index"]) == 12
    assert result["domain_count_searched"] == 1
    assert result["domain_count_skipped"] == 12
    assert result["domains_searched"] == ["sanatan_dharma"]


def test_search_records_uses_real_domain_records():
    package = SimpleNamespace(
        KNOWLEDGE_RECORDS=[{"title": "Maha Upanishad"}],
        search_records=lambda records, query: [
            item for item in records if query.casefold() in item["title"].casefold()
        ],
    )
    manager = CulturalKnowledgeEngineManager(domains={"texts": package})

    result = manager.search("upanishad")

    assert result["domain_count_searched"] == 1
    assert result["domain_matches"] == [
        {"domain": "texts", "record": {"title": "Maha Upanishad"}}
    ]


def test_unindexed_domain_is_reported_as_skipped_not_searched():
    manager = CulturalKnowledgeEngineManager(domains={"empty_domain": object()})

    result = manager.search("anything", domain="empty_domain")

    assert result["domain_count_searched"] == 0
    assert result["domain_count_skipped"] == 1
    assert result["domains_skipped"] == ["empty_domain"]
