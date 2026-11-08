"""OpenAI Responses API adapter for Global Business Ecosystem intelligence.

Credentials are read only from server-side environment variables. Business
contact details, arbitrary metadata and secrets are deliberately excluded from
the model context.
"""
from __future__ import annotations

import json
import os
from typing import Any

from .providers import BusinessAIProvider, ProviderDescriptor


class OpenAIBusinessAIProvider(BusinessAIProvider):
    """Optional live LLM adapter for business analysis and planning."""

    SAFE_CONTEXT_FIELDS = (
        "business_id", "name", "legal_name", "category", "industry",
        "business_type", "location", "headquarters", "website",
        "employee_count", "annual_revenue_band", "operating_regions",
        "departments", "tags", "compliance_status", "verified",
    )

    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY", "").strip()
        self.model = os.getenv("GLOBAL_BUSINESS_AI_MODEL", "gpt-4.1-mini").strip()
        self._client = None
        self._verified_live = False
        if self.api_key:
            from openai import OpenAI
            self._client = OpenAI(api_key=self.api_key, timeout=45.0, max_retries=1)

    @property
    def descriptor(self) -> ProviderDescriptor:
        return ProviderDescriptor(
            provider_id="openai",
            capability="business_analysis",
            enabled=bool(self._client),
            live=self._verified_live,
            requires_credentials=True,
        )

    @classmethod
    def safe_context(cls, context: dict[str, Any]) -> dict[str, Any]:
        """Allow-list business facts; exclude contact data and arbitrary metadata."""
        return {
            key: context[key]
            for key in cls.SAFE_CONTEXT_FIELDS
            if key in context and context[key] is not None
        }

    def analyze(self, *, task: str, business_context: dict[str, Any]) -> dict[str, Any]:
        if self._client is None:
            raise RuntimeError("OPENAI_API_KEY_NOT_CONFIGURED")
        prompt = task.strip()
        if not prompt:
            raise ValueError("BUSINESS_AI_TASK_REQUIRED")
        if len(prompt) > 4000:
            raise ValueError("BUSINESS_AI_TASK_TOO_LONG")

        safe_context = self.safe_context(business_context)
        response = self._client.responses.create(
            model=self.model,
            instructions=(
                "You are a rigorous global business strategy and operations analyst. "
                "Use only the supplied business context and clearly distinguish facts, "
                "assumptions, hypotheses, and recommendations. Do not invent market data, "
                "customers, revenue, legal status, certifications, or provider integrations. "
                "For legal, tax, investment, credit, and regulatory matters, identify the "
                "need for qualified professional review. Give practical prioritized actions, "
                "risks, dependencies, and measurable validation steps. If evidence is missing, "
                "say so explicitly. Respond in the language used in the task."
            ),
            input=(
                "BUSINESS CONTEXT (user-supplied; unverified):\n"
                + json.dumps(safe_context, ensure_ascii=False, default=str)
                + "\n\nANALYSIS REQUEST:\n"
                + prompt
            ),
            max_output_tokens=1200,
        )
        analysis = (getattr(response, "output_text", None) or "").strip()
        if not analysis:
            raise RuntimeError("OPENAI_EMPTY_BUSINESS_ANALYSIS")
        self._verified_live = True
        return {
            "provider": "openai",
            "model": self.model,
            "analysis": analysis,
            "context_fields_used": sorted(safe_context),
            "external_verification": False,
        }
