# Hybrid Jobs

Dedicated taxonomy for roles combining on-site and remote work.

## Tracks
- `office_remote_hybrid` — Office and Remote Hybrid Jobs: Roles combining employer-site attendance and remote work.
- `field_office_hybrid` — Field and Office Hybrid Jobs: Roles combining field visits with office-based duties.
- `fixed_day_hybrid` — Fixed-Day Hybrid Jobs: Roles with a stated recurring office-day schedule.
- `flexible_hybrid` — Flexible Hybrid Jobs: Roles where office attendance is flexible but still subject to employer policy.
- `multi_location_hybrid` — Multi-Location Hybrid Jobs: Roles involving more than one worksite plus remote work.

## API
- `GET /hybrid-jobs/status`
- `GET /hybrid-jobs/tracks`
- `GET /hybrid-jobs/tracks/{track_id}`
- `GET /hybrid-jobs/search?q=...`

Capture office location, required attendance cadence and policy source. Occasional travel alone does not make a role hybrid. Taxonomy only; no live vacancies are asserted.
