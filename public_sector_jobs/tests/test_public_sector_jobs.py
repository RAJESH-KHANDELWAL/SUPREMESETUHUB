import unittest
from ..categories import list_tracks, get_track, search_tracks, validate_tracks
class PublicSectorJobsTests(unittest.TestCase):
    def test_track_integrity(self):
        self.assertEqual(len(list_tracks()), 8)
        self.assertTrue(validate_tracks()["structurally_valid"])
    def test_lookup_and_search(self):
        self.assertIsNotNone(get_track("central_public_sector_enterprises"))
        self.assertTrue(search_tracks("banking"))
        self.assertIsNone(get_track("missing"))
if __name__ == "__main__": unittest.main()
