"""Global Energy, Utilities & Environment API ecosystem package.

Consolidates the former energy_utilities_environment and
energy_utilities_environment_api_ecosystem root folders.
"""
INDUSTRY_ID = "energy_utilities_environment"
INDUSTRY_NAME = "Energy, Utilities & Environment"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"

from .service import EnergyEnvironmentService

__all__ = [
    "INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS",
    "EnergyEnvironmentService",
]
