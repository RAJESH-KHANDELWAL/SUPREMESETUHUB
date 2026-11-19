import unittest
from ..contracts import TokenizeRequest, validate_request
class TokenizeContractTests(unittest.TestCase):
    def test_valid_request(self):
        self.assertTrue(validate_request(TokenizeRequest(text="hello")))
    def test_invalid_request(self):
        with self.assertRaises(ValueError):
            validate_request(TokenizeRequest(text=""))
if __name__ == "__main__":
    unittest.main()
