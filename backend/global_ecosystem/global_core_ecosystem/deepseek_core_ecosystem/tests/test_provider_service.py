"""Focused compatibility tests for the provider validation service."""
import unittest

from ..service import DeepSeekCoreService


class ProviderTests(unittest.TestCase):
    def setUp(self):
        self.service = DeepSeekCoreService()

    def test_unknown(self):
        with self.assertRaises(ValueError):
            self.service.validate("unknown", {})

    def test_chat(self):
        result = self.service.validate(
            "chat_completions",
            {"messages": [{"role": "user", "content": "hi"}]},
        )
        self.assertFalse(result["live_call"])

    def test_responses(self):
        self.assertEqual(
            self.service.validate("responses", {"input": "hi"})["capability"],
            "responses",
        )

    def test_search(self):
        self.assertEqual(
            self.service.validate("search", {"query": "hi"})["capability"],
            "search",
        )

    def test_fetch(self):
        self.assertEqual(
            self.service.validate(
                "fetch", {"urls": ["https://example.com"]}
            )["capability"],
            "fetch",
        )


if __name__ == "__main__":
    unittest.main()
