"""Global Education, Learning & Training API ecosystem entry point."""
from pathlib import Path as _Path
from ..education_learning_training import *
_BASE = _Path(__file__).resolve().parent
# Keep the global package's own student ecosystem visible alongside the legacy
# implementation path until the education source migration is complete.
__path__ = [str(_BASE), str(_BASE.parent / "education_learning_training")]
