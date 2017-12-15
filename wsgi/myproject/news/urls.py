from django.conf.urls import url



from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^spec_section/(?P<parameter>[\w-]+)/$', views.spec_section, name='spec_section'),
    url(r'^spec_section/(?P<parameter1>[\w-]+)/(?P<parameter2>[\w-]+)/$', views.article_detail, name='article_detail'),
]
