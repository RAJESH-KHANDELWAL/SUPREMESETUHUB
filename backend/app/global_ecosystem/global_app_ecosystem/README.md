# GLOBAL APP ECOSYSTEM

Independent application-composition and lifecycle foundation for SUPREMESETUHUB.

## Ownership and separation
APP owns application identity, component descriptors, explicit component registration, lifecycle state transitions, process-local component inventory, and safe application diagnostics. APP is the composition boundary: the application entry point may choose to assemble API routers and middleware, but their implementations remain in their owning layers.

This package does **not** implement or absorb API transport/routes, CORE orchestration, ENGINE provider execution, SECURITY policy, DATABASE persistence, STORAGE backends, or SERVER infrastructure. The APP-owned lifecycle and component metadata are exposed to the engine layer through `backend/engine/app/manager.py` (`AppEngine`). The engine is registered by `backend/core/bootstrap.py`; this does not automatically load the ecosystem from the current FastAPI entry point or execute registered components.

## Structure
- `catalog.py`: APP-owned component categories and metadata.
- `models.py`: immutable component descriptors.
- `registry.py`: thread-safe in-memory component inventory.
- `component_base.py`: explicitly injected component adapter boundary.
- `component_registry.py`: adapter validation and registration.
- `lifecycle.py`: guarded application lifecycle state machine.
- `runtime.py`: safe process diagnostics.
- `diagnostics.py`: consolidated APP status.
- `service.py` / `manager.py`: APP service and management facade.
- Engine adapter: `backend/engine/app/manager.py` owns BaseEngine lifecycle integration and delegates APP component operations back to this package.

## Safe defaults
Registration is metadata/configuration only: no automatic imports, instantiation, startup, or execution. Handlers are explicitly injected by the application composition root. Lifecycle transitions are explicit and do not start or stop the host process. Inventory is process-local and non-durable; DATABASE/STORAGE own persistence. Diagnostics never expose environment values or secrets. No dependency on FastAPI or API, CORE, ENGINE, SECURITY, DATABASE, STORAGE, or SERVER implementation modules.

## Component categories
API routers, middleware, exception handlers, startup hooks, shutdown hooks, background workers, and application extensions. These are descriptors and integration points, not active integrations.

## Tests
Run from repository root:

- `python -m unittest backend.app.global_ecosystem.global_app_ecosystem.test_app`
- `python -m unittest backend.engine.app.test_app_engine`

These are offline standard-library tests. Engine registration in Bootstrap does not mean registered APP components are automatically instantiated or executed.
