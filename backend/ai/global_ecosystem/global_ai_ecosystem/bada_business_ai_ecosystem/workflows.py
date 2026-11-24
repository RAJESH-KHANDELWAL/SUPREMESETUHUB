"""Reusable Bada Business AI workflow descriptions; no workflow runs here."""
BADA_BUSINESS_WORKFLOWS = (
    {
        "id": "resource_question_answering",
        "steps": ["load_canonical_catalog", "identify_relevant_resources", "check_evidence", "compose_answer"],
        "approval_required": False,
    },
    {
        "id": "program_comparison",
        "steps": ["load_canonical_catalog", "select_programs", "compare_known_attributes", "report_unknowns"],
        "approval_required": False,
    },
    {
        "id": "business_learning_plan",
        "steps": ["capture_learning_goal", "identify_relevant_material", "build_learning_sequence", "define_practice"],
        "approval_required": False,
    },
    {
        "id": "business_research_brief",
        "steps": ["define_research_question", "collect_evidence", "assess_source_quality", "synthesize_findings"],
        "approval_required": False,
    },
    {
        "id": "lead_qualification",
        "steps": ["obtain_consent", "collect_minimum_context", "apply_qualification_criteria", "prepare_human_review"],
        "approval_required": True,
    },
    {
        "id": "campaign_performance_review",
        "steps": ["load_user_supplied_metrics", "validate_data", "calculate_performance", "prepare_recommendations"],
        "approval_required": False,
    },
)
