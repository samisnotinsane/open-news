from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from api.models import Section, User, Article

def index(request):
    num_articles = Article.objects.all().count()
    num_sections = Section.objects.all().count()
    return render(request, 'mainapp/index.html', context = {
        'num_articles': num_articles,
        'num_sections': num_sections
        },
    )

# def sections(request):
#     topics = Section.objects.all()
#     return render(request, "mainapp/section_list.html", context= {
#             'sections': topics
#         }
#     )

def login(request):
    print('Not yet implemented')
    return HttpResponse("Not yet implemented")

def register(request):
    print('Not yet implemented')
    return HttpResponse("Not yet implemented")
    
class ArticleListView(generic.ListView):
    model = Article
    template_name = 'mainapp/article_list.html'

class SectionListView(generic.ListView):
    model = Section
    template_name = 'mainapp/section_list.html'