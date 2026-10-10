
"""Registry for GLOBAL ECOSYSTEM and its registered identities."""

from typing import Dict, List, Optional

from .models import GlobalEcosystemIdentity

GLOBAL_ECOSYSTEM_ID = "GLOBAL-ECOSYSTEM"
GLOBAL_ECOSYSTEM_NAME = "GLOBAL ECOSYSTEM"


class GlobalEcosystemRegistry:
    """Central registry for the GLOBAL ECOSYSTEM hierarchy."""

    def __init__(self) -> None:
        self.ecosystems: Dict[str, GlobalEcosystemIdentity] = {}

        # MASTER PARENT
        self._register(
            GLOBAL_ECOSYSTEM_ID,
            GLOBAL_ECOSYSTEM_NAME,
            "MASTER",
            capabilities=[
                "CENTRAL_REGISTRY",
                "HIERARCHY",
                "DISCOVERY",
                "GOVERNANCE",
            ],
        )

        # GLOBAL ECOSYSTEM CATEGORIES
        categories = [
            (
                "GLOBAL-SUPREME-ECOSYSTEM",
                "GLOBAL SUPREME ECOSYSTEM",
                "CORE",
                ["ADMINISTRATION", "PLATFORM_CONTROL", "INTEGRATION"],
            ),
            (
                "GLOBAL-PEOPLE-ECOSYSTEM",
                "GLOBAL PEOPLE ECOSYSTEM",
                "AUDIENCE",
                ["IDENTITY", "PROFILE", "COMMUNITY"],
            ),
            (
                "GLOBAL-BUSINESS-ECOSYSTEM",
                "GLOBAL BUSINESS ECOSYSTEM",
                "AUDIENCE",
                ["ORGANIZATION", "BUSINESS", "TEAM", "PROJECTS"],
            ),
            (
                "GLOBAL-ENTREPRENEUR-ECOSYSTEM",
                "GLOBAL ENTREPRENEUR ECOSYSTEM",
                "AUDIENCE",
                ["STARTUPS", "VENTURES", "BUSINESS_DEVELOPMENT"],
            ),
            (
                "GLOBAL-CLOUD-ECOSYSTEM",
                "GLOBAL CLOUD ECOSYSTEM",
                "FUNCTIONAL",
                ["COMPUTE", "INFRASTRUCTURE", "NETWORKING"],
            ),
            (
                "GLOBAL-CLOUD-STORAGE-ECOSYSTEM",
                "GLOBAL CLOUD STORAGE ECOSYSTEM",
                "FUNCTIONAL",
                ["OBJECT_STORAGE", "FILE_STORAGE", "DATA_STORAGE"],
            ),
            (
                "GLOBAL-STORAGE-ECOSYSTEM",
                "GLOBAL STORAGE ECOSYSTEM",
                "FUNCTIONAL",
                ["STORAGE_CATALOG", "ADAPTERS", "ASSET_METADATA"],
            ),
            (
                "GLOBAL-SERVER-ECOSYSTEM",
                "GLOBAL SERVER ECOSYSTEM",
                "FUNCTIONAL",
                ["SERVER_MANAGEMENT", "DEPLOYMENT", "MONITORING"],
            ),
            (
                "GLOBAL-WEB-HOSTING-ECOSYSTEM",
                "GLOBAL WEB & HOSTING ECOSYSTEM",
                "FUNCTIONAL",
                ["WEBSITES", "DOMAINS", "HOSTING", "CMS"],
            ),
            (
                "GLOBAL-SOCIAL-MEDIA-ECOSYSTEM",
                "GLOBAL SOCIAL MEDIA ECOSYSTEM",
                "FUNCTIONAL",
                ["SOCIAL_NETWORKS", "PUBLISHING", "COMMUNITIES"],
            ),
            (
                "GLOBAL-CREATOR-MEDIA-ECOSYSTEM",
                "GLOBAL CREATOR & MEDIA ECOSYSTEM",
                "FUNCTIONAL",
                ["CREATOR_TOOLS", "MEDIA", "PUBLISHING", "MONETIZATION"],
            ),
            (
                "GLOBAL-ADULT-ENTERTAINMENT-ECOSYSTEM",
                "GLOBAL ADULT ENTERTAINMENT ECOSYSTEM",
                "FUNCTIONAL",
                ["AGE_RESTRICTED_SERVICES", "CREATOR_SERVICES", "PLATFORM_DISCOVERY"],
            ),
            (
                "GLOBAL-AI-AUTOMATION-ECOSYSTEM",
                "GLOBAL AI & AUTOMATION ECOSYSTEM",
                "FUNCTIONAL",
                ["AI_MODELS", "AI_APIS", "AUTOMATION"],
            ),
            (
                "GLOBAL-PAYMENT-COMMERCE-ECOSYSTEM",
                "GLOBAL PAYMENT & COMMERCE ECOSYSTEM",
                "FUNCTIONAL",
                ["PAYMENTS", "BILLING", "SUBSCRIPTIONS", "COMMERCE"],
            ),
            (
                "GLOBAL-IDENTITY-SECURITY-ECOSYSTEM",
                "GLOBAL IDENTITY & SECURITY ECOSYSTEM",
                "FUNCTIONAL",
                ["AUTHENTICATION", "AUTHORIZATION", "PRIVACY"],
            ),
            (
                "GLOBAL-COMMUNICATION-ECOSYSTEM",
                "GLOBAL COMMUNICATION ECOSYSTEM",
                "FUNCTIONAL",
                ["EMAIL", "MESSAGING", "NOTIFICATIONS"],
            ),
            (
                "GLOBAL-DATA-DATABASE-ECOSYSTEM",
                "GLOBAL DATA & DATABASE ECOSYSTEM",
                "FUNCTIONAL",
                ["DATABASES", "DATA_EXCHANGE", "ANALYTICS"],
            ),
            (
                "GLOBAL-DEVELOPER-ECOSYSTEM",
                "GLOBAL DEVELOPER ECOSYSTEM",
                "FUNCTIONAL",
                ["APIS", "SDKS", "REPOSITORIES", "CI_CD"],
            ),
        ]

        for ecosystem_id, name, ecosystem_type, capabilities in categories:
            metadata = {}

            if ecosystem_id == "GLOBAL-ADULT-ENTERTAINMENT-ECOSYSTEM":
                metadata = {
                    "age_restricted": True,
                    "age_verification_required": True,
                    "consent_and_rights_required": True,
                    "legal_compliance_required": True,
                }

            self._register(
                ecosystem_id,
                name,
                ecosystem_type,
                capabilities=capabilities,
                parent_id=GLOBAL_ECOSYSTEM_ID,
                metadata=metadata,
            )

        # PRESERVE EXISTING PERSONAL IDENTITIES AND BRANDS
        self._register(
            "PERSONAL-RAJESHKHANDELWAL",
            "RAJESHKHANDELWAL",
            "PERSONAL",
            repository_ref=(
                "RAJESHKHANDELWALOFFICIAL/RAJESHKHANDELWAL"
            ),
            capabilities=[
                "IDENTITY", "PROFILE", "WEBSITE", "DOMAIN", "PROJECTS"
            ],
            parent_id="GLOBAL-PEOPLE-ECOSYSTEM",
        )

        self._register(
            "PERSONAL-RAJESHKHANDELWALOFFICIAL",
            "RAJESHKHANDELWALOFFICIAL",
            "PERSONAL",
            repository_ref=(
                "RAJESHKHANDELWALOFFICIAL/MAIN-BASE-FOUNDATION"
            ),
            capabilities=[
                "IDENTITY", "PROFILE", "BUSINESS",
                "WEBSITE", "DOMAIN", "PROJECTS"
            ],
            parent_id="GLOBAL-PEOPLE-ECOSYSTEM",
        )

        self._register(
            "PERSONAL-DRRAJESHKANDELWALIBC",
            "DRRAJESHKANDELWALIBC",
            "PERSONAL_BRAND",
            capabilities=[
                "IDENTITY", "BRAND", "BUSINESS", "WEBSITE", "DOMAIN"
            ],
            parent_id="GLOBAL-PEOPLE-ECOSYSTEM",
        )

        self._register(
            "PERSONAL-DRRAJESHKANDELWALIBCOFFICIAL",
            "DRRAJESHKANDELWALIBCOFFICIAL",
            "PERSONAL_BRAND",
            capabilities=[
                "IDENTITY", "BRAND", "BUSINESS", "WEBSITE", "DOMAIN"
            ],
            parent_id="GLOBAL-PEOPLE-ECOSYSTEM",
        )

        # PRESERVE EXISTING COMPANIES AND COMPANY GROUPS
        company_capabilities = [
            "ORGANIZATION",
            "BUSINESS",
            "TEAM",
            "PROJECTS",
            "WEBSITE",
            "DOMAIN",
        ]

        self._register(
            "COMPANY-KHANDELWALGROUPANDCOMPANY",
            "KHANDELWALGROUPANDCOMPANY",
            "COMPANY",
            capabilities=company_capabilities,
            parent_id="GLOBAL-BUSINESS-ECOSYSTEM",
        )

        self._register(
            "COMPANY-KHANDELWALGROUPANDCOMPANYOFFICIAL",
            "KHANDELWALGROUPANDCOMPANYOFFICIAL",
            "COMPANY",
            capabilities=company_capabilities,
            parent_id="GLOBAL-BUSINESS-ECOSYSTEM",
        )

        self._register(
            "COMPANY-KHANDELWALGROUPANDCOMPANIES",
            "KHANDELWALGROUPANDCOMPANIES",
            "COMPANY_GROUP",
            capabilities=company_capabilities,
            parent_id="GLOBAL-BUSINESS-ECOSYSTEM",
        )

        self._register(
            "COMPANY-KHANDELWALGROUPANDCOMPANIESOFFICIAL",
            "KHANDELWALGROUPANDCOMPANIESOFFICIAL",
            "COMPANY_GROUP",
            capabilities=company_capabilities,
            parent_id="GLOBAL-BUSINESS-ECOSYSTEM",
        )

    def _register(
        self,
        ecosystem_id: str,
        name: str,
        ecosystem_type: str,
        *,
        repository_ref: Optional[str] = None,
        capabilities: Optional[List[str]] = None,
        parent_id: Optional[str] = None,
        metadata: Optional[dict] = None,
        status: str = "REGISTERED",
        enabled: bool = True,
    ) -> None:
        identity = GlobalEcosystemIdentity(
            ecosystem_id=ecosystem_id,
            name=name,
            ecosystem_type=ecosystem_type,
            repository_ref=repository_ref,
            capabilities=list(capabilities or []),
            parent_id=parent_id,
            metadata=dict(metadata or {}),
            status=status,
            enabled=enabled,
        )
        self.register(identity)

    def register(self, ecosystem: GlobalEcosystemIdentity) -> None:
        """Register or replace an identity by its unique ID."""
        key = ecosystem.ecosystem_id.strip().upper()
        self.ecosystems[key] = ecosystem

    def get(self, ecosystem_id: str) -> GlobalEcosystemIdentity:
        """Return one registered identity or raise KeyError."""
        key = ecosystem_id.strip().upper()

        if key not in self.ecosystems:
            raise KeyError(
                f"Unknown GLOBAL ECOSYSTEM identity: {ecosystem_id}"
            )

        return self.ecosystems[key]

    def list(
        self,
        include_root: bool = True,
    ) -> List[GlobalEcosystemIdentity]:
        """List identities, optionally excluding the master root."""
        entries = list(self.ecosystems.values())

        if not include_root:
            entries = [
                entry for entry in entries
                if entry.parent_id is not None
            ]

        return entries

    def names(self) -> List[str]:
        """Return all registered names."""
        return [entry.name for entry in self.ecosystems.values()]

    def statuses(self) -> List[dict]:
        """Return all registered identity records."""
        return [entry.to_dict() for entry in self.ecosystems.values()]

    def exists(self, ecosystem_id: str) -> bool:
        """Check whether an identity is registered."""
        return ecosystem_id.strip().upper() in self.ecosystems

    def children(
        self,
        parent_id: str = GLOBAL_ECOSYSTEM_ID,
    ) -> List[GlobalEcosystemIdentity]:
        """Return direct children of a parent ecosystem."""
        key = parent_id.strip().upper()

        return [
            entry for entry in self.ecosystems.values()
            if entry.parent_id == key
        ]

    def tree(self) -> dict:
        """Return the master ecosystem and its direct children."""
        root = self.get(GLOBAL_ECOSYSTEM_ID).to_dict()
        root["children"] = [
            entry.to_dict() for entry in self.children()
        ]
        return root


# Backward compatibility for existing imports.
EcosystemRegistry = GlobalEcosystemRegistry
