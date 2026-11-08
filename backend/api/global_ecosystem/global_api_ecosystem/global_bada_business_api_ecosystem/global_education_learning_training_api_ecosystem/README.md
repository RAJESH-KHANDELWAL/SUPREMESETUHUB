# Global Education, Learning & Training API Ecosystem

This folder is the canonical parent for the education-industry compatibility entry point and the separate student, learner and skills taxonomy. Their data models remain distinct.

## Structure

- `education_learning_training/` — canonical Education, Learning & Training implementation, catalogue, schemas, routes and tests.
- `students_education_skills_business_api_ecosystem/` — canonical student, learner and skills taxonomy package.

## Import ownership

Use the package paths under this global ecosystem. The former root-level `education_learning_training_api_ecosystem/` and `students_education_skills_business_api_ecosystem/` compatibility folders have been removed; runtime imports must target the canonical packages.

## Boundaries

This is a folder-ownership consolidation only. It does not imply live listings, connected external APIs, complete global coverage, or verified education providers. Keep the education-industry catalogue and student/skills taxonomy as separate data domains and link them using stable identifiers.
