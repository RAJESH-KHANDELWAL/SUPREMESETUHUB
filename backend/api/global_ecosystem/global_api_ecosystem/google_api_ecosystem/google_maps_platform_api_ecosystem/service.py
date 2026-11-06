"""Google Maps Platform REST adapter; API key must remain server-side."""
from __future__ import annotations
import os
import httpx

BASE_URL = "https://maps.googleapis.com/maps/api"

class GoogleMapsClient:
    def __init__(self, api_key: str | None = None, timeout: float = 20.0):
        self.api_key = (api_key or os.getenv("GOOGLE_MAPS_API_KEY", "")).strip()
        if not self.api_key:
            raise RuntimeError("Missing required environment variable: GOOGLE_MAPS_API_KEY")
        self.timeout = timeout

    def get(self, endpoint: str, **params):
        if endpoint.startswith(("http://", "https://")) or ".." in endpoint:
            raise ValueError("Use a relative Google Maps API endpoint")
        response = httpx.get(f"{BASE_URL}/{endpoint.lstrip('/')}", params={**params, "key": self.api_key}, timeout=self.timeout)
        response.raise_for_status()
        payload = response.json()
        if payload.get("status") not in (None, "OK", "ZERO_RESULTS"):
            raise RuntimeError(f"Google Maps API error: {payload.get('status')}: {payload.get('error_message', '')}")
        return payload

def build_client() -> GoogleMapsClient:
    return GoogleMapsClient()
