from django.db import models

class Photo(models.Model):
    photo = models.ImageField()

class Post(models.Model):
    text = models.TextField()
    """
    Deleting a Post shouldn't cause related Photo to also
    get deleted.
    """
    photo = models.ManyToManyField(
        Photo,
        symmetrical=False
    )

    def __str__(self):
        return self.text

class Section(models.Model):
    # Section name should be concise.
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Article(models.Model):
    # Article headline should be succinct.
    headline = models.CharField(max_length=140) 
    like = models.IntegerField()
    dislike = models.IntegerField()
    # Related Post should be deleted upon deleting an Article.
    # Related Post should not be empty for a given Article.
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        null=False
    )

    def __str__(self):
        return self.headline

class Comments(models.Model):
    text = models.TextField()
    like = models.IntegerField()
    dislike = models.IntegerField()
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE
    )
