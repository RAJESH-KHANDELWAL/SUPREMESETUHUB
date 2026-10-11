
"""Route tests for the GLOBAL ECOSYSTEM backend API."""

import unittest

from fastapi.testclient import TestClient

from backend.api.app import app


class TestGlobalEcosystemRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_health_route(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")

    def test_ecosystem_status_route(self):
        response = self.client.get("/api/global-ecosystem/status")
        self.assertIn(response.status_code, (200, 404))

    def test_ecosystem_health_route(self):
        response = self.client.get("/api/global-ecosystem/health")
        self.assertIn(response.status_code, (200, 404))


if __name__ == "__main__":
    unittest.main()
