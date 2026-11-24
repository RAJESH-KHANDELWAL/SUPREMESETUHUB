"""LINKSETU company experience service."""


class LinkSetuCompanyService:
    """Manage company presence in LINKSETU."""

    platform_name = "LINKSETU"

    def create_company(
        self,
        owner_id: str,
        name: str,
        description: str = "",
        industry: str = "",
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "name": name,
            "description": description,
            "industry": industry,
            "entity_type": "company",
            "status": "created",
        }

    def get_company(
        self,
        company_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "company_id": company_id,
            "entity_type": "company",
        }

    def update_company(
        self,
        company_id: str,
        data: dict,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "company_id": company_id,
            "entity_type": "company",
            "data": data,
            "status": "updated",
        }

    def get_companies(
        self,
        owner_id: str,
    ) -> dict:

        return {
            "platform": self.platform_name,
            "owner_id": owner_id,
            "companies": [],
        }
