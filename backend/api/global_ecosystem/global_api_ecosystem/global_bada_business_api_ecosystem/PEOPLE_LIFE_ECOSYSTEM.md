# Global People, Work & Life Discovery

This module complements the Global Bada Business taxonomy. It covers people and
life situations, education, careers, employment, entrepreneurship, households,
gender inclusion, relationships, adult education, age-restricted adult industries,
coaching, daily needs, communities, digital creators, civic services and global
locations.

## API

Mounted below the existing global business API prefix:

- `GET /api/v1/global-ecosystem/business/people-life/domains`
- `GET /api/v1/global-ecosystem/business/people-life/domains?include_adult=true`
- `GET /api/v1/global-ecosystem/business/people-life/domains/search?q=student`
- `GET /api/v1/global-ecosystem/business/people-life/domains/{domain_id}`

Adult-only domain is excluded by default and is separately gated with
`include_adult=true`. This is a classification safeguard, not a substitute for
identity/age verification, consent controls, content moderation, or legal review.

## Classification principles

- People are not reduced to a single identity: age band, life situation, work
  arrangement, gender inclusion, location and delivery channel are independent facets.
- Students, employees, job seekers, homemakers and entrepreneurs are life/work
  situations, not business sectors.
- The same service can be online, offline or hybrid.
- Country, state, city and neighbourhood context must be used for local law,
  licensing, eligibility and availability.
- The catalog is an extensible taxonomy, not a live registry of all people,
  jobs, providers or companies worldwide.

## Adult and family-safety classifications

The adult domain distinguishes consensual adult couple intimacy and lawful adult media/publishing as separate 18+ classifications. These are excluded from default discovery and require an explicit adult-content query flag. Age verification, freely given consent, privacy, performer protections and country-specific legal review are required.

Family safety, child protection, abuse prevention and survivor support are classified separately as safeguarding services, never as adult entertainment or a sexual service.
