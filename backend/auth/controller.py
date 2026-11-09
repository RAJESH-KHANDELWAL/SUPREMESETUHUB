"""Authentication controller layer."""

from backend.auth.service import AuthenticationService


class AuthenticationController:
    """Coordinate API requests with AuthenticationService."""

    def __init__(self):
        self.service = AuthenticationService()

    def initialize(self):
        return self.service.initialize()

    def authenticate(self, master_id):
        return self.service.authenticate(master_id)

    def signin(self, master_id=None, username=None, password=None):
        return self.service.signin(
            master_id=master_id,
            username=username,
            password=password,
        )

    # Backward-compatible alias for existing internal callers.
    def login(self, master_id=None, username=None, password=None):
        return self.signin(
            master_id=master_id,
            username=username,
            password=password,
        )

    def validate_token(self, token):
        return self.service.validate_token(token)

    def signout(self, token=None, session_id=None):
        return self.service.signout(
            token=token,
            session_id=session_id,
        )

    # Backward-compatible alias for existing internal callers.
    def logout(self, token=None, session_id=None):
        return self.signout(token=token, session_id=session_id)


__all__ = ["AuthenticationController"]
