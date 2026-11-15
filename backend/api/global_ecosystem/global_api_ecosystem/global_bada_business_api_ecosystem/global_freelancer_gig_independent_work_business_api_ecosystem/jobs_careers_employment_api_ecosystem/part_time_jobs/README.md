# Part-Time Jobs

Dedicated taxonomy package for part-time jobs.

## Tracks
- `regular_part_time` — Regular Part-Time Jobs: Roles with a recurring schedule below the employer's ordinary full-time schedule.
- `student_part_time` — Student Part-Time Jobs: Part-time roles suitable for students where eligibility and schedule are explicitly stated.
- `weekend_part_time` — Weekend Part-Time Jobs: Roles whose published schedule is primarily on weekends.
- `evening_part_time` — Evening Part-Time Jobs: Roles scheduled for evening hours as stated by the employer.
- `flexible_hours_part_time` — Flexible-Hours Part-Time Jobs: Part-time roles with employer-defined flexible scheduling.

## API
- `GET /part-time-jobs/status`
- `GET /part-time-jobs/tracks`
- `GET /part-time-jobs/tracks/{track_id}`
- `GET /part-time-jobs/search?q=...`

Taxonomy only; this package does not assert live vacancies. Preserve schedule or duration, legal worker relationship, employer/client identity, source listing and last verification date.
