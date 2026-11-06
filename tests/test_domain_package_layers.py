import importlib
import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.domain_registry import DOMAIN_REGISTRY

PACKAGE_ROOT = "backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem"


class DomainPackageLayerTests(unittest.TestCase):
    def test_all_twelve_domains_have_catalogue_model_and_service_layers(self):
        for domain in DOMAIN_REGISTRY:
            package_id = {"work_careers_employment": "global_freelancer_gig_independent_work_business_api_ecosystem.jobs_careers_employment_api_ecosystem", "freelance_gig_independent_work": "global_freelancer_gig_independent_work_business_api_ecosystem", "students_education_skills": "global_education_learning_training_api_ecosystem.students_education_skills_business_api_ecosystem", "business_companies_corporates": "business_companies_corporates_business_api_ecosystem"}.get(domain["id"], f"{domain['id']}_business_api_ecosystem")
            package = f"{PACKAGE_ROOT}.{package_id}"
            if domain["id"] == "business_companies_corporates":
                company_root = "backend.api.global_ecosystem.global_api_ecosystem.global_company_companies_api_ecosystem"
                catalog = importlib.import_module(f"{company_root}.business_catalog")
                models = importlib.import_module(f"{company_root}.business_enterprises_api_ecosystem.models")
                service_module = importlib.import_module(f"{company_root}.business_enterprises_api_ecosystem.service")
                self.assertTrue(hasattr(models, "BusinessDirectoryProfile"), domain["id"])
                self.assertTrue(hasattr(catalog, "SUBCATEGORIES"), domain["id"])
                self.assertTrue(hasattr(service_module, "list_profiles"), domain["id"])
                self.assertTrue(hasattr(service_module, "get_catalog"), domain["id"])
            else:
                catalog = importlib.import_module(f"{package}.catalog")
                models = importlib.import_module(f"{package}.models")
                service_module = importlib.import_module(f"{package}.service")
                self.assertTrue(hasattr(models, "CategoryRecord"), domain["id"])
                self.assertTrue(hasattr(catalog, "list_categories"), domain["id"])
                self.assertTrue(hasattr(catalog, "get_category"), domain["id"])
                self.assertTrue(hasattr(service_module, "DomainService"), domain["id"])

    def test_catalogue_counts_match_central_registry(self):
        for domain in DOMAIN_REGISTRY:
            package_id = {"work_careers_employment": "global_freelancer_gig_independent_work_business_api_ecosystem.jobs_careers_employment_api_ecosystem", "freelance_gig_independent_work": "global_freelancer_gig_independent_work_business_api_ecosystem", "students_education_skills": "global_education_learning_training_api_ecosystem.students_education_skills_business_api_ecosystem"}.get(domain["id"], f"{domain['id']}_business_api_ecosystem")
            package = f"{PACKAGE_ROOT}.{package_id}"
            if domain["id"] == "business_companies_corporates":
                catalog = importlib.import_module("backend.api.global_ecosystem.global_api_ecosystem.global_company_companies_api_ecosystem.business_catalog")
                self.assertEqual(len(catalog.SUBCATEGORIES), domain["subcategory_count"])
                continue
            catalog = importlib.import_module(f"{package}.catalog")
            if domain["adult_only"]:
                self.assertEqual(catalog.list_categories(), [])
                self.assertEqual(len(catalog.list_categories(include_restricted=True)), domain["subcategory_count"])
            else:
                self.assertEqual(len(catalog.list_categories()), domain["subcategory_count"])

    def test_domain_service_exposes_status_and_category_search(self):
        package = f"{PACKAGE_ROOT}.global_freelancer_gig_independent_work_business_api_ecosystem.service"
        service = importlib.import_module(package).DomainService()
        self.assertEqual(service.get_status()["domain_id"], "freelance_gig_independent_work")
        self.assertTrue(service.search("web_development"))
        self.assertIsNotNone(service.get_category("web_development"))


    def test_work_careers_catalogue_and_government_jobs_package(self):
        package = f"{PACKAGE_ROOT}.global_freelancer_gig_independent_work_business_api_ecosystem.jobs_careers_employment_api_ecosystem"
        categories = importlib.import_module(f"{package}.categories")
        catalog = importlib.import_module(f"{package}.catalog")
        integrity = categories.validate_category_definitions()
        self.assertTrue(integrity["structurally_valid"], integrity)
        self.assertEqual(len(categories.CATEGORY_DEFINITIONS), 24)
        self.assertEqual(len(catalog.list_categories()), 24)
        self.assertTrue(all(item.description and item.search_terms for item in catalog.list_categories()))

        government_jobs = importlib.import_module(f"{package}.government_jobs.categories")
        government_service = importlib.import_module(f"{package}.government_jobs.services")
        government_integrity = government_jobs.validate_tracks()
        self.assertTrue(government_integrity["structurally_valid"], government_integrity)
        self.assertEqual(len(government_jobs.list_tracks()), 23)
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
