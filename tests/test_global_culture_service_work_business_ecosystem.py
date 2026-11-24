import tempfile
import unittest
from pathlib import Path

from backend.ai.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_ai_ecosystem.assistant import GlobalCultureServiceWorkBusinessAI
from backend.core.global_ecosystem.global_core_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_core_ecosystem.service import GlobalCultureServiceWorkBusinessCore
from backend.database.global_ecosystem.global_database_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_database_ecosystem.repository import GlobalCultureServiceWorkBusinessRepository
from backend.database.service import DatabaseService
from backend.engine.global_ecosystem.global_engine_ecosystem.global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_engine_ecosystem.manager import GlobalCultureServiceWorkBusinessEngine

class CultureServiceWorkBusinessLayerTests(unittest.TestCase):
    def test_catalogue_covers_service_work_and_business(self):
        items=GlobalCultureServiceWorkBusinessCore().catalogue()
        self.assertEqual({item["domain"] for item in items},{"SERVICE","WORK","BUSINESS"})
        self.assertGreaterEqual(len(items),10)
    def test_engine_ranks_artisan_and_craft_results(self):
        result=GlobalCultureServiceWorkBusinessEngine().search("artisan pottery")
        self.assertGreater(result["count"],0)
        self.assertEqual(result["results"][0]["id"],"arts_crafts_design")
    def test_ai_context_is_grounded_and_does_not_claim_live_jobs(self):
        context=GlobalCultureServiceWorkBusinessAI(GlobalCultureServiceWorkBusinessEngine()).build_context("cultural education")
        self.assertEqual(context["provider_invocation"],"NOT_PERFORMED")
        self.assertFalse(context["retrieval"]["live_jobs_or_gigs"])
    def test_repository_persists_and_filters_approved_records(self):
        with tempfile.TemporaryDirectory() as directory:
            repository=GlobalCultureServiceWorkBusinessRepository(DatabaseService(db_path=str(Path(directory)/"records.db")))
            repository.save({"record_id":"test-cultural-service-001","capability_id":"cultural_education","record_type":"SERVICE_PROVIDER","title":"Community Cultural Learning Centre","description":"A test record for cultural learning services.","status":"APPROVED","metadata":{"test":True}})
            self.assertEqual(repository.get("test-cultural-service-001")["status"],"APPROVED")
            self.assertEqual(len(repository.search("Community")),1)

if __name__=="__main__": unittest.main()
