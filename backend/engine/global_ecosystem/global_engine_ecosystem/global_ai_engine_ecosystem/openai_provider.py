"""OpenAI text-inference adapter owned by GLOBAL AI ENGINE ECOSYSTEM."""
from __future__ import annotations

import json
import os
from typing import Any


class OpenAITextEngine:
    """Executes text-generation requests through the OpenAI Responses API."""

    PROVIDER_ID = "openai"
    CAPABILITY = "text"

    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY", "").strip()
        self.model = os.getenv("GLOBAL_AI_MODEL", "gpt-4.1-mini").strip()
        self._client = None
        self._live_verified = False
        if self.api_key:
            from openai import OpenAI
            self._client = OpenAI(api_key=self.api_key, timeout=60.0, max_retries=1)

    def status(self) -> dict[str, Any]:
        return {
            "provider_id": self.PROVIDER_ID,
            "capabilities": [self.CAPABILITY],
            "model": self.model,
            "enabled": self._client is not None,
            "live_verified": self._live_verified,
            "credential_source": "SERVER_ENVIRONMENT",
        }

    def generate(self, *, task: str, context: dict[str, Any] | None = None, model_id: str | None = None) -> dict[str, Any]:
        if self._client is None:
            raise RuntimeError("OPENAI_API_KEY_NOT_CONFIGURED")
        prompt = task.strip()
        if not prompt:
            raise ValueError("AI_TASK_REQUIRED")
        if len(prompt) > 12000:
            raise ValueError("AI_TASK_TOO_LONG")
        safe_context = context or {}
        context_json = json.dumps(safe_context, ensure_ascii=False, default=str)
        if len(context_json) > 12000:
            raise ValueError("AI_CONTEXT_TOO_LARGE")

        response = self._client.responses.create(
            model=model_id or self.model,
            instructions=(
                "You are the intelligence assistant for SUPREMESETUHUB GLOBAL AI ECOSYSTEM. "
                "Be accurate, structured and explicit about uncertainty. Separate supplied "
                "facts from assumptions and recommendations. Never fabricate live data, "
                "citations, external verification, or actions. Do not claim to have executed "
                "tools or changed systems unless the caller confirms that separately. "
                "For legal, medical, financial and regulatory topics, identify limits and "
                "recommend qualified professional review where appropriate."
            ),
            input=(
                "CONTEXT (unverified caller-supplied data):\n"
                + context_json
                + "\n\nTASK:\n"
                + prompt
            ),
            max_output_tokens=1800,
        )
        output = (getattr(response, "output_text", None) or "").strip()
        if not output:
            raise RuntimeError("OPENAI_EMPTY_RESPONSE")
        self._live_verified = True
        usage = getattr(response, "usage", None)
        return {
            "provider": self.PROVIDER_ID,
            "model": model_id or self.model,
            "output": output,
            "live_verified": True,
            "usage": {
                "input_tokens": getattr(usage, "input_tokens", None),
                "output_tokens": getattr(usage, "output_tokens", None),
            } if usage else None,
        }
