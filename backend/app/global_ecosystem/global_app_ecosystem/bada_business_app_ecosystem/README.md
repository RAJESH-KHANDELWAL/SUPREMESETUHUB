# BADA BUSINESS APP ECOSYSTEM

**Layer:** APP  
**Parent:** GLOBAL APP ECOSYSTEM  
**Branch:** `main`

This package is the Bada Business-specific application composition layer, parallel in purpose to the Bada Business API and AI packages.

## Responsibilities
- Define Bada Business application module descriptors.
- Register APP-owned components.
- Track the APP composition lifecycle.
- Accept API and AI service facades through explicit dependency injection.
- Report application composition diagnostics.

## Boundaries
- **API** owns HTTP transport, routes, request/response contracts and provider-facing API interfaces.
- **AI** owns AI capabilities, agents, policies and workflows.
- **CORE** owns business rules and cross-domain orchestration.
- **ENGINE** owns runtime execution and provider/model/tool dispatch.
- **DATABASE / STORAGE** own persistence and storage adapters.
- **APP** only composes and presents these capabilities.

The APP catalog does not duplicate provider URLs, program records or resource metadata. The canonical resource owner remains `backend.global_ecosystem.global_bada_business_ecosystem/`.

## Current behavior
- Six application module descriptors are registered in an in-memory registry.
- API and AI interfaces are optional injected dependencies; no direct cross-layer implementation imports are made.
- Lifecycle transitions are explicit and validated.
- No web server, background task, API call, AI inference or provider action is started by this package.
- This package is a foundation and is not automatically mounted into the active FastAPI application.

## Public entry point
`BadaBusinessAppManager(api_service=None, ai_service=None).initialize()`
