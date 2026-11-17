# ADULT MEDIA PORNOGRAPHY 18 PLUS

Legal and policy metadata for lawful adult media; excludes exploitative and non-consensual material.

Parent registry: `global_people_life_core_ecosystem/catalog.py`.

CORE boundary: this domain contains classification and governance metadata only. It does not assert a live service, legal compliance, clinical suitability or external provider integration.

Access boundary: lawful verified adults only. Applications must independently implement age assurance, informed consent, rights/licensing, jurisdictional review, privacy, moderation and takedown. Never permit sexual content involving minors, non-consensual intimate imagery, coercion, trafficking or exploitation.

## Canonical classification taxonomy

The canonical classification contract lives in this existing People Life CORE domain:
- `taxonomy.py`
- `classification_taxonomy.json`
- `AdultMediaClassificationContract.php`

Optional content labels: `STRAIGHT`, `GAY`, `BISEXUAL`, `OTHER`, `UNSPECIFIED`.
Participant configuration is a separate field and must never be used to infer orientation.

A non-unspecified label is accepted only for a creator/performer when it is self-declared or supplied by an authorised rights-holder. Never infer orientation from a scene, appearance, partner, behaviour or browsing history. Never create viewer/user orientation profiles. The taxonomy is metadata only and does not verify age, identity, consent, rights or legal compliance.
