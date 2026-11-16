"""Authorized security-test planning checks only."""
def validate_test_plan(*, written_authorization, target_scope, test_window, emergency_contact):
    issues=[]
    if not written_authorization: issues.append("written_authorization_required")
    if not target_scope.strip(): issues.append("explicit_target_scope_required")
    if not test_window.strip(): issues.append("approved_test_window_required")
    if not emergency_contact.strip(): issues.append("emergency_contact_required")
    return tuple(issues)
