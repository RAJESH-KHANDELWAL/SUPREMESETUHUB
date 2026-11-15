import unittest
from ..ecosystem_service import EcosystemService
from ..ecosystem_taxonomy import load_taxonomy
from ..ecosystem_models import CloudStorageRecord


class CloudStorageFoundationTests(unittest.TestCase):
    def test_safe_readiness(self):
        state = EcosystemService().describe()
        self.assertEqual(state["connection_state"], "NOT_CONFIGURED")
        self.assertFalse(state["external_connections_verified"])
        self.assertFalse(state["storage_operations_enabled"])

    def test_taxonomy_has_unique_groups(self):
        taxonomy = load_taxonomy()
        ids = [item["group_id"] for item in taxonomy["groups"]]
        self.assertEqual(len(ids), len(set(ids)))

    def test_record_defaults_to_unconfigured(self):
        record = CloudStorageRecord("r1", "AWS", "OBJECT_STORAGE", "Example")
        self.assertEqual(record.connection_state, "NOT_CONFIGURED")

    def test_connection_cannot_be_asserted_by_metadata_record(self):
        with self.assertRaises(ValueError):
            CloudStorageRecord("r2", "AWS", "OBJECT_STORAGE", "Example", connection_state="CONNECTED")


if __name__ == "__main__":
    unittest.main()
