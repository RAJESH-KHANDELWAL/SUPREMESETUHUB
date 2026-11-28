"""Canonical software-domain taxonomy; taxonomy only, not an installed-software scan."""
from __future__ import annotations
from typing import Any
DOMAIN_DEFINITIONS: dict[str, dict[str, str]] = {
  "SOFTWARE_GOVERNANCE": {
    "name": "Software Governance",
    "purpose": "Software identity, lifecycle, classification, licensing metadata and provider governance."
  },
  "OPERATING_SYSTEMS": {
    "name": "Operating Systems",
    "purpose": "Desktop, server, mobile, embedded and real-time operating systems."
  },
  "DESKTOP_AND_PRODUCTIVITY": {
    "name": "Desktop and Productivity",
    "purpose": "Office suites, notes, calendars, collaboration clients and personal productivity."
  },
  "BUSINESS_AND_ENTERPRISE": {
    "name": "Business and Enterprise",
    "purpose": "ERP, CRM, HRM, finance, operations, enterprise resource planning and business suites."
  },
  "DEVELOPMENT_AND_IDE": {
    "name": "Development and IDE",
    "purpose": "IDEs, code editors, SDKs, compilers, build systems, debugging and developer workbenches."
  },
  "DEVOPS_AND_DELIVERY": {
    "name": "DevOps and Delivery",
    "purpose": "Source control, CI/CD, release engineering, artifact management and deployment workflows."
  },
  "CLOUD_AND_INFRASTRUCTURE": {
    "name": "Cloud and Infrastructure",
    "purpose": "Cloud platforms, infrastructure management, virtualization, containers and orchestration."
  },
  "DATABASE_AND_DATA": {
    "name": "Database and Data",
    "purpose": "Relational, document, graph, key-value, time-series databases, data platforms and ETL."
  },
  "AI_AND_MACHINE_LEARNING": {
    "name": "AI and Machine Learning",
    "purpose": "Model development, inference platforms, ML operations, generative AI and data science software."
  },
  "SECURITY_AND_PRIVACY": {
    "name": "Security and Privacy",
    "purpose": "Endpoint security, identity, access, encryption, vulnerability management and privacy tools."
  },
  "DESIGN_AND_CREATIVE": {
    "name": "Design and Creative",
    "purpose": "Graphic design, UI/UX, 3D, CAD, video, audio, animation and creative production software."
  },
  "WEB_AND_CONTENT": {
    "name": "Web and Content",
    "purpose": "CMS, website builders, e-commerce platforms, publishing, web frameworks and content systems."
  },
  "COMMUNICATION_AND_COLLABORATION": {
    "name": "Communication and Collaboration",
    "purpose": "Email clients, messaging, meetings, team collaboration and unified communications software."
  },
  "ANALYTICS_AND_OBSERVABILITY": {
    "name": "Analytics and Observability",
    "purpose": "BI, reporting, telemetry, logging, monitoring, tracing and performance analysis."
  },
  "NETWORKING_AND_SYSTEMS": {
    "name": "Networking and Systems",
    "purpose": "Network management, DNS, remote access, system administration and infrastructure utilities."
  },
  "MOBILE_AND_APPLICATIONS": {
    "name": "Mobile and Applications",
    "purpose": "Mobile applications, app frameworks, app distribution, testing and device software."
  },
  "GAMING_AND_INTERACTIVE": {
    "name": "Gaming and Interactive",
    "purpose": "Game engines, game development, launchers, simulation and interactive entertainment software."
  },
  "LICENSING_SUPPORT_AND_INTEROPERABILITY": {
    "name": "Licensing Support and Interoperability",
    "purpose": "Software licensing, subscriptions, support lifecycle, compatibility, migration and interoperability."
  }
}
def list_software_domain_inventory() -> list[dict[str, Any]]:
    return [{"domain_id": key, **value, "status":"CORE_DOMAIN_AVAILABLE", "live_connections_verified":0} for key,value in DOMAIN_DEFINITIONS.items()]
def software_domain_summary() -> dict[str, Any]:
    items=list_software_domain_inventory()
    return {"success":True,"domain_count":len(items),"domains":items,"live_connections_verified":0}
