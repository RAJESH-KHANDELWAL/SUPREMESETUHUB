# Staffing Services

Dedicated taxonomy for workforce supply and staffing services. Staffing services are not themselves job vacancies.

## Tracks
- `temporary_staffing` — Temporary Staffing: Supply of temporary workers for time-limited workforce needs.
- `contract_staffing` — Contract Staffing: Supply or administration of contract workers; legal employer and end client must be distinguished.
- `permanent_staffing` — Permanent Staffing: Workforce sourcing and staffing services for ongoing employment positions.
- `managed_workforce_services` — Managed Workforce Services: Managed services for workforce planning, supply or administration under defined service terms.
- `employer_of_record_services` — Employer-of-Record Services: Services where a provider acts as legal employer in a jurisdiction, subject to local law and verified contractual arrangements.

## API
- `GET /staffing/status`
- `GET /staffing/tracks`
- `GET /staffing/tracks/{track_id}`
- `GET /staffing/search?q=...`

Identify the legal employer, intermediary and end client separately when known. Do not treat marketing claims as proof of worker classification or legal compliance.
