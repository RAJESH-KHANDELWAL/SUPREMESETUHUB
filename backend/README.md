# SUPREMESETUHUB Backend

This directory contains the primary FastAPI backend, API routers, authentication, and supporting services.

## Run from the repository root (recommended)

Install dependencies:

```bash
python -m pip install -r backend/requirements.txt
```

Start the API:

```bash
python -m backend.start
```

Then open `http://127.0.0.1:8000/docs` or check `http://127.0.0.1:8000/health`.

## Development mode

From the repository root:

```bash
uvicorn backend.api.app:app --reload --host 127.0.0.1 --port 8000
```

## Deployment configuration

The root `../render.yaml` and this directory's `render.yaml` are both retained. They currently specify the same build and start commands. Use only one Render Blueprint configuration for a given service to avoid duplicate service creation.

## Entry points

- `api/app.py` — FastAPI application and router registration.
- `start.py` — Uvicorn startup wrapper used by the Render configuration.
- `requirements.txt` — backend Python dependencies.

The root-level `app.py` is a separate Flask application and is not this backend's FastAPI entry point.
