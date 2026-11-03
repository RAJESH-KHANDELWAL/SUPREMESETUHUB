"""Ensure every canonical Jobs & Careers industry category/subcategory has its own package."""
import importlib
import unittest

from ..catalog import list_categories


DOMAIN_PACKAGE = __package__.rsplit(".", 1)[0]


class JobsCareersIndustryPackageTests(unittest.TestCase):
    def test_every_category_and_subcategory_has_independent_package(self):
        categories = list_categories()
        self.assertEqual(len(categories), 15)
        subcategory_total = 0
        for item in categories:
            category_id = item["id"]
            category = importlib.import_module(f"{DOMAIN_PACKAGE}.{category_id}")
            self.assertEqual(category.CATEGORY_ID, category_id)
            self.assertTrue(category.get_category_status()["success"])

            category_routes = importlib.import_module(
                f"{DOMAIN_PACKAGE}.{category_id}.routes"
            ).router
            self.assertGreaterEqual(len(category_routes.routes), 4)

            expected_subcategories = set(item["subcategories"])
            discovered = set()
            for subcategory_id in expected_subcategories:
                package = importlib.import_module(
                    f"{DOMAIN_PACKAGE}.{category_id}.{subcategory_id}"
                )
                self.assertEqual(package.SUBCATEGORY_ID, subcategory_id)
                self.assertEqual(package.CATEGORY_ID, category_id)
                self.assertTrue(package.get_subcategory_status()["success"])
                child_router = importlib.import_module(
                    f"{DOMAIN_PACKAGE}.{category_id}.{subcategory_id}.routes"
                ).router
                self.assertTrue(child_router.routes)
                discovered.add(subcategory_id)

            self.assertEqual(discovered, expected_subcategories)
            subcategory_total += len(expected_subcategories)

        self.assertEqual(subcategory_total, 60)

    def test_main_jobs_router_mounts_all_category_routers(self):
        router = importlib.import_module(f"{DOMAIN_PACKAGE}.routes").router
        paths = {route.path for route in router.routes}
        for item in list_categories():
            self.assertIn(
                f"/jobs-careers-employment/categories/{item['id']}/package",
                paths,
            )


if __name__ == "__main__":
    unittest.main()
