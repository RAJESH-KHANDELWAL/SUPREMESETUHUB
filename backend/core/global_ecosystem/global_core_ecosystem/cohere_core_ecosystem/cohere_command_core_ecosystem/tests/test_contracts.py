import unittest
from ..contracts import CommandRequest, validate_request
class CommandContractTests(unittest.TestCase):
    def test_valid_request(self):
        self.assertTrue(validate_request(CommandRequest(message="hello")))
    def test_invalid_request(self):
        with self.assertRaises(ValueError):
            validate_request(CommandRequest(message=""))
if __name__ == "__main__":
    unittest.main()
