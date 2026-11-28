"""Cryptographic configuration policy validation; not crypto primitives."""
from dataclasses import dataclass
@dataclass(frozen=True)
class CryptoProfile:
    purpose: str
    algorithm: str
    key_management: str
    tls_required: bool = True
def validate_crypto_profile(profile: CryptoProfile):
    issues=[]
    if not profile.purpose.strip(): issues.append("purpose_required")
    if profile.algorithm.lower() in {"md5", "sha1", "des", "3des", "rc4"}: issues.append("weak_or_deprecated_algorithm")
    if not profile.algorithm.strip(): issues.append("algorithm_required")
    if profile.key_management not in {"managed_kms", "hsm", "vault", "platform_keystore"}: issues.append("approved_key_management_required")
    if not profile.tls_required: issues.append("transport_encryption_required")
    return tuple(issues)
