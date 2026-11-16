import unittest
from pathlib import Path
import re

from backend.core.global_ecosystem.global_core_ecosystem.global_domain_core_ecosystem.catalog import (
    CATEGORIES, PROVIDERS, get_domain_provider, list_domain_providers,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_domain_core_ecosystem.policy import (
    DomainCorePolicyError, classify_operation, reject_secret_material, require_metadata_only,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_domain_core_ecosystem.service import GlobalDomainCoreService


class GlobalDomainCoreContractTests(unittest.TestCase):
    def test_catalog_contains_71_unique_provider_ids(self):
        ids = [item["id"] for item in PROVIDERS]
        self.assertEqual(len(ids), 71)
        self.assertEqual(len(ids), len(set(ids)))

    def test_catalog_contains_seven_domain_categories(self):
        self.assertEqual(len(CATEGORIES), 7)

    def test_provider_lookup_is_case_insensitive_and_copy_safe(self):
        provider = get_domain_provider("CLOUDFLARE")
        self.assertEqual(provider["id"], "cloudflare")
        provider["name"] = "mutated"
        self.assertNotEqual(get_domain_provider("cloudflare")["name"], "mutated")

    def test_every_provider_is_catalog_only(self):
        for provider in list_domain_providers():
            self.assertEqual(provider["status"], "CORE_CATALOG_ONLY")
            self.assertFalse(provider["live_connection_verified"])
            self.assertIsNone(provider["api_available"])

    def test_mutating_domain_operations_fail_closed(self):
        self.assertIn("MUTATING_", classify_operation("UPDATE_DNS"))
        with self.assertRaises(DomainCorePolicyError):
            require_metadata_only("UPDATE_DNS")

    def test_metadata_only_operation_is_not_executed(self):
        result = GlobalDomainCoreService().plan_metadata_operation(
            provider_id="cloudflare", operation="READ_PROVIDER_METADATA"
        )
        self.assertTrue(result["accepted"])
        self.assertFalse(result["execution_performed"])

    def test_unknown_provider_is_rejected(self):
        with self.assertRaises(LookupError):
            GlobalDomainCoreService().readiness("unknown-provider")

    def test_php_auth_context_contract_classes_are_unique_and_well_formed(self):
        root = Path(__file__).resolve().parents[1]
        class_names = []
        for path in root.glob("*_domain_core_ecosystem/authentication/contract.php"):
            source = path.read_text(encoding="utf-8")
            namespace = source.split("namespace ", 1)[1].split(";", 1)[0]
            self.assertNotIn("\\\\", namespace)
            match = re.search(r"final class (\w+)", source)
            self.assertIsNotNone(match, path)
            class_names.append(match.group(1))
        self.assertEqual(len(class_names), 71)
        self.assertEqual(len(class_names), len(set(class_names)))

    def test_nested_secret_material_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "SECRET_MATERIAL_FORBIDDEN_IN_DOMAIN_CORE"):
            reject_secret_material({"metadata": [{"private-key": "not-allowed"}]})


if __name__ == "__main__":
    unittest.main()
