from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from mainapp.models import Section, Article

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(allow_blank=False)
    class Meta:
        model = Section
        fields = ('name',)
        read_only_fields = ('name',)

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        read_only = True,
        view_name = 'post'
    )
    class Meta:
        model = Article
        fields = ('headline', 'like', 'dislike', 'post',)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)