
import os
import sqlite3
from contextlib import asynccontextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal
from uuid import uuid4

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, Field, HttpUrl


APP_NAME = "SUPREMESETUHUB"
APP_VERSION = "0.1.0"

DB_PATH = Path(os.getenv("SUPREME_DB_PATH", "supremesetuhub.db"))
ADMIN_API_KEY = os.getenv("SUPREME_ADMIN_API_KEY", "")


# ==================================================
# DATABASE
# ==================================================

def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with db() as conn:
        conn.executescript("""
        PRAGMA journal_mode=WAL;

        CREATE TABLE IF NOT EXISTS organizations (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            org_type TEXT NOT NULL,
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS integrations (
            id TEXT PRIMARY KEY,
            organization_id TEXT NOT NULL,
            name TEXT NOT NULL,
            integration_type TEXT NOT NULL,
            endpoint TEXT,
            status TEXT NOT NULL DEFAULT 'registered',
            created_at TEXT NOT NULL,
            FOREIGN KEY (organization_id)
                REFERENCES organizations(id)
        );

        CREATE INDEX IF NOT EXISTS idx_integrations_org
        ON integrations(organization_id);
        """)


@asynccontextmanager
async def lifespan(app):
    init_db()
    yield


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description=(
        "SUPREMESETUHUB MAIN BASE FOUNDATION "
        "AND CENTRAL DIGITAL ECOSYSTEM"
    ),
    lifespan=lifespan,
)


# ==================================================
# SECURITY
# ==================================================

def admin(key):
    if not ADMIN_API_KEY:
        raise HTTPException(
            status_code=503,
            detail=(
                "Admin API disabled. Configure "
                "SUPREME_ADMIN_API_KEY."
            ),
        )

    if key != ADMIN_API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid admin API key",
        )


def now():
    return datetime.now(timezone.utc).isoformat()


# ==================================================
# DATA MODELS
# ==================================================

class OrganizationIn(BaseModel):
    name: str = Field(min_length=2, max_length=160)

    org_type: Literal[
        "person",
        "business",
        "company",
        "developer",
        "partner",
    ]


class IntegrationIn(BaseModel):
    name: str = Field(min_length=2, max_length=160)

    integration_type: Literal[
        "website",
        "mobile_app",
        "software",
        "api",
        "service",
        "other",
    ]

    endpoint: HttpUrl | None = None


# ==================================================
# MAIN FOUNDATION
# ==================================================

@app.get("/")
def root():
    return {
        "platform": APP_NAME,
        "purpose": "MAIN BASE FOUNDATION / CENTRAL HUB",
        "status": "running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "platform": APP_NAME,
        "version": APP_VERSION,
    }


@app.get("/api/v1/foundation")
def foundation():
    return {
        "name": APP_NAME,
        "role": "central_foundation",
        "principles": [
            "shared foundation",
            "modular services",
            "organization-scoped resources",
            "API-first integrations",
            "portable deployment",
        ],
        "modules": [
            "identity",
            "organizations",
            "integrations",
            "security",
            "storage",
            "AI",
            "notifications",
            "dashboard",
            "audit",
        ],
    }


# ==================================================
# ORGANIZATION REGISTRY
# ==================================================

@app.post("/api/v1/organizations", status_code=201)
def create_org(
    data: OrganizationIn,
    x_admin_api_key: str | None = Header(default=None),
):
    admin(x_admin_api_key)

    org_id = "ORG-" + uuid4().hex[:16].upper()
    created = now()

    with db() as conn:
        conn.execute(
            """
            INSERT INTO organizations
            (id, name, org_type, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (org_id, data.name, data.org_type, created),
        )

    return {
        "id": org_id,
        "name": data.name,
        "org_type": data.org_type,
        "created_at": created,
    }


@app.get("/api/v1/organizations")
def get_orgs(
    x_admin_api_key: str | None = Header(default=None),
):
    admin(x_admin_api_key)

    with db() as conn:
        rows = conn.execute(
            """
            SELECT id, name, org_type, created_at
            FROM organizations
            ORDER BY created_at DESC
            """
        ).fetchall()

    return {
        "items": [dict(row) for row in rows],
        "count": len(rows),
    }


# ==================================================
# INTEGRATION REGISTRY
# ==================================================

@app.post(
    "/api/v1/organizations/{organization_id}/integrations",
    status_code=201,
)
def create_integration(
    organization_id: str,
    data: IntegrationIn,
    x_admin_api_key: str | None = Header(default=None),
):
    admin(x_admin_api_key)

    with db() as conn:
        organization = conn.execute(
            "SELECT id FROM organizations WHERE id = ?",
            (organization_id,),
        ).fetchone()

        if organization is None:
            raise HTTPException(
                status_code=404,
                detail="Organization not found",
            )

        integration_id = "INT-" + uuid4().hex[:16].upper()
        created = now()
        endpoint = str(data.endpoint) if data.endpoint else None

        conn.execute(
            """
            INSERT INTO integrations
            (
                id,
                organization_id,
                name,
                integration_type,
                endpoint,
                status,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, 'registered', ?)
            """,
            (
                integration_id,
                organization_id,
                data.name,
                data.integration_type,
                endpoint,
                created,
            ),
        )

    return {
        "id": integration_id,
        "organization_id": organization_id,
        "name": data.name,
        "integration_type": data.integration_type,
        "endpoint": endpoint,
        "status": "registered",
        "created_at": created,
    }


@app.get(
    "/api/v1/organizations/{organization_id}/integrations"
)
def get_integrations(
    organization_id: str,
    x_admin_api_key: str | None = Header(default=None),
):
    admin(x_admin_api_key)

    with db() as conn:
        organization = conn.execute(
            "SELECT id FROM organizations WHERE id = ?",
            (organization_id,),
        ).fetchone()

        if organization is None:
            raise HTTPException(
                status_code=404,
                detail="Organization not found",
            )

        rows = conn.execute(
            """
            SELECT
                id,
                organization_id,
                name,
                integration_type,
                endpoint,
                status,
                created_at
            FROM integrations
            WHERE organization_id = ?
            ORDER BY created_at DESC
            """,
            (organization_id,),
        ).fetchall()

    return {
        "items": [dict(row) for row in rows],
        "count": len(rows),
    }
