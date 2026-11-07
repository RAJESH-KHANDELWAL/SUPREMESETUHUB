from __future__ import annotations

from typing import Any


class SupremeOrchestrator:
    """
    SUPREME PERSONAL AI request-routing layer.

    It identifies the primary capability required for a request.
    Actual execution is handled by the appropriate engine/service.
    """

    CAPABILITIES = {
        "chat",
        "memory",
        "research",
        "files",
        "github",
        "wordpress",
        "business",
        "content",
        "code",
        "automation",
        "image",
        "video",
        "audio",
        "speech",
        "design",
    }

    ROUTING_RULES = (
        (
            "github",
            (
                "github",
                "repository",
                "repo",
                "commit",
                "pull request",
                "branch",
                "workflow",
            ),
        ),
        (
            "wordpress",
            (
                "wordpress",
                "plugin",
                "woocommerce",
                "gutenberg",
                "website",
            ),
        ),
        (
            "memory",
            (
                "remember",
                "memory",
                "forget",
                "save this",
            ),
        ),
        (
            "research",
            (
                "research",
                "search",
                "investigate",
                "compare",
                "verify",
            ),
        ),
        (
            "code",
            (
                "code",
                "python",
                "php",
                "javascript",
                "typescript",
                "api",
                "bug",
                "error",
            ),
        ),
        (
            "business",
            (
                "business",
                "sales",
                "lead",
                "customer",
                "revenue",
                "marketing",
            ),
        ),
        (
            "content",
            (
                "post",
                "blog",
                "caption",
                "copy",
                "content",
                "article",
            ),
        ),
        (
            "automation",
            (
                "automate",
                "automation",
                "schedule",
                "reminder",
                "workflow",
            ),
        ),
        (
            "image",
            (
                "image",
                "poster",
                "logo",
                "picture",
            ),
        ),
        (
            "video",
            (
                "video",
                "reel",
                "movie",
            ),
        ),
        (
            "audio",
            (
                "audio",
                "music",
                "sound",
            ),
        ),
        (
            "speech",
            (
                "speech",
                "voice",
                "transcribe",
            ),
        ),
        (
            "design",
            (
                "design",
                "ui",
                "ux",
                "figma",
                "prototype",
            ),
        ),
    )

    def classify(self, request: str) -> str:
        """
        Identify the primary capability for a user request.
        """

        text = request.strip().lower()

        if not text:
            return "chat"

        for capability, keywords in self.ROUTING_RULES:
            if any(keyword in text for keyword in keywords):
                return capability

        return "chat"

    def supported(self, capability: str) -> bool:
        return capability.strip().lower() in self.CAPABILITIES

    def plan(
        self,
        request: str,
    ) -> dict[str, Any]:
        """
        Create a routing plan without executing the request.
        """

        request = request.strip()

        if not request:
            raise ValueError("SUPREME_REQUEST_REQUIRED")

        capability = self.classify(request)

        return {
            "success": True,
            "request": request,
            "capability": capability,
            "status": "READY",
            "execution": "PENDING",
        }

    def capabilities(self) -> list[str]:
        return sorted(self.CAPABILITIES)
