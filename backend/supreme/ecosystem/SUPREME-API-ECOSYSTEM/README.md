# 🔌 SUPREME API ECOSYSTEM

**Responsibility:** API surface, router composition, authentication policy and HTTP delivery.

**Current runtime owner:** `backend/api/app.py`

**Existing modules:** `auth.py`, `supreme.py`, `supreme_ecosystem.py`, `dashboard.py`, `identity.py`, `global_business_ecosystem.py`, `global_ai_ecosystem.py`.

This directory is the functional catalog layer. Do not copy router implementations here. Route migration must preserve authentication middleware, route prefixes, public paths, and the existing `app.include_router(...)` registrations.
