"""Tests for the frontend Infrastructure scaffold and backend contract."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import shutil, subprocess, unittest
ROOT=Path(__file__).resolve().parents[2]
FRONT=ROOT/"frontend"/"infrastructure"
BACK=ROOT/"backend"/"infrastructure"
GE=FRONT/"global_ecosystem"
GIE=GE/"global_infrastructure_ecosystem"
def load(path,name):
 spec=spec_from_file_location(name,path)
 if not spec or not spec.loader: raise ImportError(path)
 m=module_from_spec(spec); spec.loader.exec_module(m); return m
class FrontendInfrastructureScaffoldTests(unittest.TestCase):
 def test_frontend_root_manager_health(self):
  self.assertTrue(load(FRONT/"manager.py","frontinfra").get_manager().health()["healthy"])
 def test_global_ecosystem_manager_health(self):
  self.assertTrue(load(GE/"manager.py","frontinfra_global").get_manager().health()["healthy"])
 def test_global_infrastructure_ecosystem_manager_health(self):
  self.assertTrue(load(GIE/"manager.py","frontinfra_global_infrastructure").get_manager().health()["healthy"])
 def test_connector_contract(self):
  report=load(FRONT/"frontend_infrastructure_backend_infrastructure_connect.py","frontinfra_connector").connect_infrastructure()
  self.assertTrue(report["connected"],report)
 def test_frontend_structure_files(self):
  required=["__init__.py","manager.py","manager.php","frontend_infrastructure_backend_infrastructure_connect.py","frontend_infrastructure_backend_infrastructure_connect.php","global_ecosystem"]
  self.assertTrue(all((FRONT/name).exists() for name in required))
  self.assertTrue((GE/"global_infrastructure_ecosystem").is_dir())
 def test_backend_infrastructure_preserved(self):
  self.assertTrue((BACK/"__init__.py").exists())
  self.assertTrue((BACK/"global_ecosystem"/"global_infrastructure_ecosystem").is_dir())
 @unittest.skipUnless(shutil.which("php"),"PHP CLI missing")
 def test_php_syntax(self):
  for p in [FRONT/"manager.php",FRONT/"frontend_infrastructure_backend_infrastructure_connect.php",GE/"manager.php",GIE/"manager.php",GIE/"frontend_global_infrastructure_ecosystem_backend_global_infrastructure_ecosystem_connect.php"]:
   r=subprocess.run(["php","-l",str(p)],capture_output=True,text=True)
   self.assertEqual(r.returncode,0,r.stdout+r.stderr)
if __name__=="__main__": unittest.main()
