"""Typed models for language-domain metadata."""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class LanguageProfile:
    language_code: str
    display_name: str
    script: str | None = None
    region: str | None = None
    direction: str = "ltr"
    aliases: tuple[str, ...] = field(default_factory=tuple)

    def __post_init__(self) -> None:
        if not self.language_code or not self.display_name:
            raise ValueError("language_code and display_name are required")
        if self.direction not in {"ltr", "rtl"}:
            raise ValueError("direction must be 'ltr' or 'rtl'")
