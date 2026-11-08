# Recruitment

Dedicated taxonomy for employer-side and third-party recruitment services. Recruitment services are not job vacancies.

## Tracks
- `in_house_recruitment` — In-House Recruitment: Employer-operated sourcing, assessment and selection by internal hiring teams.
- `executive_search` — Executive Search: Specialist search services for senior leadership roles; scope and fee terms should be explicit.
- `contingent_recruitment` — Contingent Recruitment: Recruitment services where fees are contingent on a defined hiring outcome, if contractually stated.
- `retained_search` — Retained Search: Search engagements with a retainer-based fee structure where contractually stated.
- `technical_and_specialist_recruitment` — Technical and Specialist Recruitment: Recruitment focused on technical, professional or specialist talent.

## API
- `GET /recruitment/status`
- `GET /recruitment/tracks`
- `GET /recruitment/tracks/{track_id}`
- `GET /recruitment/search?q=...`

Capture provider identity, fee payer, service territory and licensing claims where applicable. Do not assume authorization or promise selection.
