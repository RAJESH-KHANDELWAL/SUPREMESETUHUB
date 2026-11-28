"""Typed errors for SERVER domain operations."""
class ServerError(Exception): pass
class ServerValidationError(ServerError): pass
class ServerNotFoundError(ServerError): pass
class ServerProviderError(ServerError): pass
class ServerConflictError(ServerError): pass
