# GLOBAL BADA BUSINESS TRANSPORT, LOGISTICS, SUPPLY CHAIN, SERVICE, WORK & BUSINESS CORE ECOSYSTEM

Parent: `GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM`. Status: `CORE_CATALOG_ONLY`.

Owns the business taxonomy for passenger and freight transport, road/rail/air/water operators, logistics, supply chain, courier and last mile, warehousing, cold chain, fleet services, mobility services, booking/ticketing, ports, infrastructure, rental, maintenance, finance, technology, consulting and compliance.

Python owns the canonical catalog. The manager/orchestrator/service provide read-only discovery. The PHP file is a thin interoperability facade. Core classifies service, work and business capabilities only; it does not dispatch vehicles, book journeys, execute fulfilment, track live shipments, operate warehouses, process payments, call provider APIs, store credentials or persist operational data. Those responsibilities belong to API, engine, database and storage layers. Catalog presence does not prove a business is operational or connected.
