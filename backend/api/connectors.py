from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

from backend.integrations.connectors.adapters import ConnectorAdapter
from backend.integrations.connectors.manager import ConnectorManager
from backend.integrations.connectors.openai_image import (
    OpenAIImageConnector,
)
from backend.integrations.connectors.registry import connector_registry


router = APIRouter(
    prefix="/api/v1/connectors",
    tags=["External Connectors"],
)


connector_manager = ConnectorManager(
    registry=connector_registry
)


class ImageGenerateRequest(BaseModel):
    prompt: str = Field(min_length=1)
    model: str = "gpt-image-1"
    size: str = "1024x1024"
    quality: str = "auto"


def register_openai_image_adapter() -> None:
    """
    Register the real OpenAI Image adapter only when
    the required provider credential is configured.
    """

    try:
        connector = OpenAIImageConnector()

    except RuntimeError:
        return

    connector_manager.register_adapter(
        ConnectorAdapter(
            name="openai_image",
            handler=connector.generate,
        )
    )


register_openai_image_adapter()


@router.get("/status")
def connector_status():
    return connector_manager.status()


@router.get("/")
def list_connectors(
    category: str | None = Query(default=None),
):
    return {
        "success": True,
        "category": category,
        "connectors": connector_manager.list_connectors(
            category=category
        ),
    }


@router.get("/{name}")
def connector_details(name: str):

    try:
        connector = connector_registry.get(name)

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    data = connector.public_info()

    data["adapter"] = (
        "READY"
        if connector_manager.has_adapter(name)
        else "NOT_CONFIGURED"
    )

    return {
        "success": True,
        "connector": data,
    }


@router.post("/openai-image/generate")
def generate_openai_image(
    payload: ImageGenerateRequest,
):

    if not connector_manager.has_adapter(
        "openai_image"
    ):
        raise HTTPException(
            status_code=503,
            detail="OPENAI_IMAGE_CONNECTOR_NOT_CONFIGURED",
        )

    try:

        return connector_manager.execute(
            "openai_image",
            prompt=payload.prompt,
            model=payload.model,
            size=payload.size,
            quality=payload.quality,
        )

    except Exception as exc:

        raise HTTPException(
            status_code=502,
            detail={
                "error": "OPENAI_IMAGE_REQUEST_FAILED",
                "message": str(exc),
            },
        ) from exc
