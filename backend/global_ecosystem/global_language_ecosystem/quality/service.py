"""Record review dimensions without pretending to score linguistic quality."""
def assess_translation_quality_metadata(*, native_reviewed: bool, terminology_checked: bool,
                                        meaning_checked: bool, locale_checked: bool,
                                        accessibility_checked: bool) -> tuple[str, ...]:
    pending = []
    for name, done in (
        ("native_speaker_review_pending", native_reviewed),
        ("terminology_review_pending", terminology_checked),
        ("meaning_fidelity_review_pending", meaning_checked),
        ("locale_review_pending", locale_checked),
        ("accessibility_review_pending", accessibility_checked),
    ):
        if not done:
            pending.append(name)
    return tuple(pending)
