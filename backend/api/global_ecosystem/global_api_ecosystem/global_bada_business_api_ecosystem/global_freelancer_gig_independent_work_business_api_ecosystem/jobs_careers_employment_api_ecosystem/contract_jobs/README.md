# Contract Jobs

Dedicated taxonomy package for contract jobs.

## Tracks
- `fixed_term_employee_roles` — Fixed-Term Employee Roles: Employment under a fixed-duration employment contract.
- `independent_contractor_roles` — Independent Contractor Roles: Services engagements where the worker is classified as an independent contractor by contract and applicable law.
- `agency_contract_roles` — Agency Contract Roles: Contract roles supplied through a staffing or employment agency; legal employer must be identified.
- `project_based_contracts` — Project-Based Contracts: Time-bounded engagements tied to defined project deliverables.
- `consulting_contracts` — Consulting Contracts: Professional consulting engagements with scope, deliverables and client terms recorded.

## API
- `GET /contract-jobs/status`
- `GET /contract-jobs/tracks`
- `GET /contract-jobs/tracks/{track_id}`
- `GET /contract-jobs/search?q=...`

Taxonomy only; this package does not assert live vacancies. Preserve schedule or duration, legal worker relationship, employer/client identity, source listing and last verification date.
