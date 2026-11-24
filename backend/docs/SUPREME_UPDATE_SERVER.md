# SUPREME UPDATE SERVER

The existing FastAPI application (backend/api/app.py) hosts the first-party WordPress update API.

## Registered plugins

- supremesetuhub — supremesetuhub/supremesetuhub.php
- dr-rajesh-khandelwal-ibc — dr-rajesh-khandelwal-ibc/dr-rajesh-khandelwal-ibc.php

## API

- GET /api/v1/supreme-updates/health — readiness and configuration status
- GET /api/v1/supreme-updates/check/{slug}?installed_version=1.0.0 — latest release metadata
- GET /api/v1/supreme-updates/download/{slug}/{version}?expires=...&token=... — short-lived signed download
- POST /api/v1/supreme-updates/admin/publish/{slug} — publish a ZIP package (Bearer admin token; multipart form)

Publishing validates the ZIP, required plugin main file, package size, and archive paths. The server stores the package and release registry, computes SHA-256, and returns that digest to WordPress. The WordPress client verifies SHA-256 before installation.

## Required environment

- SUPREME_UPDATE_ADMIN_TOKEN — long random secret used only by the publisher
- SUPREME_UPDATE_SIGNING_SECRET — at least 32 characters; signs short-lived package download URLs
- SUPREME_UPDATE_STORAGE_DIR — package/registry directory
- SUPREME_UPDATE_STORAGE_DURABILITY_ACKNOWLEDGED=true — set only after persistent storage has actually been configured and tested

## Deployment warning

The repository's current render.yaml declares the API service as plan: free. A path such as /var/data/supreme-updates is **not persistent merely because it is configured as an environment variable**. Do not set the durability acknowledgement on an ephemeral filesystem. Before publishing releases, attach a Render persistent disk (which may require a paid service) or implement and configure durable S3-compatible object storage. The API deliberately refuses release publishing until the durability acknowledgement is true.

## GitHub's limited role

GitHub Actions only validates PHP, builds ZIP packages, and sends them to this API. GitHub Releases are not used. Configure repository secret SUPREME_UPDATE_ADMIN_TOKEN; optionally configure repository variable SUPREME_UPDATE_SERVER_URL (default: https://supremesetuhub-3v4e.onrender.com). The publishing workflow is .github/workflows/publish-supreme-updates.yml.
