"""Contract tests for the metadata-only Global Database Core."""
import unittest

from backend.core.global_ecosystem.global_core_ecosystem.global_database_core_ecosystem.manager import (
    get_provider,
    list_providers,
    validate_catalog,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_database_core_ecosystem.orchestrator import (
    resolve_provider,
)


class DatabaseCoreContractTests(unittest.TestCase):
    def test_catalog_has_seven_unique_api_mirrored_providers(self):
        providers = list_providers()
        self.assertEqual(len(providers), 7)
        self.assertEqual(len({provider["provider_id"] for provider in providers}), 7)
        self.assertTrue(
            all(provider["implementation_status"] == "CATALOG_ONLY" for provider in providers)
        )
        self.assertTrue(
            all(provider["live_connection_verified"] is False for provider in providers)
        )

    def test_canonical_provider_packages_have_manifests(self):
        result = validate_catalog()
        self.assertTrue(result["valid"])
        self.assertEqual(result["missing_manifests"], [])

    def test_unknown_and_invalid_provider_ids_are_not_resolved(self):
        self.assertIsNone(get_provider("not-a-provider"))
        self.assertIsNone(get_provider(None))
        self.assertIsNone(get_provider(" "))
        self.assertFalse(resolve_provider("not-a-provider")["ready"])

    def test_known_provider_is_catalog_only_not_runtime_ready(self):
        result = resolve_provider("postgresql")
        self.assertFalse(result["ready"])
        self.assertEqual(result["reason"], "provider_not_registered")
        result = resolve_provider("aws")
        self.assertFalse(result["ready"])
        self.assertEqual(result["reason"], "catalog_only_no_runtime_adapter")
        self.assertFalse(result["live_connection_verified"])


if __name__ == "__main__":
    unittest.main()
