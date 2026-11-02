"""Google DNS products; descriptive metadata only."""
from __future__ import annotations

from ..core.service import capability

CAPABILITIES = [
    capability("dns", "Google Cloud DNS", "Cloud DNS API", notes="Managed authoritative DNS zones and records; domain delegation remains a separate registrar task."),
]


def get_capabilities() -> list[dict]:
    return [dict(item) for item in CAPABILITIES]
