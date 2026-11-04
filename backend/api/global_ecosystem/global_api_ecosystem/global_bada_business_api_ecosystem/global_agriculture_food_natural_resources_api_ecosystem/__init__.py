"""Agriculture, food and natural resources API ecosystem."""
from .routes import router
from .service import AgricultureFoodNaturalResourcesService

__all__ = ["router", "AgricultureFoodNaturalResourcesService"]
