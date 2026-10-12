# Hostinger WordPress + SUPREMESETUHUB connection checklist

This repository has a FastAPI backend in `backend/` and a WordPress connector plugin in `wordpress-plugin/supremesetuhub-connector/`. GitHub is source control; it does not automatically install a plugin into a live WordPress website.

## Required order
1. Deploy the FastAPI backend to a runtime that supports a persistent Python web process (a Hostinger VPS or another supported Python host). Standard WordPress shared hosting should not be assumed to run the FastAPI service.
2. Configure persistent database storage for the backend. The current main application uses SQLite; ensure the database directory is on persistent disk and is backed up.
3. Confirm `GET /health` returns HTTP 200 over HTTPS on the final API hostname.
4. Install and activate the connector plugin in WordPress Admin → Plugins.
5. In Settings → SUPREMESETUHUB, save the actual backend API base URL and run the connection test.
6. Add the POD and/or digital-catalog shortcode to a draft page, verify mobile layout, then publish.
7. Do not enable paid checkout until a real payment provider, server-side webhook/signature verification, order persistence, refunds, tax rules, and private file delivery are tested end to end.

## Hostinger deploy workflow
The repository contains deployment workflow drafts under `backend/.github/workflows/`. GitHub Actions only discovers workflows under the repository-root `.github/workflows/` directory. The nested drafts do not deploy anything as currently placed. Before adding a live deployment workflow, confirm whether the Hostinger plan is **shared WordPress hosting or VPS** and set the required GitHub Actions secrets/variables. Never commit credentials.

## WordPress database
Do not share database passwords in chat or commit them to GitHub. The plugin does not need direct database access: it connects to the public read-only API over HTTPS. Keep the existing WordPress database separate from the backend's SQLite database unless a deliberate, tested migration is planned.
