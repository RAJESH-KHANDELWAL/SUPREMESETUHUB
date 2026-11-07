
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

    def test_ecosystem_status_route_is_private(self):
        response = self.client.get("/api/global-ecosystem/status")
        self.assertEqual(response.status_code, 401)

    def test_ecosystem_health_route_is_private(self):
        response = self.client.get("/api/global-ecosystem/health")
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
