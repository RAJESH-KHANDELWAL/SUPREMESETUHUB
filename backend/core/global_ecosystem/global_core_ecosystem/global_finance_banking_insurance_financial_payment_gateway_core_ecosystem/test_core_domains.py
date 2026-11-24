"""Integrity tests for Global Finance Core domain and package registration."""
import unittest
from .catalog import FINANCE_ECOSYSTEM_CATALOG
from .domain_catalog import DOMAIN_DEFINITIONS, DOMAIN_PACKAGES, PACKAGE_TO_DOMAIN
from .manager import FinanceCoreManager
from .policy import FinanceCorePolicy, FinancePolicyError
from .product_catalog import FINANCE_PACKAGES
class FinanceCoreTests(unittest.TestCase):
    def test_domains_have_definitions_and_packages(self):
        self.assertEqual(set(DOMAIN_DEFINITIONS), set(DOMAIN_PACKAGES))
        self.assertTrue(all(DOMAIN_PACKAGES.values()))
    def test_package_assignments_are_unique(self):
        names = [n for group in DOMAIN_PACKAGES.values() for n in group]
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(set(names), set(PACKAGE_TO_DOMAIN))
    def test_product_catalog_matches_domain_catalog(self):
        self.assertEqual(len(FINANCE_PACKAGES), len(PACKAGE_TO_DOMAIN))
        self.assertEqual({x["package_name"] for x in FINANCE_PACKAGES}, set(PACKAGE_TO_DOMAIN))
    def test_manager_resolves_all_packages(self):
        manager = FinanceCoreManager()
        for name in PACKAGE_TO_DOMAIN: self.assertIsNotNone(manager.get_package(name))
    def test_unknown_package_is_not_resolved(self):
        self.assertIsNone(FinanceCoreManager().get_package("not_a_real_finance_package"))
    def test_catalogue_does_not_claim_live_execution(self):
        self.assertFalse(FINANCE_ECOSYSTEM_CATALOG["transaction_execution_enabled"])
        self.assertFalse(FINANCE_ECOSYSTEM_CATALOG["provider_connections_verified"])
    def test_policy_rejects_transaction_execution(self):
        with self.assertRaises(FinancePolicyError): FinanceCorePolicy.assert_catalogue_only("transfer")
if __name__ == "__main__": unittest.main()
