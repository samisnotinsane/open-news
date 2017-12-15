from django.db import models

from django.utils.text import slugify

# Create your models here.

class TopicSection(models.Model):
    topic_name = models.CharField(max_length=200)
    topic_id = models.AutoField(primary_key=True, unique=True)

    def __str__(self):
        return self.topic_name

    def __int__(self):
        return self.topic_id

class Article(models.Model):
    headline = models.CharField(max_length=140)
    body = models.TextField()
    section = models.ForeignKey(TopicSection, null=False, on_delete=models.CASCADE)
    article_id = models.AutoField(primary_key=True, unique=True)
    published = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=140)

    def __str__(self):
        return self.headline

    def save(self, *args, **kwargs):
        self.slug = slugify(self.headline)
        super(Article, self).save(*args, **kwargs)
