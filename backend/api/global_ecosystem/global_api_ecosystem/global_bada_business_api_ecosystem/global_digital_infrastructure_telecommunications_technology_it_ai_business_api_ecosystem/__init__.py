"""Compatibility entry point for the Digital Infrastructure & Telecommunications API Ecosystem."""
from pathlib import Path as _Path
from ..industry_api_ecosystems.digital_infrastructure_telecommunications import *
__path__ = [str(_Path(__file__).resolve().parent.parent / "industry_api_ecosystems" / "digital_infrastructure_telecommunications")]
