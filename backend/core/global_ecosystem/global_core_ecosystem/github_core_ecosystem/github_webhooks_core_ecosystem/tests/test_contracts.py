import unittest
from ..contracts import validate_request
class ContractTests(unittest.TestCase):
 def test_valid_contract(self):
  r=validate_request({"operation":"inspect","resource_id":"sample"}); self.assertTrue(r["accepted"]); self.assertEqual(r["family"],"webhooks"); self.assertFalse(r["live_call"])
 def test_nested_secret_rejected(self):
  with self.assertRaises(ValueError): validate_request({"metadata":{"access_token":"x"}})
 def test_unknown_key_rejected(self):
  with self.assertRaises(ValueError): validate_request({"unexpected":True})
if __name__=="__main__": unittest.main()
