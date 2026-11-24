"""Category readiness service."""
from .ecosystem_config import ECOSYSTEM_CONFIG

def readiness():
    return dict(ECOSYSTEM_CONFIG)
