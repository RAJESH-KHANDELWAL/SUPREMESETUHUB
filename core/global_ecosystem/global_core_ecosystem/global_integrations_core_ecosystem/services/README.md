# Services boundary

Services expose read-only discovery and metadata operations for provider and domain catalogs. They must not perform network requests, create provider resources, process payments or persist customer payloads. Runtime orchestration belongs to ENGINE and API.
