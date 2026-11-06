"""Tests for EducationLearningService."""
import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_education_learning_training_api_ecosystem.education_learning_training.service import EducationLearningService

class EducationLearningServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = EducationLearningService()

    def test_catalog_has_expected_categories(self):
        items = self.service.list_categories()
        self.assertEqual(len(items), 19)
        self.assertEqual(len({item["id"] for item in items}), len(items))
        self.assertTrue(all(item["id"] and item["subcategories"] for item in items))

    def test_search_is_case_insensitive(self):
        items = self.service.list_categories(query="UNIVERSITY")
        self.assertTrue(any(item["id"] == "higher_education" for item in items))

    def test_search_matches_subcategory(self):
        items = self.service.list_categories(query="spoken english")
        self.assertTrue(any(item["id"] == "language_and_communication_learning" for item in items))

    def test_get_category(self):
        item = self.service.get_category("online_learning_and_edtech")
        self.assertEqual(item["name"], "Online Learning & EdTech")

    def test_new_learning_tracks(self):
        expected = {
            "ai_and_data_literacy_education",
            "digital_skills_freelancing_and_remote_work",
            "entrepreneurship_and_business_education",
            "digital_marketing_and_creator_economy_training",
        }
        self.assertTrue(expected.issubset({item["id"] for item in self.service.list_categories()}))
        self.assertTrue(self.service.list_categories(query="generative ai"))
        self.assertTrue(self.service.list_categories(query="micro credentials"))
        self.assertTrue(self.service.list_categories(query="portfolio evidence"))

    def test_cross_ecosystem_links(self):
        links = self.service.get_cross_ecosystem_links()
        self.assertIn("jobs_careers_employment", links)
        self.assertIn("students_education_skills_business_api_ecosystem", links)
        self.assertEqual(self.service.get_status()["cross_ecosystem_link_count"], len(links))

    def test_unknown_category(self):
        self.assertIsNone(self.service.get_category("not_a_real_category"))

    def test_status(self):
        status = self.service.get_status()
        self.assertEqual(status["domain_id"], "education_learning_training")
        self.assertEqual(status["category_count"], len(self.service.list_categories()))

if __name__ == "__main__":
    unittest.main()
