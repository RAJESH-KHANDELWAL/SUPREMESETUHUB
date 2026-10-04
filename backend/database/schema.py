class DatabaseSchema:
    """
    CENTRAL DATABASE SCHEMA REGISTRY

    Future data domains:
    SERVER
    SYSTEM SOFTWARE
    WEB
    WEBSITE
    APP
    DOMAIN
    HOSTING
    WORDPRESS
    BUSINESS
    USERS
    CUSTOMERS
    """

    DOMAINS = (
        "server",
        "system_software",
        "web",
        "website",
        "app",
        "domain",
        "hosting",
        "wordpress",
        "business",
        "users",
        "customers",
    )

    @classmethod
    def list_domains(cls):
        return list(cls.DOMAINS)

    @classmethod
    def has_domain(cls, name):
        return name in cls.DOMAINS
