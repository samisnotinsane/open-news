from django.http import HttpResponse
from django.shortcuts import render


from .forms import LoginForm, SignForm
from .models import TopicSection, Article

# Create your views here.

def index(request):
    #this should only take the most current news storys. Maybe 5 - 10 listed in reverse chronological order
    topic_list = TopicSection.objects.all()
    article_list = Article.objects.all().order_by('-published')[:5]
    context = {'topics' : topic_list,
    'article_list' : article_list
    }
    return render(request, 'mainapp/article_list.html', context)

def spec_section(request, parameter):
    #this should only take the news storys from the specific topic section (sport, business etc).
    #List all of them in reverse chronological order
    topic_list = TopicSection.objects.all()
    article_list = Article.objects.filter(section__topic_name__icontains=parameter).order_by('-published')[:10]
    context = {'topics':topic_list,'article_list' : article_list}
    return render(request, 'mainapp/article_list.html',context)

def article_detail(request,parameter1,parameter2):
    topic_list = TopicSection.objects.all()
    article = Article.objects.get(slug=parameter2)
    context = {'article' : article,'topics' : topic_list}
    return render(request, 'mainapp/article_detail.html',context)
    return HttpResponse("hello world")

def login(request):
    if request.method == 'POST':
        response = "Thankyou for submitting the form"
        #This should check to see if the form is not valid
    else:
        #if the form is valid then the user should be redirected to the home page
        #form = LoginForm()
        context = {'form' : LoginForm()}
        return render(request, 'login.html', context)
    return HttpResponse(response)

def signup(request):
    if request.method == 'POST':
        reponse = "Thankyou for submitting the form"
    else:
        context = {'form' : SignForm()}
        return render(request, 'signup.html',context)
    return HttpResponse("Display Sign up form")
