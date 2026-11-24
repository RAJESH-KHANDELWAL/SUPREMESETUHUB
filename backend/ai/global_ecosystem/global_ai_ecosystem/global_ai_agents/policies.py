"""Default agent safety and execution policy descriptors."""
DEFAULT_AGENT_POLICY = {
    "policy_id": "global_ai_agents_default",
    "version": "1.0",
    "principles": {
        "least_privilege": True, "tool_allowlist_only": True,
        "no_implicit_external_actions": True, "no_implicit_memory_persistence": True,
        "human_approval_for_sensitive_actions": True, "validate_inputs_and_outputs": True,
    },
    "approval_triggers": [
        "external_message_or_publication", "financial_transaction",
        "account_or_permission_change", "destructive_repository_or_data_operation",
        "sensitive_personal_data_disclosure",
    ],
    "denied_by_default": [
        "unregistered_tool", "unregistered_agent", "unverified_provider",
        "missing_required_approval",
    ],
}
