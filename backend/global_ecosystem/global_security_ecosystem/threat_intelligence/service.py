"""Threat indicator metadata validation; does not execute or fetch indicators."""
def validate_threat_indicator(*, indicator_type, value, source, observed_at, confidence):
    issues=[]
    if indicator_type not in {"domain", "ip", "url", "file_hash", "email", "cve"}: issues.append("unsupported_indicator_type")
    if not value.strip(): issues.append("indicator_value_required")
    if not source.strip(): issues.append("source_attribution_required")
    if not observed_at.strip(): issues.append("observation_time_required")
    if not 0 <= confidence <= 100: issues.append("confidence_must_be_0_to_100")
    return tuple(issues)
