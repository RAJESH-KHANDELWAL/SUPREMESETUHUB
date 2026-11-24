"""Hierarchical API Ecosystem registry for all Work & Careers category and job-track ecosystems."""
from __future__ import annotations

from dataclasses import asdict, is_dataclass
from importlib import import_module

from fastapi import APIRouter, HTTPException, Query

from .catalog import get_category, list_categories

router = APIRouter(tags=["Work & Careers API Ecosystems"])


def _plain(record):
    return asdict(record) if is_dataclass(record) else record


def _category_or_404(category_id: str):
    category = get_category(category_id)
    if category is None:
        raise HTTPException(status_code=404, detail={"error": "WORK_CAREERS_API_ECOSYSTEM_NOT_FOUND", "category_id": category_id})
    return category


def _track_catalog(category_id: str):
    _category_or_404(category_id)
    module = import_module(f"{__package__}.{category_id}.categories")
    return module


def _category_api_record(category):
    category_id = category.id
    return {
        "api_ecosystem_id": f"{category_id.upper()}_API_ECOSYSTEM",
        "api_ecosystem_name": f"{category.name} API Ecosystem",
        "category_id": category_id,
        "category_name": category.name,
        "category_type": category.category_type,
        "api_base_path": f"/work-careers/{category_id.replace('_', '-')}",
        "ecosystem_registry_path": f"/work-careers/api-ecosystems/{category_id}",
        "specialization_api_ecosystem_template": f"{category_id.upper()}_{{SPECIALIZATION_ID}}_API_ECOSYSTEM",
        "capabilities": ["status", "specialization_catalogue", "specialization_detail", "specialization_search", "integrity"],
        "taxonomy_status": "taxonomy_only",
    }


@router.get("/api-ecosystems")
def list_work_careers_api_ecosystems(q: str | None = Query(default=None, min_length=1, max_length=100)):
    """List the 24 independent category API Ecosystems."""
    categories = list_categories()
    if q:
        needle = q.casefold().strip()
        categories = [
            item for item in categories
            if needle in item.id.casefold()
            or needle in item.name.casefold()
            or needle in item.description.casefold()
        ]
    ecosystems = [_category_api_record(item) for item in categories]
    return {
        "success": True,
        "domain_api_ecosystem": "WORK_CAREERS_EMPLOYMENT_API_ECOSYSTEM",
        "domain_name": "Work, Jobs & Careers",
        "count": len(ecosystems),
        "taxonomy_status": "taxonomy_only",
        "api_ecosystems": ecosystems,
    }


@router.get("/api-ecosystems/{category_id}")
def get_work_careers_api_ecosystem(category_id: str):
    """Return one category API Ecosystem contract."""
    category = _category_or_404(category_id)
    return {"success": True, "api_ecosystem": _category_api_record(category), "category": _plain(category)}


@router.get("/api-ecosystems/{category_id}/specializations")
@router.get("/api-ecosystems/{category_id}/tracks", include_in_schema=False)
def list_track_api_ecosystems(category_id: str, q: str | None = Query(default=None, min_length=1, max_length=100)):
    """Expose each category specialization as its own addressable API Ecosystem resource."""
    category = _category_or_404(category_id)
    module = _track_catalog(category_id)
    tracks = module.list_tracks()
    if q:
        needle = q.casefold().strip()
        tracks = [
            track for track in tracks
            if needle in track.get("id", "").casefold()
            or needle in track.get("name", "").casefold()
            or needle in track.get("description", "").casefold()
        ]
    items = []
    for track in tracks:
        track_id = track["id"]
        items.append({
            "api_ecosystem_id": f"{category_id.upper()}_{track_id.upper()}_API_ECOSYSTEM",
            "api_ecosystem_name": f"{track.get('name', track_id)} API Ecosystem",
            "parent_api_ecosystem_id": f"{category_id.upper()}_API_ECOSYSTEM",
            "category_id": category_id,
            "category_name": category.name,
            "specialization_id": track_id,
            "track_id": track_id,
            "specialization_name": track.get("name", track_id),
            "track_name": track.get("name", track_id),
            "api_resource_path": f"/work-careers/api-ecosystems/{category_id}/specializations/{track_id}",
            "capabilities": ["specialization_status", "specialization_detail"],
            "taxonomy_status": "taxonomy_only",
        })
    return {"success": True, "parent_api_ecosystem_id": f"{category_id.upper()}_API_ECOSYSTEM", "count": len(items), "specialization_api_ecosystems": items, "track_api_ecosystems": items}


@router.get("/api-ecosystems/{category_id}/specializations/{track_id}")
@router.get("/api-ecosystems/{category_id}/tracks/{track_id}", include_in_schema=False)
def get_track_api_ecosystem(category_id: str, track_id: str):
    """Return a specialization-level API Ecosystem resource and its taxonomy record."""
    category = _category_or_404(category_id)
    module = _track_catalog(category_id)
    track = module.get_track(track_id)
    if track is None:
        raise HTTPException(status_code=404, detail={"error": "WORK_CAREERS_SPECIALIZATION_API_ECOSYSTEM_NOT_FOUND", "category_id": category_id, "track_id": track_id})
    return {
        "success": True,
        "api_ecosystem": {
            "api_ecosystem_id": f"{category_id.upper()}_{track_id.upper()}_API_ECOSYSTEM",
            "api_ecosystem_name": f"{track.get('name', track_id)} API Ecosystem",
            "parent_api_ecosystem_id": f"{category_id.upper()}_API_ECOSYSTEM",
            "category_id": category_id,
            "category_name": category.name,
            "specialization_id": track_id,
            "track_id": track_id,
            "api_resource_path": f"/work-careers/api-ecosystems/{category_id}/specializations/{track_id}",
            "taxonomy_status": "taxonomy_only",
            "live_vacancies_available": False,
        },
        "specialization": track,
        "specialization": track,
        "track": track,
    }
