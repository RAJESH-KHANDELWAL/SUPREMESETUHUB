import unittest

from ..contracts import ChatMessage, ChatRequest
from ..errors import ProviderConfigurationError
from ..factory import list_chat_adapter_provider_ids
from ..openai_compatible import OpenAICompatibleChatAdapter


class AdapterContractTests(unittest.TestCase):
    def test_chat_request_requires_messages(self):
        with self.assertRaises(ValueError):
            ChatRequest(model="example-model", messages=[])

    def test_chat_message_rejects_unknown_role(self):
        with self.assertRaises(ValueError):
            ChatMessage(role="root", content="hello")

    def test_compatible_provider_allowlist(self):
        self.assertEqual(len(list_chat_adapter_provider_ids()), 20)
        self.assertIn("groq", list_chat_adapter_provider_ids())

    def test_adapter_requires_credentials(self):
        provider = {
            "id": "test", "name": "Test",
            "api_endpoint": "https://example.invalid/v1",
            "credential_env": "MISSING_TEST_PROVIDER_KEY",
        }
        with self.assertRaises(ProviderConfigurationError):
            OpenAICompatibleChatAdapter(provider, api_key=None)


if __name__ == "__main__":
    unittest.main()
