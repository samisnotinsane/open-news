from django.contrib.auth.models import User, Group
from rest_framework import serializers
from mainapp.models import Section, Article

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ('name',)

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = 'post'
    )
    class Meta:
        model = Article
        fields = ('headline', 'like', 'dislike', 'post',)
