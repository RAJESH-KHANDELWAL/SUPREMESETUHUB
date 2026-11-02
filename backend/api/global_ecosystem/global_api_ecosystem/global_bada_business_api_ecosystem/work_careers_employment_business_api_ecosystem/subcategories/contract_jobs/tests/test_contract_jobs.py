import unittest
from ..categories import list_tracks,get_track,search_tracks,validate_tracks
class ContractJobTests(unittest.TestCase):
 def test_integrity(self): self.assertEqual(len(list_tracks()),5); self.assertTrue(validate_tracks()["structurally_valid"])
 def test_lookup(self): self.assertIsNotNone(get_track("fixed_term_employee_roles")); self.assertTrue(search_tracks("Fixed-Term")); self.assertIsNone(get_track("missing"))
if __name__=="__main__": unittest.main()
