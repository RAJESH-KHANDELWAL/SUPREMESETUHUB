import unittest
from ..contracts import ClassifyRequest, validate_request
class ClassifyContractTests(unittest.TestCase):
    def test_valid_request(self):
        self.assertTrue(validate_request(ClassifyRequest(inputs=("hello",))))
    def test_invalid_request(self):
        with self.assertRaises(ValueError):
            validate_request(ClassifyRequest(inputs=("",)))
if __name__ == "__main__":
    unittest.main()
