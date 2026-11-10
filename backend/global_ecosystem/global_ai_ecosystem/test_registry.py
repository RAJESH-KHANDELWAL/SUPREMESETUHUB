import unittest

from .providers import list_ai_providers, validate_provider_registry


class ProviderRegistryTests(unittest.TestCase):
    def test_registry_contains_all_catalogued_entries(self):
        providers = list_ai_providers()
        self.assertGreaterEqual(len(providers), 49)
        self.assertEqual(len({item["id"] for item in providers}), len(providers))

    def test_registry_metadata_is_consistent(self):
        self.assertEqual(validate_provider_registry(), ())

    def test_returned_records_are_defensive_copies(self):
        first = list_ai_providers()
        first[0]["name"] = "mutated"
        second = list_ai_providers()
        self.assertNotEqual(second[0]["name"], "mutated")


if __name__ == "__main__":
    unittest.main()
