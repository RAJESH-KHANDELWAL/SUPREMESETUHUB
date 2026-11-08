"""Explainable, deterministic business intelligence for Global Business Ecosystem.

This module deliberately does not claim to call an LLM, government registry,
credit bureau, or live market-data provider. It derives transparent signals
from the business profile supplied by an authorized caller.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Mapping


@dataclass(frozen=True)
class IntelligenceSignal:
    code: str
    level: str
    score: int
    title: str
    explanation: str
    action: str


@dataclass(frozen=True)
class BusinessAssessment:
    business_id: str
    profile_completeness: int
    readiness_score: int
    maturity_band: str
    signals: tuple[IntelligenceSignal, ...]
    recommendations: tuple[str, ...]
    assumptions: tuple[str, ...]
    generated_by: str = "SUPREMESETUHUB_RULE_ENGINE"
    external_verification: bool = False

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["signals"] = [asdict(signal) for signal in self.signals]
        result["recommendations"] = list(self.recommendations)
        result["assumptions"] = list(self.assumptions)
        return result


class BusinessIntelligence:
    """Produces explainable profile, readiness and risk insights."""

    REQUIRED_FIELDS = ("name", "industry", "business_type", "location")
    COMPLETENESS_FIELDS = (
        "name", "legal_name", "category", "industry", "business_type",
        "location", "headquarters", "website", "public_contact",
        "employee_count", "annual_revenue_band", "operating_regions",
        "departments", "tags", "compliance_status",
    )

    @staticmethod
    def _value(profile: Any, key: str, default: Any = None) -> Any:
        if isinstance(profile, Mapping):
            return profile.get(key, default)
        return getattr(profile, key, default)

    @staticmethod
    def _present(value: Any) -> bool:
        if value is None:
            return False
        if isinstance(value, str):
            return bool(value.strip())
        if isinstance(value, (list, tuple, set, dict)):
            return bool(value)
        return True

    def assess(self, profile: Any) -> BusinessAssessment:
        business_id = str(self._value(profile, "business_id", "") or "")
        if not business_id:
            raise ValueError("business_id is required for assessment")

        populated = [
            field for field in self.COMPLETENESS_FIELDS
            if self._present(self._value(profile, field))
        ]
        completeness = round(100 * len(populated) / len(self.COMPLETENESS_FIELDS))
        signals: list[IntelligenceSignal] = []
        recommendations: list[str] = []

        for field in self.REQUIRED_FIELDS:
            if not self._present(self._value(profile, field)):
                signals.append(IntelligenceSignal(
                    code=f"MISSING_{field.upper()}",
                    level="WARNING",
                    score=8,
                    title=f"Missing {field.replace('_', ' ')}",
                    explanation=f"The profile does not contain {field.replace('_', ' ')}.",
                    action=f"Add a verified {field.replace('_', ' ')} value to improve assessment quality.",
                ))

        if not self._present(self._value(profile, "website")):
            recommendations.append("Add an official website or a verified public business page.")
        if not self._present(self._value(profile, "public_contact")):
            recommendations.append("Add a business-controlled public contact channel.")
        if not self._present(self._value(profile, "operating_regions")):
            recommendations.append("Define the regions where the business currently operates.")
        if not self._present(self._value(profile, "departments")):
            recommendations.append("Document core functions such as sales, operations, finance and customer support.")
        compliance = str(self._value(profile, "compliance_status", "UNSPECIFIED") or "UNSPECIFIED").upper()
        if compliance in {"UNSPECIFIED", "UNDER_REVIEW"}:
            signals.append(IntelligenceSignal(
                code="COMPLIANCE_EVIDENCE_INCOMPLETE",
                level="CAUTION",
                score=12,
                title="Compliance needs review",
                explanation="The profile does not establish a completed compliance assessment.",
                action="Have an appropriately qualified professional review applicable registrations, licences and filings.",
            ))
            recommendations.append("Review applicable legal, tax, labour and sector-specific obligations with a qualified professional.")
        elif compliance == "NON_COMPLIANT":
            signals.append(IntelligenceSignal(
                code="COMPLIANCE_NON_COMPLIANT_DECLARED",
                level="CRITICAL",
                score=25,
                title="Compliance issue declared",
                explanation="The business profile declares a non-compliant status; the engine cannot independently verify it.",
                action="Escalate to a qualified compliance professional and record corrective actions.",
            ))

        if self._value(profile, "verified", False) is not True:
            signals.append(IntelligenceSignal(
                code="BUSINESS_NOT_PLATFORM_VERIFIED",
                level="INFO",
                score=5,
                title="Platform verification not recorded",
                explanation="The profile's verified flag is not true.",
                action="Use the platform's authorized verification workflow; do not treat this assessment as verification.",
            ))

        penalty = min(50, sum(signal.score for signal in signals))
        readiness = max(0, min(100, round(completeness - penalty / 2)))
        maturity = (
            "FOUNDATION" if readiness < 40 else
            "DEVELOPING" if readiness < 65 else
            "ESTABLISHED" if readiness < 85 else "WELL_DOCUMENTED"
        )
        if not recommendations:
            recommendations.append("Maintain profile accuracy and schedule periodic operational and compliance reviews.")

        return BusinessAssessment(
            business_id=business_id,
            profile_completeness=completeness,
            readiness_score=readiness,
            maturity_band=maturity,
            signals=tuple(signals),
            recommendations=tuple(recommendations),
            assumptions=(
                "Scores describe profile documentation, not business profitability or creditworthiness.",
                "User-supplied values are not independently verified.",
                "No external registry, government service, credit bureau or live market feed was queried.",
            ),
        )

    def compare(self, profiles: list[Any]) -> list[dict[str, Any]]:
        """Assess multiple profiles independently; does not imply market ranking."""
        results = [self.assess(profile).to_dict() for profile in profiles]
        return sorted(results, key=lambda item: (-item["readiness_score"], item["business_id"]))
