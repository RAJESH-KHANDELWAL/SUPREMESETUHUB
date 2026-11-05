"""Global Education, Learning & Training API ecosystem compatibility entry point."""
from pathlib import Path as _Path
from ..education_learning_training import *
__path__ = [str(_Path(__file__).resolve().parent.parent / "education_learning_training")]
