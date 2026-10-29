"""Provider discovery facade backed by provider-specific ecosystem modules."""
from __future__ import annotations

from copy import deepcopy
from importlib import import_module
from typing import Any

PROVIDER_MODULE_IDS: tuple[str, ...] = (
    "hinge",
    "bumble",
    "match_group",
    "eharmony",
    "okcupid",
    "planned_couples_therapy_directory",
    "planned_sexual_health_directory",
    "onlyfans",
    "fansly",
    "fanvue",
    "manyvids",
    "xvideos",
    "xhamster",
    "redtube",
    "brazzers",
    "reality_kings",
    "mofos",
    "adult_time",
    "manyvids_creators",
    "segpay",
    "ccbill",
    "verotel",
    "cloudflare",
    "aws",
    "digitalocean",
    "hostkey",
    "shinjiru",
    "flokinet",
    "planned_adult_live_streaming",
    "planned_adult_audio_publishing",
    "planned_erotic_literature",
    "planned_age_assurance",
    "planned_moderation",
)


def list_entries(category_id: str | None = None) -> list[dict[str, Any]]:
    """Load provider metadata from each provider-specific package.

    This is catalog discovery only; no credentials or third-party API calls occur.
    """
    rows: list[dict[str, Any]] = []
    for provider_id in PROVIDER_MODULE_IDS:
        module = import_module(
            f"..{provider_id}_intimacy_api_ecosystem."
            f"{provider_id}_intimacy_api_ecosystem",
            package=__package__,
        )
        row = deepcopy(module.PROVIDER_INTIMACY_ECOSYSTEM)
        if category_id:
            key = category_id.strip().upper()
            if key not in row["category_ids"]:
                continue
        rows.append(row)
    return rows
