# GLOBAL ADULT CONTENT CORE ECOSYSTEM

**Parent:** GLOBAL CORE ECOSYSTEM  
**Related functional ecosystem:** GLOBAL ADULT ENTERTAINMENT ECOSYSTEM  
**Canonical root:** `backend/core/global_ecosystem/global_core_ecosystem/global_adult_content_core_ecosystem/`  
**Status:** `CORE_CATALOG_ONLY`

## Mission
A provider-neutral, metadata-only control plane for lawful adult-content classification and governance. It defines orientation labels, keeps identity and scene metadata separate, and exposes mandatory policy requirements for age assurance, consent, rights, moderation, privacy and jurisdiction.

## Orientation taxonomy
- `STRAIGHT` — heterosexual orientation label; use only when explicitly self-declared by the relevant adult creator/performer or supplied by an authorised rights-holder.
- `GAY` — homosexual orientation label; same self-declaration rule.
- `BISEXUAL` — bisexual orientation label; same self-declaration rule.
- `OTHER` and `UNSPECIFIED` — optional neutral values to avoid forcing a person into one of the three labels.

**Critical semantic rule:** sexual orientation is not inferred from a person's appearance, a video, a partner, or a scene. A bisexual person's orientation does not mean every scene must contain multiple genders. Participant configuration is a separate, optional content descriptor and must not be used to infer identity.

## Governance gates
A record may be marked eligible only when all required attestations are present: all depicted persons are verified adults under applicable law, documented informed consent and distribution rights exist, moderation is approved, and the content is permitted in the target jurisdiction. CORE records policy metadata only; it does not perform age verification or verify consent.

Prohibited categories include minors/CSAM, non-consensual intimate imagery, coercion, trafficking, exploitation, hidden-camera content, non-consensual synthetic/deepfake intimate imagery, and content lacking required rights.

## Layer ownership
- CORE: taxonomy, identifiers, metadata contracts and policy decision requirements.
- Application: age-gated user journeys, notices, reporting and consent interfaces.
- API: authentication, provider transports and external moderation/age-assurance integrations.
- Database: durable consent/rights/audit records and retention controls.
- Storage: protected media objects, access controls and deletion/takedown workflows.
- Engine/Runtime: moderation jobs and operational execution.

## Boundaries
No media is stored, streamed, scraped, generated or published here. No personal sexual-orientation profiles are created. No identity inference, biometric age estimation, provider API calls or live moderation is implemented. A CORE policy result is not legal advice or proof of compliance.
