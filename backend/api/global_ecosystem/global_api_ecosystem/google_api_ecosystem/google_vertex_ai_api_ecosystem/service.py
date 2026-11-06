"""Vertex Ai API client factory."""
from __future__ import annotations
from ..google_api_runtime import build_google_discovery_client

API_NAME = "aiplatform"
API_VERSION = "v1"
SCOPES_ENV = "GOOGLE_VERTEX_AI_SCOPES"

def build_client():
    """Build an authenticated client using ADC and configured least-privilege scopes."""
    return build_google_discovery_client(API_NAME, API_VERSION, SCOPES_ENV)
