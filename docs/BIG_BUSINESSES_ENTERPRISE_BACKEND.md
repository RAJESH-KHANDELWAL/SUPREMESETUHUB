# SUPREMESETUHUB — Big Businesses Backend

## Scope
The existing Businesses domain remains the canonical source of records. This upgrade adds an enterprise profile and a parallel `/big-businesses` API namespace while preserving existing `/businesses` routes and response fields.

## Enterprise profile fields
- Legal name and business type (including large business and enterprise)
- Industry, headquarters and employee count
- Revenue band and operating regions
- Parent-company reference
- Departments and tags
- Compliance status metadata

All new fields are optional, preserving requests from older clients. Employee counts are bounded and non-negative; business type values are allowlisted in the service. Existing authenticated owner scoping and server-generated IDs are retained.

## Routes
- `GET /big-businesses/` — owner-scoped portfolio
- `GET /big-businesses/overview` — portfolio counts and supported capability summary
- `POST /big-businesses/` — create a business using the expanded optional profile
- `GET /big-businesses/{business_id}` — owner-scoped record details

The legacy `/businesses` routes remain available. Both namespaces share the same controller and records rather than maintaining duplicate copies.

## Explicit limitations
The current BusinessService stores records in process memory. This change does not claim durable storage, multi-tenant database isolation across workers, consolidated financial reporting, HR/payroll, workflow approvals, or compliance certification. Those require persistent schema/migrations, tenant-scoped database authorization, audit trails and integration tests before production enterprise use.
