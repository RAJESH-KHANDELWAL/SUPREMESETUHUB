import unittest

from backend.global_ecosystem.cohere_ecosystem import CohereEcosystemService
from backend.global_ecosystem.cohere_ecosystem.catalog import COHERE_PRODUCTS, list_capabilities
from backend.global_ecosystem.cohere_ecosystem.health import readiness_report

class CohereEcosystemTests(unittest.TestCase):
    def setUp(self):
        self.service = CohereEcosystemService()

    def test_catalog_covers_six_product_areas(self):
        self.assertEqual(len(COHERE_PRODUCTS), 6)
        self.assertIn("command", COHERE_PRODUCTS)
        self.assertIn("rerank", COHERE_PRODUCTS)

    def test_capability_filter(self):
        rows = list_capabilities("embed")
        self.assertTrue(rows)
        self.assertTrue(all(row["product_id"] == "embed" for row in rows))

    def test_catalog_does_not_claim_live_connection(self):
        report = readiness_report()
        self.assertEqual(report["status"], "CATALOG_ONLY")
        self.assertFalse(report["live_connection_verified"])

    def test_command_plan_requires_input(self):
        with self.assertRaises(ValueError):
            self.service.plan("command", "chat", {})
        plan = self.service.plan("command", "chat", {"message": "hello"})
        self.assertEqual(plan.product_id, "command")
        self.assertEqual(plan.metadata["transport_owned_by"], "API")

    def test_embed_plan_requires_content(self):
        with self.assertRaises(ValueError):
            self.service.plan("embed", "embed", {})
        plan = self.service.plan("embed", "embed", {"texts": ["hello"]})
        self.assertEqual(plan.product_id, "embed")

    def test_rerank_plan_requires_query_and_documents(self):
        with self.assertRaises(ValueError):
            self.service.plan("rerank", "rerank", {"query": "hello"})
        plan = self.service.plan("rerank", "rerank", {"query": "hello", "documents": ["a", "b"]})
        self.assertEqual(plan.product_id, "rerank")

    def test_unknown_product_rejected(self):
        with self.assertRaises(KeyError):
            self.service.plan("unknown", "infer", {"prompt": "hello"})

    def test_inline_credentials_rejected(self):
        with self.assertRaises(ValueError):
            self.service.plan("command", "chat", {"message": "hi", "api_key": "not-allowed"})

if __name__ == "__main__":
    unittest.main()
