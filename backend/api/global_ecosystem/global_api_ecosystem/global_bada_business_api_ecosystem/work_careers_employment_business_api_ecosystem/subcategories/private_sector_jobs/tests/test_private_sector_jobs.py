import unittest
from ..categories import list_tracks, get_track, search_tracks, validate_tracks

class PrivateJobsTests(unittest.TestCase):
    def test_tracks_integrity(self):
        self.assertEqual(len(list_tracks()), 8)
        self.assertTrue(validate_tracks()["structurally_valid"])

    def test_lookup_and_search(self):
        self.assertIsNotNone(get_track("private_companies"))
        self.assertTrue(search_tracks("startup"))
        self.assertIsNone(get_track("missing"))

if __name__ == "__main__":
    unittest.main()
