from backend.core.global_ecosystem.global_core_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_core_ecosystem.service import GlobalCultureServiceWorkBusinessCore
from backend.engine.global_ecosystem.global_engine_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_engine_ecosystem.manager import GlobalCultureServiceWorkBusinessEngine
from backend.ai.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_ai_ecosystem.assistant import GlobalCultureServiceWorkBusinessAI
from backend.database.global_ecosystem.global_database_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_database_ecosystem.repository import GlobalCultureServiceWorkBusinessRepository
from backend.database.service import DatabaseService

def test_catalogue_has_service_work_and_business_domains():
    core = GlobalCultureServiceWorkBusinessCore()
    assert {item["domain"] for item in core.catalogue()} == {"SERVICE", "WORK", "BUSINESS"}
    assert len(core.catalogue()) >= 10

def test_engine_finds_cultural_artisan_capabilities():
    engine = GlobalCultureServiceWorkBusinessEngine()
    result = engine.search("artisan pottery")
    assert result["count"] > 0
    assert result["results"][0]["id"] == "arts_crafts_design"

def test_ai_context_is_retrieval_grounded_and_does_not_claim_live_jobs():
    engine = GlobalCultureServiceWorkBusinessEngine()
    ai = GlobalCultureServiceWorkBusinessAI(engine)
    context = ai.build_context("cultural education")
    assert context["provider_invocation"] == "NOT_PERFORMED"
    assert context["retrieval"]["live_jobs_or_gigs"] is False

def test_repository_only_returns_approved_records(tmp_path):
    repository = GlobalCultureServiceWorkBusinessRepository(
        DatabaseService(db_path=str(tmp_path / "culture-work-business.db"))
    )
    repository.save({
        "record_id": "test-cultural-service-001",
        "capability_id": "cultural_education",
        "record_type": "SERVICE_PROVIDER",
        "title": "Community Cultural Learning Centre",
        "description": "A test record for cultural learning services.",
        "status": "APPROVED",
        "metadata": {"test": True},
    })
    assert repository.get("test-cultural-service-001")["status"] == "APPROVED"
    assert len(repository.search("Community")) == 1
