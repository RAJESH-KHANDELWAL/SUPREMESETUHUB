"""Compatibility entry point for the Global Setu backend namespace.

The canonical implementation boundary lives at
:mod:`backend.global_hub.global_setu`. This package preserves the shorter
`backend.global_setu` import path without creating a second implementation.
"""

from backend.global_hub import global_setu

__all__ = ["global_setu"]
