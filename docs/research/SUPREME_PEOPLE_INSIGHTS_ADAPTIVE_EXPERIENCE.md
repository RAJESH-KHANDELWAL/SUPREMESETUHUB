# SUPREME PEOPLE INSIGHTS & ADAPTIVE EXPERIENCE SYSTEM
## Research baseline and implementation requirements

**Status:** Research-informed product design baseline. It is not a census of every person, a psychological diagnosis, or proof that a particular feature is wanted by all users.

## 1. Product principle

People are not one audience. Preferences differ within the same country, language, age range, household, community and income band; they can also change by context and over time. SUPREME must not assign a fixed "mindset" to a person from nationality, religion, gender, caste, ethnicity, location or other sensitive traits. It should ask people what they want, let them skip questions, remember only what they choose to save, and let them change or delete preferences.

**Design rule:** research informs hypotheses; voluntary user choices and observed usability tests validate them. Never treat a country average as an individual's preference.

## 2. Public research reviewed

### India: language and digital access
The IAMAI–Kantar *Internet in India 2024* report states that 870 million internet users accessed Indic-language content in 2024 (reported as 98% of internet users); 57% of urban internet users said they preferred accessing internet content in Indic languages. The report also describes differences in language use and content activity.

What this supports: multilingual UI, language choice, voice/text alternatives, and testing in regional languages are important product requirements.

What it does **not** support: the idea that every Indian prefers Hindi, that language preference predicts politics/religion/personality, or that 98% of all Indian people use the internet. This is an internet-user statistic, not a census of all residents.

Source: IAMAI, Internet in India 2024: https://www.iamai.in/research/internet-india-2024-kantariamai-report
Report PDF: https://www.iamai.in/sites/default/files/research/Kantar_%20IAMAI%20report_2024_.pdf

### Cross-country values and attitudes
The World Values Survey's Wave 7 dataset covers 64 countries and societies, with more than 80,000 respondents surveyed during 2017–2022. It publishes questionnaires, country documentation and data for research. Its methodology notes that cross-country comparison needs careful sampling and comparable survey procedures.

What this supports: use transparent questions, preserve country/context metadata, examine differences and uncertainty, and avoid claiming one global personality model.

Limitations: Wave 7 data is not a live 2026 measurement of every country; survey availability and dates vary. Use current, country-specific evidence before claiming a present-day local preference.

Sources:
- Data and documentation: https://www.worldvaluessurvey.org/WVSContents.jsp?CMSID=Documentation
- Methodology: https://www.worldvaluessurvey.org/WVSContents.jsp?CMSID=WVS7MET

### Human-centred service design
OECD's Digital Government Outlook 2026 highlights that engagement should include a wider range of users and continue through a service's lifecycle. It notes that engagement can miss people facing barriers, and that systematic user-needs tracking and user testing are not consistently embedded in public services. Its 2026 report includes data from the 2025 Digital Government Index across OECD members and accession candidate countries.

What this supports: conduct research before launch, include people with access barriers, test repeatedly, measure task success and friction, and close the feedback loop.

Limits: OECD government-service findings are not a global consumer-preference survey and should not be generalized to every person or every market.

Sources:
- Digital Government Outlook 2026: https://www.oecd.org/en/publications/digital-government-outlook_0496b2bc-en/full-report/building-human-centred-and-proactive-government-services-in-the-digital-age_7cc9d8c5.html
- Serving Citizens 2026: https://www.oecd.org/en/publications/serving-citizens-2026_ecaa9c7e-en/full-report/human-centred-public-administrative-services-matter_0f903f7e.html

## 3. Initial user-needs dimensions (hypotheses to test, not labels)

Offer optional controls for:
- language and script; text, voice, captions and reading support;
- accessibility, device/data constraints, low-bandwidth mode;
- goals for this session: learn, create, find a service, connect, shop, earn, manage a business, entertainment or explore;
- discovery style: search directly, guided steps, recommendations, or browse independently;
- content format: short/long, text/audio/video, practical examples;
- personalization: off, minimal, or tailored to explicitly selected interests;
- privacy and sharing: private by default, audience controls, AI processing choices;
- price/budget range when needed for a transaction, without inferring financial status;
- experience level and desired explanation depth;
- safety/content settings and age/eligibility checks where required;
- feedback, corrections, and a one-click reset of preferences.

Do not force a user into a single persona. A user can select multiple goals, skip every question, and use the product without creating a preference profile.

## 4. Research programme: India and global markets

### Stage A — desk research
For each launch market, create an evidence register with source, publication date, sample/population, method, geography, finding, limitations, applicable feature, review owner and next review date. Prefer official statistics, peer-reviewed work, reputable survey organisations and local-language research. Never scrape private groups or buy opaque sensitive profiles.

