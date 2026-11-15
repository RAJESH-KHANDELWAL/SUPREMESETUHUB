# Shift Work

Dedicated taxonomy package for shift work.

## Tracks
- `day_shift_jobs` — Day-Shift Jobs: Roles scheduled primarily in daytime hours as published by the employer.
- `evening_shift_jobs` — Evening-Shift Jobs: Roles scheduled primarily in evening hours.
- `night_shift_jobs` — Night-Shift Jobs: Roles scheduled primarily overnight; record stated hours and applicable allowances.
- `rotational_shift_jobs` — Rotational-Shift Jobs: Roles rotating between two or more stated shifts.
- `continuous_operations_shift_jobs` — Continuous-Operations Shift Jobs: Roles supporting continuous or round-the-clock operations.

## API
- `GET /shift-work/status`
- `GET /shift-work/tracks`
- `GET /shift-work/tracks/{track_id}`
- `GET /shift-work/search?q=...`

Preserve source, employer identity, role schedule or experience requirements, jurisdiction and last verification date. Taxonomy only; no live vacancies are asserted.
