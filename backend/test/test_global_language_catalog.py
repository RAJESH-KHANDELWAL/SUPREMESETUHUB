"""Tests for language and adult-language catalog services."""
import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_language_api_ecosystem.language_catalog import (
    WORLD_LANGUAGES, LOCALES, list_languages, list_locales, get_language_summary,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_language_api_ecosystem.adult_language_catalog import (
    ADULT_LANGUAGE_DOMAINS, list_adult_language_domains, get_adult_language_summary,
)


class TestGlobalLanguageCatalog(unittest.TestCase):
    def test_catalogs_have_entries(self):
        self.assertGreaterEqual(len(WORLD_LANGUAGES), 100)
        self.assertGreaterEqual(len(LOCALES), 40)
        self.assertGreaterEqual(len(ADULT_LANGUAGE_DOMAINS), 10)

    def test_language_filter_is_case_insensitive(self):
        self.assertEqual(list_languages("HINDI")[0]["id"], "hi")
        self.assertEqual(list_languages("japanese")[0]["id"], "ja")

    def test_language_limit_is_bounded(self):
        self.assertEqual(len(list_languages(limit=1)), 1)
        self.assertLessEqual(len(list_languages(limit=9999)), 500)

    def test_locale_filter(self):
        self.assertTrue(all(item["language"] == "hi" for item in list_locales("hi")))
        self.assertTrue(any(item["id"] == "en-IN" for item in list_locales("en")))

    def test_adult_domains_are_educational_and_non_graphic(self):
        ids = {item["id"] for item in list_adult_language_domains()}
        self.assertIn("consent_and_boundaries", ids)
        self.assertIn("sexual_health_education", ids)
        self.assertIn("privacy_and_digital_safety", ids)

    def test_summaries_disclose_catalog_only_status(self):
        self.assertEqual(get_language_summary()["provider_status"], "CATALOG_ONLY")
        self.assertFalse(get_language_summary()["live_translation_available"])
        self.assertEqual(get_adult_language_summary()["provider_status"], "CATALOG_ONLY")


if __name__ == "__main__":
    unittest.main()
