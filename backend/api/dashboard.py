"""Authenticated dashboard counters sourced from the canonical database."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter

from backend.database.service import DatabaseService

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

# Only fixed, repository-owned table names are used in SQL. If a table is not
# installed, report None rather than pretending its count is zero.
TABLE_CANDIDATES: dict[str, tuple[str, ...]] = {
    "users": ("supreme_people", "users"),
    "projects": ("projects", "project_records"),
    "businesses": ("businesses", "business_records"),
    "works": ("works", "work_items"),
    "opportunities": ("opportunities", "opportunity_records"),
    "referral_links": ("supreme_referral_links",),
    "referral_events": ("supreme_referral_events",),
    "commissions": ("supreme_commissions",),
}


def _count_table(database: DatabaseService, candidates: tuple[str, ...]) -> dict[str, Any]:
    """Count rows in the first known table that exists; absent means unknown."""
    for table_name in candidates:
        if database.table_exists(table_name):
            row = database.fetchone(f'SELECT COUNT(*) AS row_count FROM "{table_name}"')
            return {
                "count": int(row["row_count"]) if row is not None else 0,
                "table": table_name,
                "available": True,
            }
    return {"count": None, "table": None, "available": False}


def get_dashboard_metrics(database: DatabaseService | None = None) -> dict[str, Any]:
    """Read dashboard metrics without creating tables or mutating records."""
    owns_database = database is None
    db = database or DatabaseService()
    try:
        return {
            key: _count_table(db, candidates)
            for key, candidates in TABLE_CANDIDATES.items()
        }
    finally:
        if owns_database:
            db.close()


def _legacy_count(metrics: dict[str, Any], key: str) -> int | None:
    return metrics[key]["count"]


@router.get("/")
def dashboard():
    return {
        "success": True,
        "name": "SUPREMESETUHUB",
        "dashboard": "PEOPLE DASHBOARD",
        "version": "1.0.0",
        "status": "active",
        "access": "AUTHENTICATED",
    }


@router.get("/summary")
def summary():
    metrics = get_dashboard_metrics()
    return {
        "success": True,
        "dashboard": "PEOPLE DASHBOARD",
        "users": _legacy_count(metrics, "users"),
        "projects": _legacy_count(metrics, "projects"),
        "businesses": _legacy_count(metrics, "businesses"),
        "works": _legacy_count(metrics, "works"),
        "status": "active",
        "data_sources": metrics,
    }


@router.get("/statistics")
def statistics():
    metrics = get_dashboard_metrics()
    return {
        "success": True,
        "dashboard": "PEOPLE DASHBOARD",
        "statistics": {
            "users": _legacy_count(metrics, "users"),
            "projects": _legacy_count(metrics, "projects"),
            "businesses": _legacy_count(metrics, "businesses"),
            "works": _legacy_count(metrics, "works"),
            "opportunities": _legacy_count(metrics, "opportunities"),
        },
        "data_sources": metrics,
    }


@router.get("/health")
def health():
    return {
        "success": True,
        "dashboard": "PEOPLE DASHBOARD",
        "status": "healthy",
    }


@router.get("/version")
def version():
    return {
        "success": True,
        "dashboard": "PEOPLE DASHBOARD",
        "version": "1.0.0",
    }
