# Full-Time Jobs

Dedicated taxonomy for roles explicitly classified as full-time.

## Tracks
- `permanent_full_time` — Permanent Full-Time Jobs: Ongoing full-time employment, subject to the employer's stated terms and applicable law.
- `fixed_term_full_time` — Fixed-Term Full-Time Jobs: Full-time employment for a stated or contractually bounded term.
- `graduate_full_time` — Graduate Full-Time Jobs: Full-time roles explicitly designed for graduates or early-career applicants.
- `professional_full_time` — Professional Full-Time Jobs: Full-time roles requiring professional skills or prior experience.
- `operations_full_time` — Operations Full-Time Jobs: Full-time roles in operations, delivery, production and service functions.

## API
- `GET /full-time-jobs/status`
- `GET /full-time-jobs/tracks`
- `GET /full-time-jobs/tracks/{track_id}`
- `GET /full-time-jobs/search?q=...`

Preserve employer-stated hours and applicable jurisdictional definition; do not infer statutory full-time status from a title. Taxonomy only; no live vacancies are asserted.
