"""Optional boto3-backed adapter for Amazon Bedrock Converse API."""
from __future__ import annotations

import os
from typing import Any

from ..adapters.contracts import ChatRequest, ChatResponse
from ..adapters.errors import ProviderConfigurationError, ProviderRequestError, ProviderTransportError
from .catalog import PROVIDER


class AWSBedrockAdapter:
    provider_id = "aws_bedrock"

    def __init__(self, *, region: str | None = None, client: Any = None):
        self.region = region or os.getenv("AWS_REGION") or os.getenv("AWS_DEFAULT_REGION")
        if not self.region:
            raise ProviderConfigurationError("Set AWS_REGION or AWS_DEFAULT_REGION for Bedrock.")
        if client is None:
            try:
                import boto3
            except ImportError as exc:
                raise ProviderConfigurationError("Install boto3 to use the AWS Bedrock adapter.") from exc
            try:
                client = boto3.client("bedrock-runtime", region_name=self.region)
            except Exception as exc:
                raise ProviderConfigurationError("Could not initialize the AWS Bedrock runtime client.") from exc
        self.client = client

    def chat(self, request: ChatRequest) -> ChatResponse:
        system = [{"text": item.content} for item in request.messages if item.role in {"system", "developer"}]
        messages = []
        for item in request.messages:
            if item.role in {"system", "developer"}:
                continue
            role = "assistant" if item.role == "assistant" else "user"
            messages.append({"role": role, "content": [{"text": item.content}]})
        kwargs: dict[str, Any] = {"modelId": request.model, "messages": messages}
        if system:
            kwargs["system"] = system
        inference = {}
        if request.max_tokens is not None:
            inference["maxTokens"] = request.max_tokens
        if request.temperature is not None:
            inference["temperature"] = request.temperature
        if inference:
            kwargs["inferenceConfig"] = inference
        try:
            result = self.client.converse(**kwargs)
        except Exception as exc:
            # Do not forward SDK exception strings: they may contain request metadata.
            raise ProviderTransportError("AWS Bedrock Converse request failed.") from exc
        message = result.get("output", {}).get("message", {})
        blocks = message.get("content", []) if isinstance(message, dict) else []
        parts = [block.get("text", "") for block in blocks if isinstance(block, dict) and isinstance(block.get("text"), str)]
        if not parts:
            raise ProviderRequestError("Bedrock response did not contain text output.")
        metadata = result.get("ResponseMetadata", {})
        return ChatResponse(
            provider_id=self.provider_id, model=request.model, content="".join(parts),
            finish_reason=result.get("stopReason"), usage=result.get("usage", {}),
            request_id=metadata.get("RequestId"), raw=result,
        )
