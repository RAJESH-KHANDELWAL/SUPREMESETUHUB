from backend.logger.service import LoggerService
from backend.config.service import ConfigService
from backend.database.service import DatabaseService
from backend.identity.service import IdentityService
from backend.auth.service import AuthenticationService
from backend.status.service import StatusService
from backend.storage.service import StorageService
from backend.security.service import SecurityService
from backend.api.service import APIService
from backend.users.service import UserService
from backend.organizations.service import OrganizationService
from backend.roles.service import RoleService


class MainBaseFoundation:

    def __init__(self):
        self.logger = LoggerService()

        self.config = ConfigService()
        self.database = DatabaseService()
        self.identity = IdentityService()
        self.authentication = AuthenticationService()
        self.status = StatusService()
        self.storage = StorageService()
        self.security = SecurityService()
        self.api = APIService()

        self.users = UserService()
        self.organizations = OrganizationService()
        self.roles = RoleService()

    def start(self):

        self.logger.info(
            "CORE",
            "MAIN BASE FOUNDATION boot started."
        )

        config = self.config.initialize()
        database = self.database.initialize()
        identity = self.identity.initialize()
        authentication = self.authentication.initialize()

        status = self.status.initialize()

        storage = self.storage.initialize()
        security = self.security.initialize()
        api = self.api.initialize()

        users = self.users.initialize()
        organizations = self.organizations.initialize()
        roles = self.roles.initialize()

        self.logger.info(
            "CORE",
            "MAIN BASE FOUNDATION boot completed successfully."
        )

        return {

            "config": config,

            "database": database,

            # IdentityService.initialize() creates/migrates storage; it does
            # not create a default person identity. Report readiness without
            # assuming that an identity record already exists.
            "identity": {
                "master_id": getattr(identity, "master_id", None),
                "full_name": getattr(identity, "full_name", None),
                "username": getattr(
                    identity,
                    "primary_username",
                    getattr(identity, "username", None),
                ),
                "status": getattr(identity, "status", "INITIALIZED"),
                "record_available": identity is not None,
            },

            "authentication": authentication,

            "status": status,

            "storage": storage,

            "security": security,

            "api": api,

            "users": users,

            "organizations": organizations,

            "roles": roles,
        }
