import unittest
from .service import DeepSeekCoreService
class ProviderTests(unittest.TestCase):
 def setUp(self): self.s=DeepSeekCoreService()
 def test_unknown(self):
  with self.assertRaises(ValueError): self.s.validate("unknown",{})
 def test_chat(self): self.assertFalse(self.s.validate("chat_completions",{"messages":[{"role":"user","content":"hi"}]})["live_call"])
 def test_responses(self): self.assertEqual(self.s.validate("responses",{"input":"hi"})["capability"],"responses")
 def test_search(self): self.assertEqual(self.s.validate("search",{"query":"hi"})["capability"],"search")
 def test_fetch(self): self.assertEqual(self.s.validate("fetch",{"urls":["https://example.com"]})["capability"],"fetch")
if __name__=="__main__": unittest.main()
