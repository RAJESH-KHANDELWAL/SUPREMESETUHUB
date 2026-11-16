"""Tool capability descriptors; actual tool execution belongs to ENGINE."""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class AgentToolContract:
    tool_id: str
    description: str
    risk_level: str = "low"
    approval_required: bool = False
    input_schema_ref: str | None = None

    def validate(self) -> None:
        if not self.tool_id.strip():
            raise ValueError("AI_AGENT_TOOL_ID_REQUIRED")
        if self.risk_level not in {"low", "medium", "high", "critical"}:
            raise ValueError("AI_AGENT_TOOL_RISK_INVALID")
        if self.risk_level in {"high", "critical"} and not self.approval_required:
            raise ValueError("AI_AGENT_HIGH_RISK_TOOL_REQUIRES_APPROVAL")

DEFAULT_TOOL_CONTRACTS = (
    AgentToolContract("search", "Retrieve external information.", "medium"),
    AgentToolContract("document_reader", "Read explicitly supplied documents.", "low"),
    AgentToolContract("calculator", "Perform deterministic calculations.", "low"),
    AgentToolContract("repository_reader", "Read repository files and metadata.", "medium"),
    AgentToolContract("test_runner", "Run configured repository tests.", "medium"),
    AgentToolContract("repository_writer", "Modify repository content.", "high", True),
    AgentToolContract("external_publisher", "Publish content to an external service.", "high", True),
)
