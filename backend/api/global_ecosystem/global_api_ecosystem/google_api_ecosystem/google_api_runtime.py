"""Shared, credential-safe runtime for Google API integrations."""
from __future__ import annotations
import os
from typing import Any

class GoogleIntegrationError(RuntimeError):
    """Raised when Google API configuration or authorization is incomplete."""

def required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise GoogleIntegrationError(f"Missing required environment variable: {name}")
    return value

def configured_scopes(env_name: str) -> list[str]:
    scopes = [item.strip() for item in required_env(env_name).split(",") if item.strip()]
    if not scopes:
        raise GoogleIntegrationError(f"{env_name} must contain at least one OAuth scope")
    return scopes

def build_google_discovery_client(api_name: str, api_version: str, scopes_env: str, *, cache_discovery: bool = False) -> Any:
    """Build a Discovery API client using Google Application Default Credentials."""
    try:
        import google.auth
        from googleapiclient.discovery import build
    except ImportError as exc:
        raise GoogleIntegrationError("Install backend requirements to use Google API integrations") from exc
    credentials, _ = google.auth.default(scopes=configured_scopes(scopes_env))
    return build(api_name, api_version, credentials=credentials, cache_discovery=cache_discovery)

def build_authorized_session(scopes_env: str) -> Any:
    """Return an authenticated HTTP session for Google REST APIs."""
    try:
        import google.auth
        from google.auth.transport.requests import AuthorizedSession
    except ImportError as exc:
        raise GoogleIntegrationError("Install google-auth to use Google REST integrations") from exc
    credentials, _ = google.auth.default(scopes=configured_scopes(scopes_env))
    return AuthorizedSession(credentials)
