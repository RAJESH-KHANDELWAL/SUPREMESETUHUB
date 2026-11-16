"""Tests for the global namespace facade and scope taxonomy."""
import unittest

from backend.global_ecosystem.global_ai_ecosystem import (
    AI_MATURITY_LEVELS,
    AI_SCOPE_DOMAINS,
    GlobalAIEcosystemService,
    get_catalog,
    get_scope_catalog,
)


class GlobalAINamespaceTests(unittest.TestCase):
    def test_namespace_exposes_canonical_ai_catalog(self):
        catalog = get_catalog()
        self.assertIn("providers", catalog)
        self.assertIn("capabilities", catalog)
        self.assertIn("governance", catalog)

    def test_service_is_the_canonical_ai_service(self):
        self.assertIsInstance(GlobalAIEcosystemService(), GlobalAIEcosystemService)
        self.assertFalse(GlobalAIEcosystemService().status()["runtime_enabled"])

    def test_scope_includes_bharat_and_global_domains(self):
        ids = {item["id"] for item in AI_SCOPE_DOMAINS}
        self.assertIn("bharat_india_ai", ids)
        self.assertIn("global_world_ai", ids)

    def test_supreme_intelligence_is_not_claimed_as_implemented(self):
        item = next(x for x in AI_MATURITY_LEVELS if x["id"] == "supreme_intelligence")
        self.assertEqual(item["status"], "LONG_TERM_RESEARCH_ONLY")

    def test_adult_platform_scope_has_explicit_safeguards(self):
        item = next(x for x in AI_SCOPE_DOMAINS if x["id"] == "lawful_adult_content_ai")
        self.assertIn("adults_only", item["safeguards"])
        self.assertIn("no_nonconsensual_intimate_imagery", item["safeguards"])

    def test_scope_catalog_is_defensive(self):
        catalog = get_scope_catalog()
        catalog["domains"].clear()
        self.assertTrue(get_scope_catalog()["domains"])


if __name__ == "__main__":
    unittest.main()
