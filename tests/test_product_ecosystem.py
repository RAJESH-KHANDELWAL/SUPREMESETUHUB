"""Tests for the relationship-first product map and closed adult gates."""
import unittest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.api.product_ecosystem import router

app = FastAPI()
app.include_router(router)
client = TestClient(app)


class ProductEcosystemTests(unittest.TestCase):
    def test_combined_journey_is_relationship_first(self):
        data = client.get("/api/v1/products/catalog").json()
        self.assertEqual(data["combined_journey"], ["relationship", "romance", "intimacy"])
        self.assertTrue(data["journey_is_optional"])
        self.assertTrue(data["standalone_access_supported"])
        self.assertTrue(data["consent_is_never_inferred"])

    def test_adult_product_is_not_published_before_gates(self):
        data = client.get("/api/v1/products/catalog").json()
        intimacy = next(item for item in data["products"] if item["product_id"] == "intimacy")
        self.assertEqual(intimacy["status"], "LOCKED_PENDING_COMPLIANCE")
        self.assertFalse(intimacy["public_catalog_enabled"])
        self.assertTrue(intimacy["age_gate_required"])
        self.assertTrue(intimacy["region_gate_required"])
        self.assertTrue(intimacy["performer_consent_and_distribution_rights_required"])

    def test_family_store_excludes_explicit_content(self):
        data = client.get("/api/v1/products/catalog").json()
        family = next(item for item in data["products"] if item["product_id"] == "family_safe_store")
        self.assertTrue(family["must_exclude_explicit_content"])

    def test_provider_connections_are_not_falsely_claimed(self):
        providers = client.get("/api/v1/products/provider-readiness").json()["providers"]
        by_id = {item["provider_id"]: item for item in providers}
        self.assertEqual(by_id["vicetemple"]["status"], "NOT_CONNECTED")
        self.assertEqual(by_id["faphouse"]["status"], "NOT_CONNECTED")


if __name__ == "__main__":
    unittest.main()
