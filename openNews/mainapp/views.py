from django.shortcuts import render
from django.http import HttpResponse

from api.models import Section

def index(request):
    return HttpResponse("<h1>Welcome to OpenNews!</h1><br/><p>You are now viewing our index page.</p>")

def sections(request):
    sections = Section.objects.all()
    context: {
        'sections': sections
    }
    return render(request, "mainapp/sections.html", context)