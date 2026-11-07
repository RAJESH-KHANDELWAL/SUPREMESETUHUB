"""
CORE Leadership Layer

Central leadership-role definitions for the SupremeSetuHub CORE.

This package represents leadership and management responsibilities.
Actual technical execution belongs to backend/engines.
"""

from .base import LeadershipRole
from .registry import LeadershipRegistry

__all__ = [
    "LeadershipRole",
    "LeadershipRegistry",
]
