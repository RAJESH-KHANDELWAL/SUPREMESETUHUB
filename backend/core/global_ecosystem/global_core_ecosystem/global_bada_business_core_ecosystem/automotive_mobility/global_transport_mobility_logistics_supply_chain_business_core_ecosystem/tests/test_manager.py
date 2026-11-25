import unittest
from ..manager import get_manager
from ..orchestrator import TransportBusinessCoreOrchestrator

class TestTransportBusinessCore(unittest.TestCase):
    def test_status_is_catalog_only(self):
        status = get_manager().status()
        self.assertTrue(status["success"])
        self.assertEqual(status["status"], "CORE_CATALOG_ONLY")
        self.assertFalse(status["live_connection_verified"])
    def test_catalog_ids_are_unique(self):
        ids = [x["id"] for x in get_manager().list_entries()["entries"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(ids), 15)
    def test_discovery(self):
        result = TransportBusinessCoreOrchestrator().discover("supply chain")
        self.assertEqual(result["count"], 1)
        self.assertEqual(result["entries"][0]["id"], "SUPPLY_CHAIN_BUSINESS")

if __name__ == "__main__": unittest.main()
