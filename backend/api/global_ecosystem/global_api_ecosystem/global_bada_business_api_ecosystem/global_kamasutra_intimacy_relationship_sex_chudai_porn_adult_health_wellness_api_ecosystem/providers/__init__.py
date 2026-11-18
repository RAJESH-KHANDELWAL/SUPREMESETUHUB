"""Provider directory for the global relationship and intimacy ecosystem.

The canonical metadata lives in the root service registry. These helpers expose it
from a distinct, visible providers package. Records are research leads only.
"""
from .catalog import list_entries

__all__ = ["list_entries"]
