from mainapp.models import Section, Article
from rest_framework import viewsets
from api.serializers import SectionSerializer, ArticleSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().order_by('-like')
    serializer_class = ArticleSerializer

