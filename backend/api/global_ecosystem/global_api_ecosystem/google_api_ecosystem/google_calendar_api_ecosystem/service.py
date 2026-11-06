"""Calendar API client factory."""
from __future__ import annotations
from ..google_api_runtime import build_google_discovery_client

API_NAME = "calendar"
API_VERSION = "v3"
SCOPES_ENV = "GOOGLE_CALENDAR_SCOPES"

def build_client():
    """Build an authenticated client using ADC and configured least-privilege scopes."""
    return build_google_discovery_client(API_NAME, API_VERSION, SCOPES_ENV)
