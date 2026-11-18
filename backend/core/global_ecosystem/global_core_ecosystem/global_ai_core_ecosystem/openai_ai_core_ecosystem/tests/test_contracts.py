import unittest
from ..contracts import validate_request
class FacadeTests(unittest.TestCase):
 def test_provider_contract(self):
  x=validate_request({"provider_id":"openai","task":"hello"}); self.assertEqual(x["provider_id"],"openai"); self.assertFalse(x["execution_performed"])
 def test_mismatch_rejected(self):
  with self.assertRaises(ValueError): validate_request({"provider_id":"different","task":"hello"})
if __name__=="__main__": unittest.main()
