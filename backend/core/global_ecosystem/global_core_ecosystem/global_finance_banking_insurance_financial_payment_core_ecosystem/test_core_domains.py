"""Integrity tests for the finance ecosystem catalogue."""

import unittest

from .domain_catalog import DOMAIN_NAMES, DOMAIN_PACKAGES
from .manager import FinanceEcosystemManager


class FinanceCoreDomainTests(unittest.TestCase):
    def test_every_domain_has_a_name_and_packages(self):
        self.assertEqual(set(DOMAIN_NAMES), set(DOMAIN_PACKAGES))
        self.assertTrue(all(DOMAIN_PACKAGES.values()))

    def test_package_names_are_unique(self):
        packages = [
            package
            for package_list in DOMAIN_PACKAGES.values()
            for package in package_list
        ]
        self.assertEqual(len(packages), len(set(packages)))

    def test_manager_finds_registered_packages(self):
        manager = FinanceEcosystemManager()
        for package in manager.list_packages():
            self.assertIsNotNone(manager.find_package(package))

    def test_unknown_package_is_not_resolved(self):
        self.assertIsNone(FinanceEcosystemManager().find_package("not_a_real_package"))


if __name__ == "__main__":
    unittest.main()
