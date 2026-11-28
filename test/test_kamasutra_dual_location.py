import importlib
import unittest

from fastapi import FastAPI

GLOBAL_ROOT = "backend.api.global_ecosystem.global_api_ecosystem.global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem"
BUSINESS_ROOT = "backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem"


class KamasutraDualLocationTests(unittest.TestCase):
    def test_both_packages_exist_with_same_folder_basename(self):
        global_package = importlib.import_module(GLOBAL_ROOT)
        business_package = importlib.import_module(BUSINESS_ROOT)
        self.assertTrue(hasattr(global_package, "router"))
        self.assertTrue(hasattr(business_package, "router"))
        self.assertEqual(global_package.router.prefix, business_package.router.prefix)

    def test_global_router_is_mounted(self):
        parent = importlib.import_module("backend.api.global_api_ecosystem_routes").router
        app = FastAPI()
        app.include_router(parent)
        self.assertIn(
            "/api/v1/global-api-ecosystem/adult-wellness/status",
            app.openapi()["paths"],
        )

    def test_bada_business_router_is_mounted_from_local_copy(self):
        parent = importlib.import_module(
            "backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.routes"
        ).router
        app = FastAPI()
        app.include_router(parent)
        self.assertIn(
            "/api/v1/global-ecosystem/business/kamasutra/adult-wellness/status",
            app.openapi()["paths"],
        )

    def test_bada_business_registry_uses_local_copy(self):
        registry = importlib.import_module(
            "backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.domain_registry"
        )
        adult = registry.get_domain("adult_18_plus_lawful_industry", include_adult=True)
        self.assertIsNotNone(adult)
        local_module = importlib.import_module(
            BUSINESS_ROOT + ".adult_18_plus_lawful_industry_domain"
        )
        self.assertTrue(hasattr(local_module, "DOMAIN_ID"))


if __name__ == "__main__":
    unittest.main()
