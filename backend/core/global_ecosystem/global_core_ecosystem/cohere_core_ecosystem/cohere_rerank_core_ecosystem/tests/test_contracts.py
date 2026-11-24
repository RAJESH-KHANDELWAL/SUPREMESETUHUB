import unittest
from ..contracts import RerankRequest, validate_request
class RerankContractTests(unittest.TestCase):
    def test_valid_request(self):
        self.assertTrue(validate_request(RerankRequest(query="hello", documents=("hello world",))))
    def test_invalid_request(self):
        with self.assertRaises(ValueError):
            validate_request(RerankRequest(query="", documents=()))
if __name__ == "__main__":
    unittest.main()
