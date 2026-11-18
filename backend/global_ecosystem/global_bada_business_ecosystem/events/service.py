"""Event lifecycle helpers for Bada Business event snapshots.

Dates are evaluated only when explicitly present in the source data. Missing
dates remain unknown; this service never invents a future event or availability.
"""
from __future__ import annotations

from copy import deepcopy
from datetime import date
from typing import Any

from ..platform_resources.programs.bb_impact import BB_IMPACT
from ..platform_resources.programs.idea_to_ipo import IDEA_TO_IPO

_EVENT_SNAPSHOTS: tuple[dict[str, Any], ...] = (BB_IMPACT, IDEA_TO_IPO)


def list_events(*, on_date: date | None = None) -> tuple[dict[str, Any], ...]:
    """Return event snapshots with a derived lifecycle status when date exists."""
    today = on_date or date.today()
    results = []
    for source in _EVENT_SNAPSHOTS:
        event = deepcopy(source)
        event_date = event.get("event_date") or event.get("webinar", {}).get("date")
        if not event_date:
            event["lifecycle_status"] = "DATE_NOT_PUBLISHED"
        else:
            try:
                parsed = date.fromisoformat(event_date)
            except (TypeError, ValueError):
                event["lifecycle_status"] = "DATE_INVALID"
            else:
                event["lifecycle_status"] = "PAST" if parsed < today else ("TODAY" if parsed == today else "UPCOMING")
        results.append(event)
    return tuple(results)


def get_event(event_id: str, *, on_date: date | None = None) -> dict[str, Any] | None:
    """Return one event snapshot by its program ID."""
    normalized = (event_id or "").strip().lower()
    for event in list_events(on_date=on_date):
        if event.get("program_id") == normalized:
            return event
    return None
