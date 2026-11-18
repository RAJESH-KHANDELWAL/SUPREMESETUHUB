import unittest
from ..contracts import validate_request
class CapabilityContractTests(unittest.TestCase):
 def test_rejects_non_mapping(self):
  with self.assertRaises(ValueError): validate_request(None)
 def test_rejects_secret_field(self):
  payload={"input":"hello","metadata":{"api_key":"x"}}
  with self.assertRaises(ValueError): validate_request(payload)
