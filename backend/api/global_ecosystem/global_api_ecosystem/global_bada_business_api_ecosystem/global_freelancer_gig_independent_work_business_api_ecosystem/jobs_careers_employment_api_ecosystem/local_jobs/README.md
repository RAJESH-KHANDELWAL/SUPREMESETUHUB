# Local Jobs

Dedicated taxonomy package for local jobs.

## Tracks
- `city_jobs` — City Jobs: Roles located within a named city and its defined commuting area.
- `district_jobs` — District Jobs: Roles located within a named administrative district.
- `neighborhood_jobs` — Neighborhood Jobs: Roles tied to a specific neighborhood or local service area.
- `rural_and_village_jobs` — Rural and Village Jobs: Roles based in rural areas and villages, with normalized locality data.
- `commuting_area_jobs` — Commuting-Area Jobs: Roles within a documented commuting region; do not infer travel time without route data.

## API
- `GET /local-jobs/status`
- `GET /local-jobs/tracks`
- `GET /local-jobs/tracks/{track_id}`
- `GET /local-jobs/search?q=...`

Taxonomy only: no live vacancy or employer verification is implied. Capture the original listing, legal employer, work location, eligibility constraints, employment relationship and last-verified timestamp.
