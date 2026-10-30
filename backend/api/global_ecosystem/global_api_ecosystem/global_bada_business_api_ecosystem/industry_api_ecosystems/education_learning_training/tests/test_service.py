"""Tests for EducationLearningService."""
import unittest

from education_learning_training.service import EducationLearningService

class EducationLearningServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = EducationLearningService()

    def test_catalog_has_expected_categories(self):
        items = self.service.list_categories()
        self.assertGreaterEqual(len(items), 12)
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

    def test_unknown_category(self):
        self.assertIsNone(self.service.get_category("not_a_real_category"))

    def test_status(self):
        status = self.service.get_status()
        self.assertEqual(status["domain_id"], "education_learning_training")
        self.assertEqual(status["category_count"], len(self.service.list_categories()))

if __name__ == "__main__":
    unittest.main()
