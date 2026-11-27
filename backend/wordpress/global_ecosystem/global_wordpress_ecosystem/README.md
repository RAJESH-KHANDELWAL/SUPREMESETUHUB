# GLOBAL WORDPRESS ECOSYSTEM — BACKEND

This package is the backend home for the global WordPress ecosystem.

## Current integration boundary

The established runtime modules currently remain in `backend/wordpress/`
to preserve existing imports and deployment behavior:

- `bootstrap.py`
- `connection.py`
- `controller.py`
- `registry.py`
- `rest_api.py`
- `service.py`
- `sites.py`
- `wp-content/`

Move these implementation modules into this package only as a coordinated
migration that updates all imports, tests, plugin packaging, and deployment
references. Do not duplicate or silently relocate the live integration code.

## Scope

- Backend WordPress site registration and lifecycle
- Authenticated REST API integration
- Database connection and health checks
- WordPress plugin integration boundary

This package declaration does not imply that external WordPress sites are
connected or that deployment configuration has been changed.
