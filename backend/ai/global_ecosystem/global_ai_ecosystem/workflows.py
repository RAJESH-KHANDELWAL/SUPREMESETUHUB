"""Reusable workflow patterns and their required control points."""
from .schemas import CatalogRecord

WORKFLOWS = tuple(
    CatalogRecord(key, name, "workflow_pattern", description, metadata={"approval_required": approval})
    for key, name, description, approval in (
        ("retrieve_and_answer", "Retrieve and answer", "Retrieve evidence, rerank it and generate a grounded response.", False),
        ("document_pipeline", "Document pipeline", "Ingest, parse, classify, extract and validate documents.", False),
        ("research_pipeline", "Research pipeline", "Plan research, collect sources, synthesize and cite findings.", False),
        ("content_creation", "Content creation", "Create and evaluate text or media assets.", False),
        ("human_approved_action", "Human-approved action", "Prepare an external action and wait for explicit approval.", True),
    )
)
