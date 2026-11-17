"""Plan-only orchestration metadata; performs no media operations."""

from __future__ import annotations

from .catalog import DOMAINS, ECOSYSTEM_ID


def describe_dependencies() -> dict:
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "dependencies": [
            {"layer": "APPLICATION", "responsibility": "age-gated UX, reporting and consent capture"},
            {"layer": "API", "responsibility": "external verification and moderation transports"},
            {"layer": "DATABASE", "responsibility": "consent, rights and audit persistence"},
            {"layer": "STORAGE", "responsibility": "protected media access and takedown"},
            {"layer": "ENGINE", "responsibility": "moderation workflow execution"},
        ],
        "domain_count": len(DOMAINS),
        "execution_enabled": False,
    }
