"""Offline tests for DATABASE-owned server inventory."""
import unittest
from .models import ServerInventoryRecord
from .server_inventory_repository import ServerInventoryRepository
from .service import GlobalDatabaseEcosystemService

def record(server_id="node-1"):
    return ServerInventoryRecord(server_id, "Node", "aws", "vps", "app", "IN", "ap-south-1", "test")

class DatabaseServerInventoryTests(unittest.TestCase):
    def test_create_list_get_and_copy_isolation(self):
        repo=ServerInventoryRepository()
        created=repo.create(record())
        created["metadata"]["mutate"]=True
        self.assertIsNone(repo.get("missing"))
        self.assertNotIn("mutate", repo.get("node-1")["metadata"])
        self.assertEqual(len(repo.list()),1)

    def test_duplicate_and_update_allowlist(self):
        repo=ServerInventoryRepository()
        repo.create(record())
        with self.assertRaises(ValueError): repo.create(record())
        with self.assertRaises(ValueError): repo.update("node-1", password="secret")
        updated=repo.update("node-1", status="ACTIVE")
        self.assertEqual(updated["status"],"ACTIVE")

    def test_service_inventory_contract(self):
        service=GlobalDatabaseEcosystemService()
        result=service.create_server_inventory(record("node-2"))
        self.assertTrue(result["success"])
        self.assertEqual(service.describe()["server_inventory_count"],1)
        self.assertTrue(service.list_server_inventory()["success"])

if __name__=="__main__": unittest.main()
