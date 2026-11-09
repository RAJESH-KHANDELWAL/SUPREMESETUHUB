import unittest
from personal_lifestyle_wellness.service import PersonalWellnessService
class PersonalWellnessServiceTests(unittest.TestCase):
 def setUp(self): self.service=PersonalWellnessService()
 def test_default_hides_adult_categories(self):
  items=self.service.list_categories()
  self.assertEqual(len(items),21)
  self.assertTrue(all(x["access_class"]=="general" for x in items))
 def test_adult_categories_are_explicitly_opt_in(self):
  items=self.service.list_categories(include_adult=True)
  self.assertEqual(len(items),23)
  self.assertEqual(self.service.get_category("adult_porn_media_18_plus"),None)
  self.assertEqual(self.service.get_category("adult_sexual_wellness_18_plus",include_adult=True)["access_class"],"18_plus_restricted")
 def test_family_and_couple_categories(self):
  ids={x["id"] for x in self.service.list_categories()}
  self.assertTrue({"personal_health_wellness","relatives_extended_family","friends_social_relationships","family_relationships","marriage_partnership","couple_relationships","parenting_parenthood","relationship_counselling","sexual_health_education"}.issubset(ids))
 def test_known_and_unknown_categories(self):
  self.assertIsNotNone(self.service.get_category("personal_care"))
  self.assertIsNone(self.service.get_category("unknown"))
 def test_status(self):
  status=self.service.get_status()
  self.assertEqual(status["category_count"],23)
  self.assertEqual(status["restricted_18_plus_count"],2)
if __name__=="__main__": unittest.main()
