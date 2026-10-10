
from __future__ import annotations

import os
import httpx

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
    """Register the OpenAI Image adapter."""

    def generate_image(**payload):
        connector = OpenAIImageConnector()
        return connector.generate(**payload)

    connector_manager.register_adapter(
        ConnectorAdapter(
            name="openai_image",
            handler=generate_image,
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


@router.post("/openai-image/generate")
def generate_openai_image(
    payload: ImageGenerateRequest,
):
    if not connector_manager.has_adapter("openai_image"):
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


@router.get("/github/status")
def github_repository_status():
    repository = os.getenv(
        "SUPREMESETUHUB_GITHUB_REPOSITORY",
        "RAJESH-KHANDELWAL/SUPREMESETUHUB",
    )

    try:
        response = httpx.get(
            f"https://api.github.com/repos/{repository}",
            headers={
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
            timeout=8.0,
        )

        if response.status_code != 200:
            return {
                "success": False,
                "connector": "github",
                "status": "ERROR",
                "http_status": response.status_code,
            }

        data = response.json()

        return {
            "success": True,
            "connector": "github",
            "status": "CONNECTED",
            "repository": data.get("full_name"),
            "default_branch": data.get("default_branch"),
        }

    except httpx.HTTPError as exc:
        return {
            "success": False,
            "connector": "github",
            "status": "UNAVAILABLE",
            "error": type(exc).__name__,
        }


@router.get("/google-cloud/status")
def google_cloud_configuration_status():
    required = {
        "project_id": "GOOGLE_CLOUD_PROJECT",
        "instance_name": "GCP_INSTANCE_NAME",
        "zone": "GCP_ZONE",
    }

    settings = {
        key: bool(os.getenv(variable, "").strip())
        for key, variable in required.items()
    }

    missing = [
        variable
        for key, variable in required.items()
        if not settings[key]
    ]

    return {
        "success": True,
        "connector": "google_cloud",
        "status": (
            "CONFIGURED"
            if not missing
            else "NEEDS_CONFIGURATION"
        ),
        "settings": settings,
        "missing_environment_variables": missing,
        "ssh_connected": False,
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
