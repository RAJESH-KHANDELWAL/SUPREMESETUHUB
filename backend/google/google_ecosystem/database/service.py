"""Google database products; descriptive metadata only."""
from __future__ import annotations

from ..core.service import capability

CAPABILITIES = [
    capability("database", "Cloud SQL", "Cloud SQL Admin API", notes="Managed relational database; project, region, IAM, and billing configuration required."),
    capability("database", "Cloud Firestore", "Cloud Firestore API", notes="Document database; security rules and IAM must be configured separately."),
    capability("database", "Firebase Realtime Database", "Firebase Realtime Database API", notes="Realtime JSON database; access rules must be configured separately."),
    capability("database", "BigQuery", "BigQuery API", notes="Analytics data warehouse, not a transactional database replacement."),
]


def get_capabilities() -> list[dict]:
    return [dict(item) for item in CAPABILITIES]
