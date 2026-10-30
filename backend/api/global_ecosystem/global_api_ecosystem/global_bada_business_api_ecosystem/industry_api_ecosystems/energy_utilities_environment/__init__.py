"""Energy, Utilities & Environment industry API domain package."""
INDUSTRY_ID = "energy_utilities_environment"
INDUSTRY_NAME = "Energy, Utilities & Environment"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .service import EnergyEnvironmentService
__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "EnergyEnvironmentService"]
