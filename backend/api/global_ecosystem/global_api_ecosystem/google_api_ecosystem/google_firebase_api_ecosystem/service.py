"""Firebase API client factory."""
from __future__ import annotations
from ..google_api_runtime import build_google_discovery_client

API_NAME = "firebase"
API_VERSION = "v1beta1"
SCOPES_ENV = "GOOGLE_FIREBASE_SCOPES"

def build_client():
    """Build an authenticated client using ADC and configured least-privilege scopes."""
    return build_google_discovery_client(API_NAME, API_VERSION, SCOPES_ENV)
