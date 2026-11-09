"""Legacy import alias for the consolidated marketing/media/entertainment package."""

from pathlib import Path as _Path

from ..marketing_media_entertainment import *

__path__ = [
    str(_Path(__file__).resolve().parent.parent / "marketing_media_entertainment")
]
