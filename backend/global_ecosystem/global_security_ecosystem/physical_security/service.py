"""Facility access governance metadata."""
def validate_facility_access(*, named_sponsor, identity_checked, access_expiry, visitor_logged):
    issues=[]
    if not named_sponsor: issues.append("sponsor_required")
    if not identity_checked: issues.append("identity_check_required")
    if not access_expiry: issues.append("time_limited_access_required")
    if not visitor_logged: issues.append("visitor_log_required")
    return tuple(issues)
