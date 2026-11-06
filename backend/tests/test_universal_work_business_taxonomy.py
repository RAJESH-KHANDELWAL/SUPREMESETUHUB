import unittest
from fastapi import FastAPI
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.routes import router as ecosystem_router
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_universal_work_business_taxonomy_api_ecosystem.catalog import list_sectors, validate_catalogue, get_facets

class UniversalWorkBusinessTaxonomyTests(unittest.TestCase):
    def test_catalogue_has_26_unique_a_to_z_codes(self):
        result = validate_catalogue()
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["sector_count"], 26)

    def test_restricted_sector_is_excluded_by_default(self):
        ids = {item["id"] for item in list_sectors()}
        self.assertNotIn("adult_sexual_wellness_restricted", ids)

    def test_audience_and_work_model_facets(self):
        facets = get_facets()
        self.assertIn("students", facets["audience_groups"])
        self.assertIn("homemakers", facets["audience_groups"])
        self.assertIn("couples", facets["audience_groups"])
        self.assertIn("freelance", facets["work_models"])
        self.assertIn("online", facets["delivery_modes"])

    def test_taxonomy_routes_are_mounted(self):
        app = FastAPI()
        app.include_router(ecosystem_router)
        paths = set(app.openapi()["paths"])
        self.assertIn("/api/v1/global-ecosystem/business/work-business-taxonomy/sectors", paths)
        self.assertIn("/api/v1/global-ecosystem/business/work-business-taxonomy/facets", paths)
        self.assertIn("/api/v1/global-ecosystem/business/work-business-taxonomy/integrity", paths)

if __name__ == "__main__":
    unittest.main()
