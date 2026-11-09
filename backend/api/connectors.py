
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
from backend.supreme.config import CONNECTED_REPOS
from backend.integrations.provider.github import GitHubProvider
from backend.integrations.provider.huggingface import HuggingFaceProvider


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


github_api_provider = GitHubProvider()


def _github_api_error(exc: httpx.HTTPStatusError) -> HTTPException:
    status = exc.response.status_code
    if status == 401:
        detail = "GITHUB_TOKEN_INVALID_OR_EXPIRED"
    elif status == 403:
        detail = "GITHUB_PERMISSION_OR_RATE_LIMIT_ERROR"
    elif status == 404:
        detail = "GITHUB_RESOURCE_NOT_FOUND_OR_NOT_ACCESSIBLE"
    else:
        detail = "GITHUB_API_REQUEST_FAILED"
    return HTTPException(status_code=502 if status >= 500 else status, detail=detail)


@router.get("/github/status")
def github_repository_status():
    """Validate the configured server-side GitHub token against the user and repository APIs."""
    if not github_api_provider.token():
        return {
            "success": False,
            "connector": "github",
            "status": "NEEDS_CONFIGURATION",
            "required_environment_variables": ["GITHUB_TOKEN (or GH_TOKEN)"],
            "live_connection_verified": False,
        }

    repository = os.getenv(
        "SUPREMESETUHUB_GITHUB_REPOSITORY",
        "RAJESH-KHANDELWAL/SUPREMESETUHUB",
    ).strip()

    try:
        user = github_api_provider.request("GET", "/user")
        repo_data = github_api_provider.request("GET", f"/repos/{repository}")
        return {
            "success": True,
            "connector": "github",
            "status": "CONNECTED",
            "authenticated_user": user.get("login"),
            "repository": repo_data.get("full_name"),
            "default_branch": repo_data.get("default_branch"),
            "permissions": repo_data.get("permissions", {}),
            "token_scopes": None,
            "live_connection_verified": True,
        }
    except httpx.HTTPStatusError as exc:
        raise _github_api_error(exc) from exc
    except (httpx.HTTPError, RuntimeError) as exc:
        raise HTTPException(
            status_code=503,
            detail="GITHUB_API_UNAVAILABLE_OR_NOT_CONFIGURED",
        ) from exc


@router.get("/github/api/user")
def github_authenticated_user():
    """Return the identity associated with the configured GitHub API token."""
    try:
        user = github_api_provider.request("GET", "/user")
        return {
            "success": True,
            "login": user.get("login"),
            "name": user.get("name"),
            "html_url": user.get("html_url"),
            "type": user.get("type"),
        }
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except httpx.HTTPStatusError as exc:
        raise _github_api_error(exc) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=503, detail="GITHUB_API_UNAVAILABLE") from exc


@router.get("/github/api/repositories")
def github_authenticated_repositories(
    visibility: str = Query(default="all", pattern="^(all|public|private)$"),
    per_page: int = Query(default=30, ge=1, le=100),
):
    """List repositories visible to the configured GitHub token."""
    try:
        data = github_api_provider.request(
            "GET",
            "/user/repos",
            params={
                "visibility": visibility,
                "per_page": per_page,
                "sort": "updated",
                "direction": "desc",
            },
        )
        return {"success": True, "repositories": data.get("items", [])}
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except httpx.HTTPStatusError as exc:
        raise _github_api_error(exc) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=503, detail="GITHUB_API_UNAVAILABLE") from exc


@router.get("/github/api/repository/{owner}/{repo}")
def github_authenticated_repository(owner: str, repo: str):
    """Read repository metadata through authenticated GitHub REST API."""
    try:
        data = github_api_provider.request("GET", f"/repos/{owner}/{repo}")
        return {
            "success": True,
            "repository": {
                "full_name": data.get("full_name"),
                "private": data.get("private"),
                "default_branch": data.get("default_branch"),
                "html_url": data.get("html_url"),
                "permissions": data.get("permissions", {}),
            },
        }
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except httpx.HTTPStatusError as exc:
        raise _github_api_error(exc) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=503, detail="GITHUB_API_UNAVAILABLE") from exc


