"""Runtime regression tests for all mounted Company profile adapters."""
import importlib
import unittest

PACKAGE = (
    "backend.api.global_ecosystem.global_api_ecosystem."
    "global_company_companies_api_ecosystem.global_companies_ecosystem"
)

class TestCompanyProfileAdapters(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = importlib.import_module(f"{PACKAGE}.routes")
        cls.company_ids = cls.registry.COMPANY_ADAPTER_IDS

    def test_all_26_company_packages_load(self):
        self.assertEqual(len(self.company_ids), 26)
        self.assertEqual(len(set(self.company_ids)), 26)
        for company_id in self.company_ids:
            with self.subTest(company_id=company_id):
                package = importlib.import_module(f"{PACKAGE}.{company_id}")
                self.assertTrue(callable(package.get_profile))
                self.assertTrue(callable(package.get_sources))
                self.assertTrue(callable(package.get_adapter_status))

    def test_each_profile_has_explicit_source_and_verification_state(self):
        for company_id in self.company_ids:
            with self.subTest(company_id=company_id):
                package = importlib.import_module(f"{PACKAGE}.{company_id}")
                profile = package.get_profile()
                self.assertEqual(profile["company_id"], company_id)
                self.assertEqual(profile["record_type"], "company")
                self.assertEqual(profile["profile_status"], "source_registered_unverified")
                self.assertIn(
                    profile["data_status"],
                    {"no_verified_profile_record", "no_verified_legal_entity_record"},
                )
                self.assertGreaterEqual(len(profile["sources"]), 1)
                self.assertFalse(profile["sources"][0]["live_connection"])

    def test_each_adapter_exposes_profile_source_and_status_routes(self):
        for company_id in self.company_ids:
            with self.subTest(company_id=company_id):
                package = importlib.import_module(f"{PACKAGE}.{company_id}")
                paths = {route.path for route in package.router.routes}
                base = f"/global/company-profile-adapters/{company_id}"
                self.assertIn(base, paths)
                self.assertIn(f"{base}/sources", paths)
                self.assertIn(f"{base}/status", paths)

    def test_no_adapter_claims_live_external_connectivity(self):
        for company_id in self.company_ids:
            with self.subTest(company_id=company_id):
                package = importlib.import_module(f"{PACKAGE}.{company_id}")
                status = package.get_adapter_status()
                self.assertFalse(status["live_connection"])
                self.assertEqual(status["status"], "not_connected")

if __name__ == "__main__":
    unittest.main()
