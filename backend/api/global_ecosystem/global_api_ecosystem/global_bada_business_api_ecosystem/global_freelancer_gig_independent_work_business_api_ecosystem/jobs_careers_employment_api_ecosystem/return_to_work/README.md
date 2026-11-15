# Return-to-Work Opportunities

Dedicated taxonomy for structured pathways and roles supporting employment re-entry.

## Tracks
- `returnship_programmes` — Returnship Programmes: Structured employer programmes supporting professionals returning after a career break.
- `career_reentry_roles` — Career Re-Entry Roles: Roles explicitly open to applicants returning after time away from paid employment.
- `flexible_reentry_jobs` — Flexible Re-Entry Jobs: Return-to-work roles with stated flexible schedules or arrangements.
- `refresher_and_retraining_pathways` — Refresher and Retraining Pathways: Programmes offering documented refresher training or skills updates before or during re-entry.
- `experienced_returner_roles` — Experienced Returner Roles: Roles that value prior professional experience while allowing a career re-entry.

## API
- `GET /return-to-work/status`
- `GET /return-to-work/tracks`
- `GET /return-to-work/tracks/{track_id}`
- `GET /return-to-work/search?q=...`

Avoid collecting or inferring sensitive reasons for a career break. Capture programme eligibility only from official sources. Taxonomy only; no live vacancies are asserted.
