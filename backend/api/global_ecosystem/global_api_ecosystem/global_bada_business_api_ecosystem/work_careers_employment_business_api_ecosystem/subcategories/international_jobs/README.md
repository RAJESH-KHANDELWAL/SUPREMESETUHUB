# International Jobs

Dedicated taxonomy package for international jobs.

## Tracks
- `overseas_employment` — Overseas Employment: Employment where the worker is hired to work in a country other than their ordinary residence.
- `international_organizations` — International Organizations: Roles with intergovernmental and international organizations; employer status and duty station must be sourced.
- `cross_border_remote_roles` — Cross-Border Remote Roles: Remote roles with explicit cross-border hiring eligibility; work authorization and payroll country remain separate.
- `expatriate_assignments` — Expatriate Assignments: Employer-sponsored international assignments with assignment duration, host location and terms recorded.
- `relocation_supported_roles` — Relocation-Supported Roles: Roles where the employer explicitly describes relocation assistance; never infer visa sponsorship.

## API
- `GET /international-jobs/status`
- `GET /international-jobs/tracks`
- `GET /international-jobs/tracks/{track_id}`
- `GET /international-jobs/search?q=...`

Taxonomy only: no live vacancy or employer verification is implied. Capture the original listing, legal employer, work location, eligibility constraints, employment relationship and last-verified timestamp.
