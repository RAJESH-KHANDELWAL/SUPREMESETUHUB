"""
Global Business Ecosystem
Runtime Entry Point
"""

from fastapi import FastAPI

from backend.api.global_business_ecosystem import router as api_router

from backend.supreme.supreme_ecosystem.supreme_business_ecosystem.global_business_ecosystem.config.settings import settings


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)


app.include_router(
    api_router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "system": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "active"
    }
