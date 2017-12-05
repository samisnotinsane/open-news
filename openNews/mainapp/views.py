from django.shortcuts import render
from django.http import HttpResponse

from api.models import Section, User, Article

def index(request):
    num_articles = Article.objects.all().count()
    num_sections = Section.objects.all().count()
    return render(request, 'mainapp/index.html', context = {
        'num_articles': num_articles,
        'num_sections': num_sections
        },
    )

    # return HttpResponse("<h1>Welcome to OpenNews!</h1><br/><p>You are now viewing our index page.</p>")

def sections(request):
    sections = Section.objects.all()

    context: {
        'sections': sections
    }
    return render(request, "mainapp/sections.html", context)

def login(request):
    print('Not yet implemented')
    return HttpResponse("Not yet implemented")

def register(request):
    print('Not yet implemented')
    return HttpResponse("Not yet implemented")
    
