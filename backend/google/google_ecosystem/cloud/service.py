"""Google Cloud foundation capabilities; descriptive metadata only."""
from __future__ import annotations

from ..core.service import capability

CAPABILITIES = [
    capability("cloud", "Google Cloud", "Google Cloud APIs", auth="Google Cloud IAM / workload identity federation", notes="Cloud projects, billing, IAM, enabled APIs, quotas, and region policy must be configured independently."),
    capability("cloud", "Cloud Run", "Cloud Run API", notes="Managed container runtime; deployment is not performed by this metadata catalog."),
    capability("cloud", "Google Kubernetes Engine", "Google Kubernetes Engine API", notes="Managed Kubernetes; cluster provisioning is not performed by this metadata catalog."),
]


def get_capabilities() -> list[dict]:
    return [dict(item) for item in CAPABILITIES]
