from django.test import TestCase
from .models import Section, Article

# Create your tests here.
class SectionTestCase(TestCase):
    def setUp(self):
        Section.objects.create(name="TestSection1")
        Section.objects.create(name="TestSection2")
    
    def test_one(self):
        section1 = Section.objects.get(name="TestSection1")
        section2 = Section.objects.get(name="TestSection2")
        self.assertNotEqual(section1, section2)

class ArticleTestCase(TestCase):
    def setUp(self):
        Article.objects.create(
            headline="Test Headline 1",
            body="Body of Test Headline 1"
            )
        Article.objects.create(
            headline="Test Headline 2",
            body="Body of Test Headline 2"
            )
    
    def test_headline_body_not_equals(self):
        article = Article.objects.get(headline="Test Headline 1")
        headline = article.headline
        body = article.body
        self.assertNotEqual(headline, body)
    
    def test_headlines_not_equals(self):
        article1 = Article.objects.get(headline="Test Headline 1")
        article2 = Article.objects.get(headline="Test Headline 2")
        headline1 = article1.headline
        headline2 = article2.headline
        self.assertNotEqual(headline1, headline2)

    def test_bodies_not_equals(self):
        article1 = Article.objects.get(headline="Test Headline 1")
        article2 = Article.objects.get(headline="Test Headline 2")
        body1 = article1.body
        body2 = article2.body
        self.assertNotEqual(body1, body2)

