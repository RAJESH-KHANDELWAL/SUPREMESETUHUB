# GLOBAL PEOPLE LIFE CORE ECOSYSTEM

**Root:** `backend/core/global_ecosystem/global_core_ecosystem/global_people_life_core_ecosystem/`  
**Parent:** GLOBAL CORE ECOSYSTEM  
**Layer:** CORE — read-only taxonomy, policy metadata, discovery and readiness

## Mission and lifecycle coverage

A shared people-and-life control plane spanning prenatal and birth stages, childhood, youth, education, work, independent living, relationships, family, wellbeing, public services, digital life, community, mobility, ageing, retirement and end-of-life transitions. Coverage is organized for people across ages 0–100+; access and content are age-appropriate.

## Canonical architecture

- `catalog.json`: backward-compatible registry of 28 existing capability/module directories.
- `domain_catalog.py`: 24 canonical domains, module-to-domain routing and service-tier mapping.
- `catalog.py`: canonical ecosystem/module registry and compatibility facade.
- `contracts.py`: tenant, actor, adult-context, secret-reference and result contracts.
- `policy.py`: privacy redaction, tenant boundary, sensitive capability classification and adult-only safeguards.
- `module_service.py`: policy-aware read-only module metadata service.
- `domain_runtime.py`: shared runtime for local domain managers.
- `orchestrator.py`: domain/module discovery, health and dependency mapping.
- `service.py`: public read-only service and global registry integration.
- `manager.py`: stable application-facing manager.
- `test_core_domains.py` and `tests/test_core_contracts.py`: structural and policy tests.
- 19 `people_*_core_ecosystem/` directories: local domain managers.
- 5 adult-only domains: references to the canonical Kamasutra ecosystem, not duplicate implementations.

## Domain coverage

1. **Life Stages and Human Development** — Human development from prenatal and birth stages through infancy, childhood, adolescence, adulthood, midlife and major life transitions, including age-appropriate development and support.
2. **Identity, Citizenship and Personal Administration** — Personal identity, civil records, documentation, accessibility of identity services, personal administration and life-event records. Sensitive identifiers remain outside Core metadata.
3. **Education, Learning and Skills** — Early learning, school, higher education, vocational learning, lifelong learning, skills, literacy, language learning, training and credentials.
4. **Career, Employment and Workforce** — Career discovery, jobs, employment, recruitment metadata, workforce development, professional transitions, remote work, freelancing and workplace life.
5. **Entrepreneurship, Livelihood and Small Business** — Self-employment, entrepreneurship, livelihood, micro and small business support, independent work and business capability discovery; detailed commercial execution belongs to Business ecosystems.
6. **Personal Finance and Life Planning** — Personal budgeting, household financial planning, savings literacy, insurance and financial-service discovery, benefits and life planning; regulated financial execution remains in Finance ecosystems.
7. **Family, Parenting and Caregiving** — Family relationships, parenting, child development, caregiving, eldercare, household coordination and family-life transitions.
8. **Personal Safety, Crisis and Survivor Support** — Personal and family safety information, safeguarding, abuse prevention, crisis navigation, survivor support and referral metadata; not an emergency-response service.
9. **Dating, Relationships, Marriage and Compatibility** — Dating, friendship, partnership, marriage, compatibility, communication, conflict navigation, separation and relationship-life education for age-appropriate audiences.
10. **Home, Household and Daily Living** — Housing and household administration, daily living, food and nutrition literacy, consumer life, routines, personal organization and independent living.
11. **Physical Health, Wellbeing and Accessibility** — General health literacy, preventive wellbeing, fitness, nutrition, disability inclusion and accessibility discovery; not diagnosis, treatment or clinical advice.
12. **Mental, Emotional and Social Wellbeing** — Emotional literacy, resilience, social connection, stress-awareness, wellbeing resources and qualified-care referral discovery; not psychotherapy or crisis intervention.
13. **Sexual and Reproductive Health Education** — Age-appropriate sexual and reproductive health education, consent literacy, puberty education and health-resource discovery with safeguarding and privacy boundaries.
14. **Digital Life and Global Digital Services** — Digital identity awareness, online participation, personal technology, digital literacy, online safety and cross-border digital-service discovery.
15. **Civic, Legal and Public Services** — Citizen services, public-benefit discovery, legal-information navigation, civic participation and government-service metadata; not legal representation or official eligibility decisions.
16. **Community, Culture, Spirituality and Belonging** — Community participation, culture, language, traditions, spirituality, social belonging, volunteering and intergenerational connection.
17. **Travel, Mobility, Leisure and Recreation** — Mobility, relocation, travel-life planning, recreation, hobbies, sports, arts, entertainment and personal interests.
18. **Ageing, Retirement and Life Transitions** — Healthy ageing information, later-life independence, retirement transitions, elder support, legacy planning and end-of-life resource discovery.
19. **Global, India and Cross-Border People Life** — Global and India-specific people-life contexts, migration and relocation information, cross-border family/work transitions and localized service discovery.
20. **Adult Intimacy, Kamasutra and Sexual Wellness 18+** — delegated to the canonical Kamasutra ecosystem.
21. **Adult Media, Pornography and Content Governance 18+** — delegated to the canonical Kamasutra ecosystem.
22. **Adult Creator Economy, Production and Work 18+** — delegated to the canonical Kamasutra ecosystem.
23. **Adult Consent, Age, Safety, Privacy and Rights 18+** — delegated to the canonical Kamasutra ecosystem.
24. **Adult Commerce, Subscriptions and Billing 18+** — delegated to Kamasutra and Finance ecosystems.

## Service levels

Normal → Basic → Standard → Premium → Professional → Enterprise → Supreme. These are service/governance levels, not separate life domains or guaranteed entitlements. Existing `normal/`, `standard/`, `premium/`, `enterprise/` and `supreme/` folders remain compatibility modules; Basic and Professional are represented in the canonical tier registry without unnecessary empty folders.

## Adult-only and safety boundary

Adult-only metadata is limited to lawful, consenting, verified adults and must be independently gated by the application. Require reliable age assurance, informed and revocable consent, rights/licensing checks, jurisdictional review, privacy-by-design, moderation, reporting and takedown. Prohibit any sexual content involving minors, non-consensual intimate imagery, coercion, trafficking, exploitation, illegal content and non-consensual recording/distribution. Kamasutra is the canonical specialist implementation; this ecosystem only provides cross-ecosystem discovery and age-policy metadata.

## Layer ownership

CORE owns taxonomy, domain routing, capability metadata, policy classification and readiness. API owns provider authentication/transport; Storage owns files; Database owns persistence and migrations; Runtime owns jobs and execution; Application owns user sessions, age assurance, consent UI and workflows. Business owns commercial execution. Finance owns regulated financial/payment operations. Health/legal/crisis decisions require qualified services.

Catalog registration does not verify identity, age, consent, legal compliance, clinical suitability, entitlement, provider support or live connectivity. No live service connection or workflow is claimed.
