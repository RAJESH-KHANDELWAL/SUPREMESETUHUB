import unittest
from ..contracts import EmbedRequest, validate_request
class EmbedContractTests(unittest.TestCase):
    def test_valid_request(self):
        self.assertTrue(validate_request(EmbedRequest(texts=("hello",))))
    def test_invalid_request(self):
        with self.assertRaises(ValueError):
            validate_request(EmbedRequest(texts=("",)))
if __name__ == "__main__":
    unittest.main()
