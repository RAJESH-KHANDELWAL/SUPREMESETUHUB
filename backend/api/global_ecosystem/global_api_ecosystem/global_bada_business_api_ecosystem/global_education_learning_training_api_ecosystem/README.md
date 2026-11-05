# Global Education, Learning & Training API Ecosystem

This folder groups the education and learner-facing taxonomy packages without merging their data models.

## Structure

- `education_learning_training/` — compatibility entry point to the canonical industry implementation in `../industry_api_ecosystems/education_learning_training/`.
- `students_education_skills_business_api_ecosystem/` — separate student, learner and skills taxonomy package. It remains a distinct domain and is not merged into the education-industry catalogue.

## Compatibility

The previous root import paths `education_learning_training`, `education_learning_training_api_ecosystem`, and `students_education_skills_business_api_ecosystem` remain as thin compatibility facades.

## Boundaries

This is a folder-ownership consolidation only. It does not imply live listings, connected external APIs, complete global coverage, or verified education providers. Keep the education-industry catalogue and student/skills taxonomy as separate data domains and link them using stable identifiers.
