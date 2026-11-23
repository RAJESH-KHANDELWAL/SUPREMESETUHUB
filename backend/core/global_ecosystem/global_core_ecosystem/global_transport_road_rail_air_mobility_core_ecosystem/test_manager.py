import unittest

from .catalog import get_transport_mode, list_transport_modes
from .manager import get_manager


class GlobalTransportMobilityCoreTests(unittest.TestCase):
    def test_catalog_has_distinct_transport_modes(self):
        modes = list_transport_modes()
        self.assertEqual(len(modes), 5)
        self.assertEqual(len({item["id"] for item in modes}), 5)

    def test_mode_lookup_is_case_insensitive(self):
        self.assertEqual(get_transport_mode("ROAD_TRANSPORT")["id"], "road_transport")
        self.assertIsNone(get_transport_mode("unknown"))

    def test_manager_is_metadata_only(self):
        status = get_manager().status()
        self.assertEqual(status["status"], "CORE_CATALOG_ONLY")
        self.assertFalse(status["live_transport_operations_verified"])
        self.assertEqual(get_manager().list_modes()["count"], 5)


if __name__ == "__main__":
    unittest.main()
