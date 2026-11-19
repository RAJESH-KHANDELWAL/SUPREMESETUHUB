"""Backend Global Ecosystem manager; legacy core layer remains in place."""
from pathlib import Path
class GlobalEcosystemManager:
 NAME="BACKEND GLOBAL ECOSYSTEM"; VERSION="1.0.0"
 def __init__(self): self.root=Path(__file__).resolve().parent; self.status="READY"
 def initialize(self): self.status="RUNNING"; return self.health()
 def health(self):
  legacy=self.root.parent/"core"/"global_ecosystem"
  c={"package_init":(self.root/"__init__.py").exists(),"manager":(self.root/"manager.py").exists(),"php_bridge":(self.root/"manager.php").exists(),"global_foundation_ecosystem":(self.root/"global_foundation_ecosystem").is_dir(),"legacy_core_global_ecosystem_preserved":legacy.is_dir()}
  return {"name":self.NAME,"version":self.VERSION,"status":self.status,"checks":c,"healthy":all(c.values())}
 def get_global_foundation_manager(self):
  from .global_foundation_ecosystem.manager import GlobalFoundationEcosystemManager
  return GlobalFoundationEcosystemManager()
def get_manager(): return GlobalEcosystemManager()
