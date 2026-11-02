import importlib
import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.domain_registry import DOMAIN_REGISTRY

PACKAGE_ROOT = "backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem"


class DomainPackageLayerTests(unittest.TestCase):
    def test_all_twelve_domains_have_catalogue_model_and_service_layers(self):
        for domain in DOMAIN_REGISTRY:
            package = f"{PACKAGE_ROOT}.{domain['id']}_business_api_ecosystem"
            catalog = importlib.import_module(f"{package}.catalog")
            models = importlib.import_module(f"{package}.models")
            service_module = importlib.import_module(f"{package}.service")
            self.assertTrue(hasattr(models, "CategoryRecord"), domain["id"])
            self.assertTrue(hasattr(catalog, "list_categories"), domain["id"])
            self.assertTrue(hasattr(catalog, "get_category"), domain["id"])
            self.assertTrue(hasattr(service_module, "DomainService"), domain["id"])

    def test_catalogue_counts_match_central_registry(self):
        for domain in DOMAIN_REGISTRY:
            package = f"{PACKAGE_ROOT}.{domain['id']}_business_api_ecosystem"
            catalog = importlib.import_module(f"{package}.catalog")
            if domain["adult_only"]:
                self.assertEqual(catalog.list_categories(), [])
                self.assertEqual(len(catalog.list_categories(include_restricted=True)), domain["subcategory_count"])
            else:
                self.assertEqual(len(catalog.list_categories()), domain["subcategory_count"])

    def test_domain_service_exposes_status_and_category_search(self):
        package = f"{PACKAGE_ROOT}.freelance_gig_independent_work_business_api_ecosystem.service"
        service = importlib.import_module(package).DomainService()
        self.assertEqual(service.get_status()["domain_id"], "freelance_gig_independent_work")
        self.assertTrue(service.search("web_development"))
        self.assertIsNotNone(service.get_category("web_development"))


    def test_work_careers_catalogue_and_government_jobs_package(self):
        package = f"{PACKAGE_ROOT}.work_careers_employment_business_api_ecosystem"
        categories = importlib.import_module(f"{package}.categories")
        catalog = importlib.import_module(f"{package}.catalog")
        integrity = categories.validate_category_definitions()
        self.assertTrue(integrity["structurally_valid"], integrity)
        self.assertEqual(len(categories.CATEGORY_DEFINITIONS), 23)
        self.assertEqual(len(catalog.list_categories()), 23)
        self.assertTrue(all(item.description and item.search_terms for item in catalog.list_categories()))

        government_jobs = importlib.import_module(f"{package}.subcategories.government_jobs.categories")
        government_service = importlib.import_module(f"{package}.subcategories.government_jobs.services")
        government_integrity = government_jobs.validate_tracks()
        self.assertTrue(government_integrity["structurally_valid"], government_integrity)
        self.assertEqual(len(government_jobs.GOVERNMENT_JOB_TRACKS), 13)
        self.assertTrue(government_service.search_government_job_tracks("civilian"))

        from fastapi import FastAPI
        global_routes = importlib.import_module(f"{PACKAGE_ROOT}.routes").router
        app = FastAPI()
        app.include_router(global_routes)
        self.assertIn(
            "/api/v1/global-ecosystem/business/work-careers/government-jobs/status",
            app.openapi()["paths"],
        )

if __name__ == "__main__":
    unittest.main()
