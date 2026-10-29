"""Provider discovery facade for relationship, intimacy, and adult-industry services."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from ..service import list_providers

def list_entries(category_id: str | None = None) -> list[dict[str, Any]]:
    """Return canonical provider research entries; none are marked live."""
    rows = list_providers(category_id)
    return deepcopy(rows)
