# Entry-Level Jobs

Dedicated taxonomy package for entry-level jobs.

## Tracks
- `fresher_jobs` — Fresher Jobs: Roles open to applicants with limited or no prior relevant work experience where explicitly stated.
- `graduate_trainee_jobs` — Graduate Trainee Jobs: Structured trainee roles for recent graduates.
- `apprenticeships` — Apprenticeships: Formal apprenticeship pathways; preserve programme rules and jurisdiction-specific status.
- `internships` — Internships: Time-limited supervised work experience or learning placements.
- `junior_associate_jobs` — Junior Associate Jobs: Junior roles with limited experience requirements stated by the employer.

## API
- `GET /entry-level-jobs/status`
- `GET /entry-level-jobs/tracks`
- `GET /entry-level-jobs/tracks/{track_id}`
- `GET /entry-level-jobs/search?q=...`

Preserve source, employer identity, role schedule or experience requirements, jurisdiction and last verification date. Taxonomy only; no live vacancies are asserted.
