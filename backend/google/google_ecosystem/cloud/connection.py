"""Read-only Google Cloud authentication and project-access check.

This adapter only reads Cloud Resource Manager project metadata. It does not
create, update, or delete Google Cloud resources.
"""
from __future__ import annotations

import os
from typing import Any

CLOUD_PLATFORM_READ_ONLY_SCOPE = "https://www.googleapis.com/auth/cloud-platform.read-only"
PROJECTS_API = "https://cloudresourcemanager.googleapis.com/v3/projects"


def check_cloud_connection() -> dict[str, Any]:
    """Check ADC credentials and read the configured Google Cloud project.

    Configuration:
      - GOOGLE_CLOUD_PROJECT (recommended) or a project ID discovered from ADC.
      - Application Default Credentials, e.g. workload identity or a service
        account configured outside the repository.

    No credential values, tokens, or full provider error bodies are returned.
    """
    try:
        import google.auth
        from google.auth.exceptions import DefaultCredentialsError
        from google.auth.transport.requests import AuthorizedSession
    except ImportError:
        return {
            "provider": "google_cloud",
            "status": "DEPENDENCY_MISSING",
            "connected": False,
            "project_id": None,
            "detail": "Install the backend requirements to enable Google Cloud checks.",
        }

    try:
        credentials, discovered_project = google.auth.default(
            scopes=[CLOUD_PLATFORM_READ_ONLY_SCOPE]
        )
    except DefaultCredentialsError:
        return {
            "provider": "google_cloud",
            "status": "AUTHENTICATION_NOT_CONFIGURED",
            "connected": False,
            "project_id": os.getenv("GOOGLE_CLOUD_PROJECT") or None,
            "detail": "Configure Application Default Credentials outside the repository.",
        }
    except Exception:
        return {
            "provider": "google_cloud",
            "status": "CREDENTIAL_DISCOVERY_ERROR",
            "connected": False,
            "project_id": os.getenv("GOOGLE_CLOUD_PROJECT") or None,
            "detail": "Google credential discovery failed; inspect server logs securely.",
        }

    project_id = os.getenv("GOOGLE_CLOUD_PROJECT") or discovered_project
    if not project_id:
        return {
            "provider": "google_cloud",
            "status": "PROJECT_NOT_CONFIGURED",
            "connected": False,
            "project_id": None,
            "detail": "Set GOOGLE_CLOUD_PROJECT to the target project ID.",
        }

    try:
        session = AuthorizedSession(credentials)
        response = session.get(f"{PROJECTS_API}/{project_id}", timeout=10)
    except Exception:
        return {
            "provider": "google_cloud",
            "status": "NETWORK_ERROR",
            "connected": False,
            "project_id": project_id,
            "detail": "Google Cloud Resource Manager could not be reached.",
        }

    if response.status_code == 200:
        try:
            project: dict[str, Any] = response.json()
        except ValueError:
            project = {}
        return {
            "provider": "google_cloud",
            "status": "CONNECTED_READ_ONLY",
            "connected": True,
            "project_id": project_id,
            "project_state": project.get("state"),
            "detail": "Read-only project metadata was retrieved successfully.",
        }

    if response.status_code in (401, 403):
        status = "AUTHENTICATION_FAILED" if response.status_code == 401 else "PERMISSION_DENIED"
        detail = (
            "Google Cloud rejected the credentials."
            if response.status_code == 401
            else "Credentials were not permitted to read this project's metadata."
        )
    elif response.status_code == 404:
        status = "PROJECT_NOT_FOUND"
        detail = "The configured project was not found or is not visible to these credentials."
    else:
        status = "PROVIDER_ERROR"
        detail = f"Google Cloud Resource Manager returned HTTP {response.status_code}."

    return {
        "provider": "google_cloud",
        "status": status,
        "connected": False,
        "project_id": project_id,
        "detail": detail,
    }
