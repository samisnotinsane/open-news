from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to OpenNews! You are now viewing our index page.")
