"""Global Education, Learning & Training API ecosystem entry point."""
from pathlib import Path as _Path
from .education_learning_training import *
_BASE = _Path(__file__).resolve().parent
# Expose the parent student taxonomy and the nested canonical industry API.
__path__ = [str(_BASE), str(_BASE / "education_learning_training")]
