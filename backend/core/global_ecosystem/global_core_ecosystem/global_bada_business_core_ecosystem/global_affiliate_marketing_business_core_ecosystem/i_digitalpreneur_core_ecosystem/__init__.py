"""iDigitalPreneur-specific CORE ecosystem package."""

from .manager import IDigitalPreneurCoreManager, get_manager
from .module_service import IDigitalPreneurModuleService
from .policies import validate_platform_program
from .service import IDigitalPreneurCoreService

PLATFORM_ID = "I-DIGITALPRENEUR"
PLATFORM_NAME = "iDigitalPreneur"
LAYER = "CORE"
ECOSYSTEM_ID = "I-DIGITALPRENEUR-CORE-ECOSYSTEM"

__all__ = [
    "PLATFORM_ID", "PLATFORM_NAME", "LAYER", "ECOSYSTEM_ID",
    "IDigitalPreneurCoreManager", "get_manager",
    "IDigitalPreneurModuleService", "IDigitalPreneurCoreService",
    "validate_platform_program",
]
