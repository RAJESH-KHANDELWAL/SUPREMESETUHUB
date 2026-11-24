# Global Setu — Global Hub

Global Setu is the central backend hub and integration boundary for the SUPREMESETUHUB ecosystem.

## Responsibilities
- Provide a future central registry/index for ecosystem modules and their stable identifiers.
- Define navigation and discovery boundaries between independent backend domains.
- Coordinate approved API entry points without owning or duplicating their domain data.
- Keep module ownership, versioning, health/status and integration provenance explicit.

## Architecture rules
- Global Setu is an orchestration and discovery layer, not a replacement for domain services.
- General Business and Bada Business remain separate packages.
- Company, Platform, Person/Freelancer and Business remain distinct entity domains.
- Do not store credentials, tokens or secrets in public registries or documentation.
- Do not advertise an integration as connected until it has been implemented and verified.

This package currently establishes the namespace and architecture contract. Runtime registry, routing and service discovery must be implemented and tested before describing Global Setu as operational.
