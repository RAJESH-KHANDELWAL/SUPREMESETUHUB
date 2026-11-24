from __future__ import annotations

import os
from typing import Any

from openai import OpenAI


class OpenAIImageConnector:
    """
    Real OpenAI Image API connector.

    OpenAI remains the external provider.
    SUPREMESETUHUB only sends an authorized API request.
    """

    NAME = "openai_image"
    DISPLAY_NAME = "OpenAI Image"
    OFFICIAL_API = "https://api.openai.com"

    def __init__(self) -> None:

        self.api_key = os.getenv("OPENAI_API_KEY")

        if not self.api_key:
            raise RuntimeError(
                "OPENAI_API_KEY_NOT_CONFIGURED"
            )

        self.client = OpenAI(
            api_key=self.api_key
        )

    def generate(
        self,
        prompt: str,
        model: str = "gpt-image-1",
        size: str = "1024x1024",
        quality: str = "auto",
    ) -> dict[str, Any]:

        prompt = prompt.strip()

        if not prompt:
            raise ValueError(
                "IMAGE_PROMPT_REQUIRED"
            )

        result = self.client.images.generate(
            model=model,
            prompt=prompt,
            size=size,
            quality=quality,
        )

        data = []

        for item in result.data or []:

            data.append(
                {
                    "url": getattr(
                        item,
                        "url",
                        None,
                    ),
                    "b64_json": getattr(
                        item,
                        "b64_json",
                        None,
                    ),
                }
            )

        return {
            "success": True,
            "provider": "openai",
            "connector": self.NAME,
            "model": model,
            "images": data,
        }


openai_image_connector = OpenAIImageConnector
