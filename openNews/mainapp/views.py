from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to OpenNews!</h1><br/><p>You are now viewing our index page.</p>")
