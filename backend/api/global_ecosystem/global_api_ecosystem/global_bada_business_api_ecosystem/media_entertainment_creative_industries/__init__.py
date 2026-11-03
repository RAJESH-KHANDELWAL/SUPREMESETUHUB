"""Legacy root-level compatibility alias for marketing_media_entertainment."""

from pathlib import Path as _Path

from ..industry_api_ecosystems.marketing_media_entertainment import *

__path__ = [
    str(_Path(__file__).resolve().parent.parent / "industry_api_ecosystems" / "marketing_media_entertainment")
]
