"""Compatibility entry point for the Education, Learning & Training API Ecosystem."""
from pathlib import Path as _Path
from ..industry_api_ecosystems.education_learning_training import *
__path__ = [str(_Path(__file__).resolve().parent.parent / "industry_api_ecosystems" / "education_learning_training")]
