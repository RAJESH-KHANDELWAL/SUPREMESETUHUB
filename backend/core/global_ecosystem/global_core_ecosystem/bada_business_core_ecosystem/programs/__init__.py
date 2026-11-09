"""BADA BUSINESS CORE PROGRAMS domain package.

Owns program discovery, domain rules and workflow contracts. Canonical
program facts remain in backend.bada_business_ecosystem.
"""

from .service import BadaBusinessProgramsService
from .manager import BadaBusinessProgramsManager

__all__ = ["BadaBusinessProgramsService", "BadaBusinessProgramsManager"]
