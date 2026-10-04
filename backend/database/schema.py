class DatabaseSchema:
    """
    CENTRAL DATABASE SCHEMA

    Central data backbone for:

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

    # ==========================================================
    # LOGICAL DATA DOMAINS
    # ==========================================================

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

    # ==========================================================
    # ACTUAL DATABASE TABLES
    # ==========================================================

    TABLES = {

        # ======================================================
        # USERS
        # ======================================================

        "users": """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id TEXT UNIQUE,

            full_name TEXT NOT NULL DEFAULT '',

            username TEXT UNIQUE NOT NULL,

            email TEXT UNIQUE NOT NULL,

            phone TEXT NOT NULL DEFAULT '',

            password TEXT,

            password_hash TEXT,

            role TEXT NOT NULL DEFAULT 'USER',

            status TEXT NOT NULL DEFAULT 'ACTIVE',

            phone_no TEXT NOT NULL DEFAULT '',

            mobile_no TEXT NOT NULL DEFAULT '',

            whatsapp_no TEXT NOT NULL DEFAULT '',

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """,

        # ======================================================
        # SERVERS
        # ======================================================

        "servers": """
        CREATE TABLE IF NOT EXISTS servers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            hostname TEXT,

            ip_address TEXT,

            provider TEXT,

            status TEXT DEFAULT 'active',

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """,

        # ======================================================
        # SYSTEM SOFTWARE
        # ======================================================

        "system_software": """
        CREATE TABLE IF NOT EXISTS system_software (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            server_id INTEGER,

            name TEXT NOT NULL,

            version TEXT,

            vendor TEXT,

            status TEXT DEFAULT 'active',

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (server_id)
                REFERENCES servers(id)
                ON DELETE SET NULL
        )
        """,

        # ======================================================
        # WEB
        # ======================================================

        "web": """
        CREATE TABLE IF NOT EXISTS web (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            version TEXT,

            server_id INTEGER,

            status TEXT DEFAULT 'active',

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (server_id)
                REFERENCES servers(id)
                ON DELETE SET NULL
        )
        """,

        # ======================================================
        # SITES / WEBSITES
        # ======================================================

        "sites": """
        CREATE TABLE IF NOT EXISTS sites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            domain TEXT UNIQUE NOT NULL,

            hosting_provider TEXT,

            platform TEXT,

            scope TEXT DEFAULT 'SITE',

            status TEXT DEFAULT 'active',

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """,

        # ======================================================
        # APPS
        # ======================================================

        "apps": """
        CREATE TABLE IF NOT EXISTS apps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            version TEXT,

            platform TEXT,

            status TEXT DEFAULT 'active',

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """,

        # ======================================================
        # DOMAINS
        # ======================================================

        "domains": """
        CREATE TABLE IF NOT EXISTS domains (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            site_id INTEGER NOT NULL,

            domain_name TEXT UNIQUE NOT NULL,

            registrar TEXT,

            expiry_date TEXT,

            ssl_status TEXT,

            dns_status TEXT,

            status TEXT DEFAULT 'active',

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (site_id)
                REFERENCES sites(id)
                ON DELETE CASCADE
        )
        """,

        # ======================================================
        # HOSTING ACCOUNTS
        # ======================================================

        "hosting_accounts": """
        CREATE TABLE IF NOT EXISTS hosting_accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            site_id INTEGER NOT NULL,

            provider TEXT NOT NULL,

            account_name TEXT,

            server_name TEXT,

            plan_name TEXT,

            status TEXT DEFAULT 'active',

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (site_id)
                REFERENCES sites(id)
                ON DELETE CASCADE
        )
        """,

        # ======================================================
        # WORDPRESS SITES
        # ======================================================

        "wordpress_sites": """
        CREATE TABLE IF NOT EXISTS wordpress_sites (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            site_id INTEGER NOT NULL,

            wordpress_version TEXT,

            admin_url TEXT,

            database_name TEXT,

            php_version TEXT,

            theme_name TEXT,

            status TEXT DEFAULT 'active',

            last_sync TEXT,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (site_id)
                REFERENCES sites(id)
                ON DELETE CASCADE
        )
        """,

        # ======================================================
        # BUSINESS
        # ======================================================

        "business": """
        CREATE TABLE IF NOT EXISTS business (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            business_type TEXT,

            status TEXT DEFAULT 'active',

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """,

        # ======================================================
        # CUSTOMERS
        # ======================================================

        "customers": """
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id INTEGER,

            name TEXT NOT NULL,

            email TEXT,

            phone TEXT,

            status TEXT DEFAULT 'active',

            created_at TEXT DEFAULT CURRENT_TIMESTAMP,

            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (user_id)
                REFERENCES users(id)
                ON DELETE SET NULL
        )
        """,

        # ======================================================
        # AUDIT LOGS
        # ======================================================

        "audit_logs": """
        CREATE TABLE IF NOT EXISTS audit_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            actor TEXT,

            action TEXT NOT NULL,

            target TEXT,

            details TEXT,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """,
    }

    # ==========================================================
    # DOMAIN METHODS
    # ==========================================================

    @classmethod
    def list_domains(cls):
        return list(cls.DOMAINS)

    @classmethod
    def has_domain(cls, name):
        return name in cls.DOMAINS

    # ==========================================================
    # TABLE METHODS
    # ==========================================================

    @classmethod
    def list_tables(cls):
        return list(cls.TABLES.keys())

    @classmethod
    def has_table(cls, name):
        return name in cls.TABLES

    @classmethod
    def get_table_schema(cls, name):
        return cls.TABLES.get(name)


__all__ = [
    "DatabaseSchema",
]
