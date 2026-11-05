"""Mount each independent Work & Careers job-family router at its canonical path."""
from importlib import import_module
from pkgutil import iter_modules
from fastapi import APIRouter
from .categories import CATEGORY_DEFINITIONS

router = APIRouter(tags=["Work & Careers — Independent Job Families"])

for category_definition in CATEGORY_DEFINITIONS:
    category_id = category_definition["id"]
    category_package = import_module(f"{__package__}.{category_id}")
    for child in iter_modules(category_package.__path__):
        if not child.ispkg or child.name in {"tests", "__pycache__"}:
            continue
        child_router = import_module(f"{__package__}.{category_id}.{child.name}.routes").router
        router.include_router(child_router, prefix=f"/work-careers/{category_id.replace('_', '-')}/{child.name}")
