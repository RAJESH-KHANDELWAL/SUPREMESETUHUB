import unittest
from ..contracts import validate_request
class ContractTests(unittest.TestCase):
    def test_non_mapping_rejected(self):
        with self.assertRaises(ValueError): validate_request(None)
    def test_secret_field_rejected(self):
        with self.assertRaises(ValueError): validate_request({"metadata":{"api_key":"hidden"}})
if __name__=="__main__": unittest.main()
