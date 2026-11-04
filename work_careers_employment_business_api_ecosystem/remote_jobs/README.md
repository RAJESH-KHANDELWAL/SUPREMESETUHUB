# Remote Jobs

Dedicated taxonomy for remote work arrangements.

## Tracks
- `fully_remote_jobs` — Fully Remote Jobs: Roles explicitly described as fully remote without routine office attendance.
- `remote_first_companies` — Remote-First Companies: Roles at organizations whose operating model is remote-first; verify policy from employer sources.
- `work_from_home_jobs` — Work-from-Home Jobs: Roles explicitly allowing work from the worker's home location.
- `distributed_team_roles` — Distributed-Team Roles: Roles in teams distributed across locations and time zones.
- `location_restricted_remote_jobs` — Location-Restricted Remote Jobs: Remote roles limited to specified countries, states or regions.

## API
- `GET /remote-jobs/status`
- `GET /remote-jobs/tracks`
- `GET /remote-jobs/tracks/{track_id}`
- `GET /remote-jobs/search?q=...`

Remote does not mean work-from-anywhere. Record eligible locations, time-zone expectations, employment relationship, original listing and last verification date. Taxonomy only; no live vacancies are asserted.
