"""Google storage products; descriptive metadata only."""
from __future__ import annotations

from ..core.service import capability

CAPABILITIES = [
    capability("storage", "Google Cloud Storage", "Cloud Storage JSON API", notes="Object storage; bucket IAM, retention, and lifecycle policies are separate setup steps."),
    capability("storage", "Google Drive", "Google Drive API", auth="User OAuth 2.0 with least-privilege scopes", notes="User or Workspace file access depends on consent and granted scopes."),
]


def get_capabilities() -> list[dict]:
    return [dict(item) for item in CAPABILITIES]
