"""Tests for language registry and safe translation configuration."""
import os
import unittest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.api.language_services import router


app = FastAPI()
app.include_router(router)
client = TestClient(app)


class LanguageServicesTests(unittest.TestCase):
    def test_catalog_separates_human_and_programming_languages(self):
        response = client.get("/api/v1/languages/catalog")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertGreaterEqual(data["human_language_count"], 50)
        self.assertGreaterEqual(data["programming_language_count"], 40)
        human_codes = {item["code"] for item in data["human_languages"]}
        self.assertTrue({"hi", "gu", "en", "ar", "zh", "ja"}.issubset(human_codes))
        programming_names = {item["name"] for item in data["programming_languages"]}
        self.assertTrue({"Python", "JavaScript", "Rust", "HTML", "CSS"}.issubset(programming_names))

    def test_translation_requires_configured_provider(self):
        os.environ.pop("SUPREME_TRANSLATION_API_URL", None)
        response = client.post("/api/v1/languages/translate", json={
            "text": "Hello world",
            "source": "en",
            "target": "hi",
        })
        self.assertEqual(response.status_code, 503)

    def test_unsupported_target_is_rejected(self):
        response = client.post("/api/v1/languages/translate", json={
            "text": "Hello world",
            "source": "en",
            "target": "made-up-language",
        })
        self.assertEqual(response.status_code, 422)

    def test_batch_size_is_bounded(self):
        response = client.post("/api/v1/languages/translate/batch", json={
            "texts": ["hello"] * 41,
            "source": "en",
            "target": "hi",
        })
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
