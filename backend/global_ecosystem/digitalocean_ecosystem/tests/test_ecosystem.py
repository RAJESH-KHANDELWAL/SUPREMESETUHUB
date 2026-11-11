import unittest

from backend.global_ecosystem.digitalocean_ecosystem.catalog import (
    list_capabilities, get_capability, search_capabilities,
)
from backend.global_ecosystem.digitalocean_ecosystem.models import OperationRequest
from backend.global_ecosystem.digitalocean_ecosystem.service import plan_operation, readiness
from backend.global_ecosystem.digitalocean_ecosystem.validation import validate_request
from backend.global_ecosystem.digitalocean_ecosystem.adapters.digitalocean_api import adapter_status


class DigitalOceanCatalogTests(unittest.TestCase):
    def test_catalog_has_compute_storage_networking(self):
        categories = {item["category"] for item in list_capabilities()}
        self.assertTrue({"compute", "storage", "networking"}.issubset(categories))

    def test_catalog_lookup_and_search(self):
        self.assertEqual(get_capability("droplets")["name"], "Droplets")
        self.assertTrue(search_capabilities("kubernetes"))

    def test_unknown_capability_is_rejected(self):
        errors = validate_request(OperationRequest("unknown", "list"))
        self.assertIn("unknown capability_id", errors)

    def test_destructive_action_requires_confirmation(self):
        request = OperationRequest("droplets", "delete")
        self.assertTrue(validate_request(request))
        confirmed = OperationRequest("droplets", "delete", confirmation=True)
        self.assertEqual(validate_request(confirmed), [])

    def test_plan_does_not_execute_provider_operation(self):
        result = plan_operation(OperationRequest("droplets", "list"))
        self.assertTrue(result["ready"])
        self.assertFalse(result["execution_performed"])

    def test_readiness_is_explicit_about_live_connection(self):
        state = readiness()
        self.assertTrue(state["catalog_loaded"])
        self.assertFalse(state["live_provider_connection_verified"])

    def test_adapter_contract_does_not_claim_live_connection(self):
        state = adapter_status()
        self.assertTrue(state["adapter_contract_available"])
        self.assertFalse(state["live_connection_verified"])


if __name__ == "__main__":
    unittest.main()
