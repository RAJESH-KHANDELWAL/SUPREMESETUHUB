# Backend Global Android Ecosystem

Backend-owned Android platform services and contracts.

## Scope
- Android-facing backend APIs, service orchestration, validation, and integration contracts.
- Keep business logic in backend services; keep UI and device-side implementation in the Android application layer.
- Reuse existing backend identity, security, database, API, and infrastructure components instead of creating duplicate implementations.

## Boundaries
- No frontend UI assets or Android application source code belong here.
- No credentials, signing keys, or production secrets belong in this directory.
- Add runtime modules only with tests and documented ownership.
