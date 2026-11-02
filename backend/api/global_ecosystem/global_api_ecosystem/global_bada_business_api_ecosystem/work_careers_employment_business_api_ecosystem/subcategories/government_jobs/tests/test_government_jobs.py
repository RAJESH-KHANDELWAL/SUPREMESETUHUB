import unittest

from ..categories import get_track, list_tracks, validate_tracks
from ..services import search_government_job_tracks
from ..validators import validate_notice_record

class GovernmentJobsTaxonomyTests(unittest.TestCase):
    def test_track_ids_are_unique(self):
        tracks = list_tracks()
        ids = [item["id"] for item in tracks]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(tracks), 13)

    def test_track_lookup(self):
        self.assertIsNotNone(get_track("central_government_recruitment"))
        self.assertIsNone(get_track("not_a_track"))

    def test_search_uses_track_description_and_roles(self):
        self.assertTrue(search_government_job_tracks("civilian"))
        self.assertTrue(search_government_job_tracks("engineering"))

    def test_track_integrity(self):
        self.assertTrue(validate_tracks()["structurally_valid"])

    def test_notice_validator_rejects_missing_provenance(self):
        result = validate_notice_record({})
        self.assertFalse(result["valid"])
        self.assertTrue(result["missing_fields"])
        self.assertFalse(result["authenticity_verified"])

    def test_notice_validator_only_checks_structure(self):
        record = {
            "notice_id": "sample-1",
            "title": "Sample recruitment notice",
            "issuing_authority": "Example Authority",
            "jurisdiction": "Example jurisdiction",
            "official_notice_url": "https://example.gov/notice",
            "notice_or_advertisement_id": "ADV-001",
            "publication_date": "2026-01-01",
            "last_verified_at": "2026-01-02T00:00:00Z",
            "verification_status": "source_checked",
        }
        result = validate_notice_record(record)
        self.assertTrue(result["valid"])
        self.assertFalse(result["authenticity_verified"])

if __name__ == "__main__":
    unittest.main()
