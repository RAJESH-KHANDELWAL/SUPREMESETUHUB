# GLOBAL TRANSPORT, ROAD, RAIL, AIR & MOBILITY CORE ECOSYSTEM

Parent: `GLOBAL-CORE-ECOSYSTEM`. Status: `CORE_CATALOG_ONLY`.

Owns general transport-mode and mobility taxonomy: road, rail, air, water, public transit, personal/shared/active mobility, intermodal transport, infrastructure, traffic systems and accessibility.

Python owns the canonical catalog. The manager/orchestrator/service provide read-only discovery. The PHP file is a thin interoperability facade. Core does not calculate routes, book tickets, dispatch vehicles, operate infrastructure, call provider APIs, store credentials or persist operational data; those belong to API, engine, database and storage layers. Catalog presence is not proof of live service or connectivity.
