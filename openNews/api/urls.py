from rest_framework import routers
from django.conf.urls import include, url
from api import views

router = routers.DefaultRouter()
router.register(r'sections', views.SectionViewSet)
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