### Stage B — consent-based discovery
Run interviews and usability sessions with diverse volunteers, including urban/rural users, different language groups, disabled users, low-bandwidth users, first-time digital users, students, workers, caregivers, creators and small-business owners. These are recruitment dimensions, not assumptions about an individual's wishes. Pay participants fairly where feasible and explain the study purpose, retention and withdrawal.

### Stage C — voluntary preference survey
Use neutral, non-leading questions; offer "none", "other", "not sure" and "prefer not to say". Translate and back-check questionnaires. Pilot for comprehension before fielding. Record recruitment method, dates, sample size, country/region, language, response rate where known and weighting method. Report sample limitations; do not describe a convenience sample as nationally representative.

### Stage D — experiments and usability
Test two or more experience variants with consent. Compare task completion, error rate, time-to-complete, abandonment, accessibility, satisfaction and complaints. Avoid optimizing only clicks, session duration, or addictive engagement. Keep a control/rollback path and publish meaningful changes to participants.

### Stage E — continuous feedback
Every feature should provide an easy "Was this useful?", report/complaint, preference edit, and delete/reset route. Review aggregate results by market and access conditions only when sample sizes are sufficient; suppress small cells to reduce re-identification risk. Retest after major changes.

## 5. Safe data model and personalization rules

- Keep preference records separate from account identity where practical; use pseudonymous IDs and least-privilege access.
- Save only preferences needed for a clear purpose, with a retention period and delete/export route.
- Treat preferences as user-declared, editable and time-stamped; provide a reason/preview for recommendations.
- No sensitive-trait inference, hidden psychological scoring, political/religious profiling, or decisions about eligibility, credit, employment or access based on inferred mindset.
- Do not infer consent from browsing, silence, friendship, or a platform account.
- Do not send user text, voice, or profile data to AI/translation providers without clear notice and the appropriate choice/permission.
- Use aggregate statistics for product decisions; never expose individual survey answers to partners or advertisers by default.
- Let people disable personalization and continue using core functionality.
- Provide multilingual privacy notices, age-appropriate flows and local legal review where required.
- Apply purpose-specific consent and revocation controls from SUPREME_GLOBAL_PERMISSIONS_AND_COLLABORATION_GOVERNANCE.md.

## 6. First-party data quality and evidence grading

Label each insight:
- `PUBLIC_RESEARCH`: published source; attach URL, date, population and limitations.
- `SUPREME_VOLUNTARY_RESEARCH`: user research conducted with consent; attach protocol, sample and retention details.
- `PRODUCT_FEEDBACK_AGGREGATE`: aggregate product feedback with minimum cohort threshold.
- `HYPOTHESIS`: unvalidated design idea.
- `VALIDATED_FOR_SCOPE`: tested for a defined population, market, language and date; not universal.
- `RETIRED`: no longer supported or too old.

Every insight should include confidence, last reviewed date, geographic scope and an expiry/review date. No unsupported claim should silently become a personalization rule.

## 7. Initial launch plan

1. Ship optional language, accessibility, content-format and recommendation controls.
2. Add a clear preference centre with view/edit/reset/delete and personalization-off controls.
3. Pilot in India with several language options and varied digital-access conditions; recruit volunteers instead of treating a single language or city as representative.
4. Publish a short research note showing methodology, sample, results and limitations.
5. Repeat in each new market with local researchers and legal/privacy review.
6. Enable personalized recommendations only after consent, tests, monitoring and rollback are ready.

## 8. Success measures

Measure: task success; time and steps to complete; accessibility failures; user-reported usefulness; language comprehension; voluntary opt-in/opt-out; preference correction/deletion completion; complaint rate; privacy/security incidents; representation gaps; and outcomes across low-bandwidth and assistive-technology use.

Do not use "time spent", click-through, or conversion alone as proof of user benefit. Review whether people achieve their stated goal safely and with less friction.

## 9. Research sources

1. IAMAI, *Internet in India 2024* (published 17 January 2025): https://www.iamai.in/research/internet-india-2024-kantariamai-report
2. World Values Survey, Wave 7 data and documentation (2017–2022): https://www.worldvaluessurvey.org/WVSContents.jsp?CMSID=Documentation
3. World Values Survey methodology: https://www.worldvaluessurvey.org/WVSContents.jsp?CMSID=WVS7MET
4. OECD, *Digital Government Outlook 2026*, human-centred public services chapter: https://www.oecd.org/en/publications/digital-government-outlook_0496b2bc-en/full-report/building-human-centred-and-proactive-government-services-in-the-digital-age_7cc9d8c5.html
5. OECD, *Serving Citizens 2026*: https://www.oecd.org/en/publications/serving-citizens-2026_ecaa9c7e-en/full-report/human-centred-public-administrative-services-matter_0f903f7e.html

**This document records a researched starting point, not a claim that all world populations have already been surveyed.**
