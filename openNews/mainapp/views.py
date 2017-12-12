from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from api.models import Section, User, Article

appname = 'Open News'
apptagline = 'An open source news platform.'

def index(request):
    num_articles = Article.objects.all().count()
    latest_article = Article.objects.order_by('id')[0]
    num_sections = Section.objects.all().count()
    return render(request, 'mainapp/index.html', context = {
        'appname': appname,
        'apptagline': apptagline,
        'num_articles': num_articles,
        'latest_article': latest_article,
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

class ArticleDetailView(generic.DetailView):
    model = Article
    template_name = 'mainapp/article_detail.html'

class SectionListView(generic.ListView):
    model = Section
    template_name = 'mainapp/section_list.html'