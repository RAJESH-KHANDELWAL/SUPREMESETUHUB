import unittest

from .. import categories


class WorkCategoryTests(unittest.TestCase):
    """Validate dynamic category catalogues without freezing their folder count."""

    def test_integrity_matches_discovered_specializations(self):
        records = categories.list_tracks()
        result = categories.validate_tracks()

        self.assertTrue(records)
        self.assertEqual(result["track_count"], len(records))
        self.assertTrue(result["structurally_valid"], result)
        ids = [item["id"] for item in records]
        self.assertEqual(len(ids), len(set(ids)))
        for item in records:
            self.assertTrue(item.get("id"))
            self.assertTrue(item.get("name"))
            self.assertTrue(item.get("description"))

    def test_lookup_and_search_follow_discovered_ids(self):
        records = categories.list_tracks()
        first_id = records[0]["id"]

        self.assertIsNotNone(categories.get_track(first_id))
        self.assertTrue(categories.search_tracks(first_id))
        self.assertIsNone(categories.get_track("__missing_specialization__"))


if __name__ == "__main__":
    unittest.main()
