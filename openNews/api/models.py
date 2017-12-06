from django.db import models

from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse

class Section(models.Model):
    # Section name should be concise.
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    # Article headline should be succinct.
    headline = models.CharField(max_length=140)
    body = models.TextField()
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    section = models.ForeignKey(Section, null=False, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of Article.
        """
        return reverse('article-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.headline


class Photo(models.Model):
    photo = models.ImageField()
    article_id = models.ForeignKey(Article)


class Comments(models.Model):
    text = models.TextField()
    like = models.IntegerField()
    dislike = models.IntegerField()
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True)
    birth_date = models.DateField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=60, null=True)

    def __str__(self):
        return self.user.username

    # def Create_Account(Sender, **kwargs):
    #     if kwargs['created']:
    #         user_account = Account.objects.create(user = kwargs['instance'])

    # post_save.connect(Create_Account, sender = User)


class Comment(models.Model):
    content = models.CharField(max_length=50, null=False, blank=False)
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


class ProfilePicture(models.Model):
    profile = models.OneToOneField(Account, on_delete=models.CASCADE)
    pic = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.profile.phone_number
