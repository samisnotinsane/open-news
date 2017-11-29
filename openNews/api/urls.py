from rest_framework import routers
from django.conf.urls import include, url
from api import views

router = routers.DefaultRouter()
router.register(r'sections', views.SectionViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'register', views.UserCreateAPIView)
router.register(r'profile', views.UserAccountView)
router.register(r'profile-picture', views.ProfilePictureView)
router.register(r'login', views.UserLoginAPIView)
router.register(r'comments', views.CommentView)

urlpatterns = [
    url(r'^', include(router.urls)),
]
