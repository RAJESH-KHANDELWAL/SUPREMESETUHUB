"""Global relationship and intimacy API ecosystem.

This package exposes a catalog/discovery layer. A catalog entry is not proof
that a third-party API exists, is permitted, or is connected.
"""

from .service import get_ecosystem_status, list_categories, list_providers

__all__ = ["get_ecosystem_status", "list_categories", "list_providers"]
