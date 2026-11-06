"""Global Finance, Banking & Insurance API ecosystem entry point."""
from pathlib import Path as _Path
from ..finance_banking_insurance import *
_BASE = _Path(__file__).resolve().parent
_IMPLEMENTATION = _Path(__file__).resolve().parent.parent / "finance_banking_insurance"
# Expose both local Global payment sub-ecosystems and the current finance
# implementation while the source package is being consolidated.
__path__ = [str(_BASE), str(_IMPLEMENTATION)]
