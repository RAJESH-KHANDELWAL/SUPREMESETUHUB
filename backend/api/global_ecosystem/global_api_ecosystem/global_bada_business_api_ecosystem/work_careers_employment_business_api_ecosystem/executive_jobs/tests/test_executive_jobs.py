import unittest
from ..categories import list_tracks,get_track,search_tracks,validate_tracks
class ExecutiveJobsTests(unittest.TestCase):
 def test_integrity(self): self.assertEqual(len(list_tracks()),5); self.assertTrue(validate_tracks()["structurally_valid"])
 def test_lookup(self): self.assertIsNotNone(get_track("c_suite_roles")); self.assertTrue(search_tracks("director")); self.assertIsNone(get_track("missing"))
if __name__=="__main__": unittest.main()
