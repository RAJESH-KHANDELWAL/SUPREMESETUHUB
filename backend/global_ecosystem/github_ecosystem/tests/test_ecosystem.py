import unittest
from backend.global_ecosystem.github_ecosystem.catalog import list_capabilities, get_capability, search_capabilities
from backend.global_ecosystem.github_ecosystem.models import OperationRequest
from backend.global_ecosystem.github_ecosystem.service import plan_operation, readiness
from backend.global_ecosystem.github_ecosystem.validation import validate_request
from backend.global_ecosystem.github_ecosystem.adapters.github_api import adapter_status
from backend.global_ecosystem.github_ecosystem.governance import governance_profile
from backend.global_ecosystem.github_ecosystem.health import health

class GitHubCatalogTests(unittest.TestCase):
    def test_catalog_covers_core_domains(self):
        categories = {x["category"] for x in list_capabilities()}
        self.assertTrue({"source_control", "collaboration", "automation", "security"}.issubset(categories))
    def test_catalog_lookup_and_search(self):
        self.assertEqual(get_capability("repositories")["name"], "Repositories")
        self.assertTrue(search_capabilities("pull request"))
    def test_unknown_capability_is_rejected(self):
        self.assertIn("unknown capability_id", validate_request(OperationRequest("unknown", "list")))
    def test_write_action_requires_confirmation(self):
        req = OperationRequest("repositories", "delete", owner="acme", repository="demo")
        self.assertTrue(validate_request(req))
        approved = OperationRequest("repositories", "delete", owner="acme", repository="demo", confirmation=True)
        self.assertEqual(validate_request(approved), [])
    def test_owner_validation(self):
        errors = validate_request(OperationRequest("repositories", "get", owner="org/name"))
        self.assertIn("owner must be a single GitHub account or organization name", errors)
    def test_plan_is_non_executing(self):
        result = plan_operation(OperationRequest("repositories", "list"))
        self.assertTrue(result["ready"])
        self.assertFalse(result["execution_performed"])
    def test_local_readiness_and_health(self):
        self.assertFalse(readiness()["live_provider_connection_verified"])
        self.assertFalse(health()["network_probe_performed"])
    def test_adapter_and_governance_contracts(self):
        self.assertFalse(adapter_status()["live_connection_verified"])
        self.assertIn("least-privilege GitHub App permissions", governance_profile()["controls"])

if __name__ == "__main__":
    unittest.main()