@router.get("/github/repositories")
def github_repository_registry():
    """List repositories registered under the SUPREMESETUHUB foundation.

    This is a central registry, not proof of live API connectivity or sync.
    Secrets and repository write credentials are never returned by this route.
    """
    repositories = [
        {
            "key": key,
            "name": item["name"],
            "owner": item["owner"],
            "url": item["url"],
            "type": item["type"],
            "status": item["status"],
            "integration_mode": item["integration_mode"],
            "runtime_connection": item["runtime_connection"],
        }
        for key, item in CONNECTED_REPOS.items()
    ]
    return {
        "success": True,
        "foundation": "SUPREMESETUHUB",
        "mode": "CENTRAL_REPOSITORY_REGISTRY",
        "live_runtime_sync_enabled": False,
        "repository_count": len(repositories),
        "repositories": repositories,
        "note": (
            "Registration centralizes project identity only. Configure and "
            "verify authenticated API/runtime integrations before enabling sync."
        ),
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


huggingface_api_provider = HuggingFaceProvider()


def _huggingface_api_error(exc: httpx.HTTPStatusError) -> HTTPException:
    status = exc.response.status_code
    if status == 401:
        detail = "HUGGINGFACE_TOKEN_INVALID_OR_EXPIRED"
    elif status == 403:
        detail = "HUGGINGFACE_PERMISSION_OR_GATED_RESOURCE_ERROR"
    elif status == 404:
        detail = "HUGGINGFACE_RESOURCE_NOT_FOUND"
    else:
        detail = "HUGGINGFACE_API_REQUEST_FAILED"
    return HTTPException(status_code=502 if status >= 500 else status, detail=detail)


@router.get("/huggingface/status")
def huggingface_status():
    if not huggingface_api_provider.token():
        return {
            "success": False,
            "connector": "huggingface",
            "status": "NEEDS_CONFIGURATION",
            "required_environment_variables": ["HF_TOKEN (or HUGGINGFACEHUB_API_TOKEN)"],
            "live_connection_verified": False,
        }
    try:
        identity = huggingface_api_provider.request("GET", "/whoami-v2")
        return {
            "success": True,
            "connector": "huggingface",
            "status": "CONNECTED",
            "authenticated_user": identity.get("name") or identity.get("fullname"),
            "live_connection_verified": True,
        }
    except httpx.HTTPStatusError as exc:
        raise _huggingface_api_error(exc) from exc
    except (httpx.HTTPError, RuntimeError) as exc:
        raise HTTPException(status_code=503, detail="HUGGINGFACE_API_UNAVAILABLE_OR_NOT_CONFIGURED") from exc


@router.get("/huggingface/api/whoami")
def huggingface_whoami():
    try:
        return {"success": True, "identity": huggingface_api_provider.request("GET", "/whoami-v2")}
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except httpx.HTTPStatusError as exc:
        raise _huggingface_api_error(exc) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=503, detail="HUGGINGFACE_API_UNAVAILABLE") from exc


def _huggingface_search(resource: str, search: str | None, limit: int):
    try:
        data = huggingface_api_provider.request(
            "GET",
            f"/{resource}",
            params={"search": search or "", "limit": limit},
        )
        return {"success": True, "items": data}
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except httpx.HTTPStatusError as exc:
        raise _huggingface_api_error(exc) from exc
    except httpx.HTTPError as exc:
        raise HTTPException(status_code=503, detail="HUGGINGFACE_API_UNAVAILABLE") from exc


@router.get("/huggingface/api/models")
def huggingface_models(search: str | None = Query(default=None, max_length=200), limit: int = Query(default=20, ge=1, le=100)):
    return _huggingface_search("models", search, limit)


@router.get("/huggingface/api/datasets")
def huggingface_datasets(search: str | None = Query(default=None, max_length=200), limit: int = Query(default=20, ge=1, le=100)):
    return _huggingface_search("datasets", search, limit)


@router.get("/huggingface/api/spaces")
def huggingface_spaces(search: str | None = Query(default=None, max_length=200), limit: int = Query(default=20, ge=1, le=100)):
    return _huggingface_search("spaces", search, limit)
