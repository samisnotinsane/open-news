from django.test import TestCase
from .models import Section

# Create your tests here.
class SectionTestCase(TestCase):
    def setUp(self):
        Section.objects.create(name="TestSection1")
        Section.objects.create(name="TestSection2")
    
    def test_one(self):
        section1 = Section.objects.get(name="TestSection1")
        section2 = Section.objects.get(name="TestSection2")
        self.assertEqual(section1, section2)
    
    def test_two(self):
        section1 = Section.objects.get(name="TestSection1")
        section2 = Section.objects.get(name="TestSection2")
        self.assertNotEqual(section1, section2)
