from django.contrib import admin
from api.models import Section, Article
# Register your models here.
admin.site.register(Section)
class ArticleAdmin(admin.ModelAdmin):
    # Prevent showing like and dislike fields.
    fields = ['headline', 'body', 'section'] 
    list_display = ('headline', 'like', 'dislike', 'section')
    list_filter = ('section',)

# Register the admin class with the associated model
admin.site.register(Article, ArticleAdmin)

# admin.site.register(Article)
