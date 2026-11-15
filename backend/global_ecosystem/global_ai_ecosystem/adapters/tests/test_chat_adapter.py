import unittest

from ..contracts import ChatMessage, ChatRequest
from ..openai_compatible import OpenAICompatibleChatAdapter


class FakeHttpClient:
    def __init__(self, response):
        self.response = response
        self.last_call = None

    def post_json(self, url, *, headers, payload, idempotency_key=None):
        self.last_call = (url, headers, payload, idempotency_key)
        return self.response


class ChatAdapterTests(unittest.TestCase):
    def test_maps_request_and_normalizes_response(self):
        fake = FakeHttpClient({
            "id": "req_test", "model": "model-live",
            "choices": [{"message": {"role": "assistant", "content": "Namaste"}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 3, "completion_tokens": 1},
        })
        provider = {
            "id": "test", "name": "Test",
            "api_endpoint": "https://api.example.test/v1",
            "credential_env": "TEST_API_KEY",
        }
        adapter = OpenAICompatibleChatAdapter(provider, api_key="not-a-real-secret", http_client=fake)
        response = adapter.chat(ChatRequest(
            model="model-requested", messages=[ChatMessage(role="user", content="Hello")],
        ))
        self.assertEqual(response.content, "Namaste")
        self.assertEqual(response.provider_id, "test")
        self.assertEqual(response.model, "model-live")
        self.assertEqual(fake.last_call[0], "https://api.example.test/v1/chat/completions")
        self.assertEqual(fake.last_call[1]["Authorization"], "Bearer not-a-real-secret")
        self.assertEqual(fake.last_call[2]["messages"][0]["content"], "Hello")


if __name__ == "__main__":
    unittest.main()
