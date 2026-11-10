import unittest

from .capabilities import list_ai_capability_groups, list_ai_modalities


class CapabilityCatalogTests(unittest.TestCase):
    def test_modality_ids_are_unique(self):
        ids = [item["id"] for item in list_ai_modalities()]
        self.assertEqual(len(ids), len(set(ids)))

    def test_groups_reference_known_modalities(self):
        known = {item["id"] for item in list_ai_modalities()}
        for group in list_ai_capability_groups():
            self.assertTrue(set(group["modalities"]).issubset(known))


if __name__ == "__main__":
    unittest.main()
