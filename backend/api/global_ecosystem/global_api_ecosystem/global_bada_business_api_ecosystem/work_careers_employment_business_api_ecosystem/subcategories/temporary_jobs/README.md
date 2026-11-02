# Temporary Jobs

Dedicated taxonomy package for time-limited roles.

## Tracks
- `short_term_temporary_roles` — Short-Term Temporary Roles: Roles intended to cover a short and limited period.
- `seasonal_temporary_roles` — Seasonal Temporary Roles: Temporary roles linked to seasonal demand.
- `temporary_replacement_roles` — Temporary Replacement Roles: Temporary cover for leave, absence or a vacancy pending permanent recruitment.
- `agency_temporary_roles` — Agency Temporary Roles: Temporary workers supplied through an agency; agency and end client should be distinguished.
- `event_temporary_roles` — Event-Based Temporary Roles: Temporary roles for a defined event, exhibition, campaign or production.

## API
- `GET /temporary-jobs/status`
- `GET /temporary-jobs/tracks`
- `GET /temporary-jobs/tracks/{track_id}`
- `GET /temporary-jobs/search?q=...`

Preserve start/end dates only when stated. Do not assume benefits or conversion to permanent employment. Taxonomy only; no live vacancies are asserted.
