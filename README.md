# SUPREMESETUHUB — MAIN BASE FOUNDATION

SUPREMESETUHUB is a central foundation for identity, businesses, applications, websites, software, storage, security, and digital services.

## Project layout

- `backend/` — primary FastAPI backend, API routers, services, and backend dependencies.
- `backend/api/app.py` — primary FastAPI application.
- `backend/start.py` — backend startup entry point.
- `backend/requirements.txt` — Python dependencies for the primary backend.
- `app.py` — separate root-level Flask application; it is not the FastAPI entry point.

## Run the primary backend locally

From the repository root, install backend dependencies:

```bash
python -m pip install -r backend/requirements.txt
```

Start the FastAPI backend:

```bash
python -m backend.start
```

The server uses `PORT` if set and otherwise defaults to `8000`. Open the API docs at `http://127.0.0.1:8000/docs` and check `http://127.0.0.1:8000/health`.

Equivalent development command:

```bash
uvicorn backend.api.app:app --reload --host 127.0.0.1 --port 8000
```

## Deployment

The root `render.yaml` and `backend/render.yaml` are both retained intentionally. Both currently use the repository-root working directory and the same backend dependency/start commands. Configure only one of these files for a given Render service to avoid creating duplicate services.

## Important

The presence of modules or endpoints does not by itself establish production readiness. Before public production use, verify authentication and authorization, tenant isolation, database migrations and backups, monitoring, secret management, provider integrations, and end-to-end tests.
