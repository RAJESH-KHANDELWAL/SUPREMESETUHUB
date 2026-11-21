"""Stable, dependency-free contracts for finance catalogue metadata."""

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class FinanceDomain:
    domain_id: str
    name: str
    package_ids: Tuple[str, ...]


@dataclass(frozen=True)
class FinancePackage:
    package_id: str
    package_name: str
    domain_id: str
    status: str = "REGISTERED_SCAFFOLD"
