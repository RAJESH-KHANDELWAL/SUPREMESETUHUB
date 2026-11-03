"""Tests for Jobs, Careers & Employment taxonomy and service."""
import unittest

from ..service import JobsCareersService


class JobsCareersServiceTests(unittest.TestCase):
    def test_catalog_has_unique_ids_and_categories(self):
        service = JobsCareersService()
        items = service.list_categories()
        ids = [item["id"] for item in items]
        self.assertEqual(len(items), 15)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(item["name"] and item["subcategories"] for item in items))

    def test_search_and_detail(self):
        service = JobsCareersService()
        first = service.list_categories()[0]
        self.assertEqual(service.get_category(first["id"])["id"], first["id"])
        self.assertTrue(service.list_categories(query=first["id"]))
        self.assertIsNone(service.get_category("not_a_real_category"))

    def test_status_is_explicit_about_scaffold(self):
        service = JobsCareersService()
        status = service.get_status()
        self.assertEqual(status["status"], "taxonomy_scaffold")
        self.assertEqual(status["category_count"], len(service.list_categories()))

    def test_employment_taxonomy_bridge_exposes_job_categories(self):
        service = JobsCareersService()
        items = service.list_employment_categories()
        ids = {item["id"] for item in items}
        self.assertEqual(len(items), 24)
        self.assertTrue({"government_jobs", "private_sector_jobs", "corporate_jobs", "public_sector_jobs"} <= ids)
        self.assertTrue(all(item["taxonomy_status"] == "taxonomy_only" for item in items))

    def test_employment_taxonomy_search_and_detail(self):
        service = JobsCareersService()
        results = service.list_employment_categories(query="government")
        self.assertTrue(any(item["id"] == "government_jobs" for item in results))
        self.assertEqual(service.get_employment_category("private_sector_jobs")["id"], "private_sector_jobs")
        self.assertIsNone(service.get_employment_category("not_a_real_category"))


if __name__ == "__main__":
    unittest.main()
