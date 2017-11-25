from django.contrib.auth.models import User, Group
from rest_framework import serializers
from mainapp.models import Section, Article

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ('text')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        read_only = False,
        view_name = 'post'
    )
    class Meta:
        model = Article
        fields = ('headline', 'like', 'dislike', 'post')
