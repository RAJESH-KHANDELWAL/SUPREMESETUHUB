"""Integration contract tests for cultural knowledge platform layers."""
from backend.ai.cultural_knowledge_assistant import CulturalKnowledgeAssistant
from backend.core.global_ecosystem.global_core_ecosystem.cultural_knowledge_core_ecosystem import CulturalKnowledgeCoreService
from backend.engine.global_ecosystem.global_engine_ecosystem.cultural_knowledge_engine_ecosystem import CulturalKnowledgeEngineManager
from backend.database.cultural_knowledge_repository import CulturalKnowledgeRepository
from backend.database.service import DatabaseService
from backend.cloud.global_ecosystem.global_cloud_ecosystem.cultural_knowledge_cloud_ecosystem import CulturalKnowledgeCloudBridge


def test_core_and_engine_are_connected():
    core = CulturalKnowledgeCoreService()
    engine = CulturalKnowledgeEngineManager(core=core)
    assert core.describe()["ecosystem_id"].startswith("GLOBAL_VASUDHAIVA")
    result = engine.search("Maha Upanishad")
    assert result["foundational_matches"]
    assert result["domain_count_searched"] == 13


def test_ai_builds_grounded_context_without_claiming_provider_call():
    context = CulturalKnowledgeAssistant().build_context("Vasudhaiva Kutumbakam")
    assert context["provider_invocation"] == "NOT_PERFORMED"
    assert context["answering_rules"]


def test_database_repository_only_returns_approved_records(tmp_path):
    repository = CulturalKnowledgeRepository(DatabaseService(str(tmp_path / "culture.db")))
    repository.save({
        "record_id": "TEST-001", "domain_id": "sanatan_dharma",
        "title": "Test text", "content": "Maha Upanishad reference",
        "source_kind": "primary_text", "confidence": "medium",
        "publication_status": "APPROVED",
    })
    assert repository.get("TEST-001")["title"] == "Test text"
    assert len(repository.search("Upanishad")) == 1
    assert repository.search("Upanishad", domain_id="world_cultures") == []


def test_cloud_bridge_requires_explicit_adapter():
    bridge = CulturalKnowledgeCloudBridge()
    assert bridge.status()["status"] == "NOT_CONFIGURED"
