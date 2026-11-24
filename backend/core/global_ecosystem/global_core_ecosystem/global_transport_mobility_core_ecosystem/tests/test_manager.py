import unittest
from ..manager import get_manager
from ..orchestrator import TransportMobilityCoreOrchestrator

class TestTransportMobilityCore(unittest.TestCase):
    def test_status_is_catalog_only(self):
        status = get_manager().status()
        self.assertTrue(status["success"])
        self.assertEqual(status["status"], "CORE_CATALOG_ONLY")
        self.assertFalse(status["live_connection_verified"])
    def test_catalog_ids_are_unique(self):
        ids = [x["id"] for x in get_manager().list_entries()["entries"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreater(len(ids), 0)
    def test_discovery(self):
        result = TransportMobilityCoreOrchestrator().discover("rail")
        self.assertTrue(result["entries"])
        self.assertTrue(all("rail" in x["name"].casefold() or "rail" in x["id"].casefold() or "rail" in x["description"].casefold() for x in result["entries"]))

if __name__ == "__main__": unittest.main()
