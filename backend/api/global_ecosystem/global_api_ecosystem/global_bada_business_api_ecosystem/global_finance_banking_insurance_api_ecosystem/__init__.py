"""Global Finance, Banking & Insurance API ecosystem entry point.

The former finance_banking_insurance and
finance_banking_insurance_api_ecosystem root packages are consolidated here.
The maintained implementation remains in industry_api_ecosystems/
finance_banking_insurance; this package exposes that implementation without
duplicating its catalogs, services, schemas, or routes.
"""
from ..finance_banking_insurance import *
from ..finance_banking_insurance import __path__
