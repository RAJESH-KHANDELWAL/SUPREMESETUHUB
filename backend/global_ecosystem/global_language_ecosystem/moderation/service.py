"""Policy flags for language content workflows; not an automated classifier."""
PROHIBITED_FLAGS = ("sexual_content_involving_minors", "non_consensual_intimate_imagery", "coercion_or_exploitation", "trafficking", "sexual_extortion")
REVIEW_FLAGS = ("age_assurance_required", "consent_review_required", "privacy_review_required", "jurisdiction_review_required")
def review_content_policy_flags(flags: tuple[str, ...]) -> tuple[str, ...]:
 known = set(PROHIBITED_FLAGS) | set(REVIEW_FLAGS)
 return tuple(sorted(set(flags) & known))
