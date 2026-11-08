"""Unit tests for the independent DATABASE ecosystem manager."""
import unittest

from .manager import GlobalDatabaseEcosystemManager
from .models import DatabaseEcosystemIdentity


class TestGlobalDatabaseEcosystemManager(unittest.TestCase):
    def setUp(self):
        self.manager = GlobalDatabaseEcosystemManager()

    def test_root_and_status(self):
        status = self.manager.status()
        self.assertTrue(status["success"])
        self.assertEqual(status["layer"], "DATABASE")
        self.assertEqual(status["ecosystem_id"], "GLOBAL-DATABASE-ECOSYSTEM")
        self.assertGreater(status["count"], 1)

    def test_health_does_not_claim_live_database_connection(self):
        health = self.manager.health()
        self.assertTrue(health["success"])
        self.assertFalse(health["database_connections_verified"])
        self.assertFalse(health["migrations_verified"])

    def test_hierarchy_tree_and_connection_map(self):
        tree = self.manager.tree()
        graph = self.manager.connection_map()
        self.assertTrue(tree["success"])
        self.assertEqual(tree["tree"]["ecosystem_id"], self.manager.ROOT_ID)
        self.assertEqual(graph["node_count"], self.manager.registry.count())
        self.assertEqual(graph["edge_count"], graph["node_count"] - 1)

    def test_lookup_by_id_and_name(self):
        self.assertIsNotNone(self.manager.get("GLOBAL-AWS-DATABASE-ECOSYSTEM"))
        self.assertIsNotNone(self.manager.get("GLOBAL AWS DATABASE ECOSYSTEM"))
        self.assertTrue(self.manager.exists(self.manager.ROOT_ID))

    def test_register_child_and_reject_duplicate(self):
        item = DatabaseEcosystemIdentity(
            ecosystem_id="TEST-DATABASE-NODE", name="Test Database Node",
            parent_id=self.manager.ROOT_ID,
        )
        self.assertTrue(self.manager.register(item)["success"])
        self.assertEqual(self.manager.register(item)["error"], "ECOSYSTEM_ALREADY_EXISTS")


if __name__ == "__main__":
    unittest.main()
