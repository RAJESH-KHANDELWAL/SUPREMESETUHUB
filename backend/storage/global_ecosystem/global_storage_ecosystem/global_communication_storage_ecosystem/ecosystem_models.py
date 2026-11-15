"""Root category descriptor."""
from dataclasses import dataclass
@dataclass(frozen=True)
class CategoryDescriptor:
    package_name: str
    namespace: str = "communication"
