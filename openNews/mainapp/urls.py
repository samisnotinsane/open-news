from django.conf.urls import url
from mainapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sections/$', views.SectionListView.as_view(), name='sections'),
    # url(r'^sections/<name>$', views.sections, name='section_by_name'),
    url(r'^articles/$', views.ArticleListView.as_view(), name='articles'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),

]
