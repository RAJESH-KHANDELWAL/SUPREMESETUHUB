"""Unit tests using a small in-memory SQLite DatabaseService."""

import unittest
from backend.database.service import DatabaseService
from .repository import BadaBusinessProgramRepository
from .service import BadaBusinessProgramPersistenceService


class BadaBusinessProgramPersistenceTests(unittest.TestCase):
    def setUp(self):
        self.database = DatabaseService(":memory:")
        self.repository = BadaBusinessProgramRepository(self.database)
        self.service = BadaBusinessProgramPersistenceService(
            repository=self.repository,
            catalog_loader=lambda: [
                {"program_id": "lfp_digital", "name": "LFP Digital", "tagline": "Growth"}
            ],
        )

    def tearDown(self):
        self.database.close()

    def test_sync_canonical_snapshot(self):
        result = self.service.sync_canonical_catalog("owner-a")
        self.assertEqual(result["records_saved"], 1)
        self.assertEqual(result["data"][0]["program_id"], "lfp_digital")

    def test_owner_scope_isolation(self):
        self.service.sync_canonical_catalog("owner-a")
        self.assertIsNone(self.service.get_program("owner-b", "lfp_digital"))
        self.assertIsNotNone(self.service.get_program("owner-a", "lfp_digital"))

    def test_upsert_does_not_duplicate_owner_program_pair(self):
        self.service.sync_canonical_catalog("owner-a")
        self.service.save_snapshot("owner-a", {
            "program_id": "lfp_digital", "name": "LFP Digital Updated"
        })
        records = self.service.list_programs("owner-a")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["program_name"], "LFP Digital Updated")

    def test_delete_is_owner_scoped(self):
        self.service.sync_canonical_catalog("owner-a")
        self.assertFalse(self.service.delete_program("owner-b", "lfp_digital"))
        self.assertTrue(self.service.delete_program("owner-a", "lfp_digital"))

    def test_limit_validation(self):
        with self.assertRaises(ValueError):
            self.service.list_programs("owner-a", limit=0)


if __name__ == "__main__":
    unittest.main()
