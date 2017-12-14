from rest_framework import routers
from django.conf.urls import include, url
from api import views

router = routers.DefaultRouter()
router.register(r'sections', views.SectionViewSet)
router.register(r'photos', views.PhotoViewSet)
# router.register(r'comments', views.CommentView)
# router.register(r'user', views.UserAccountView)
# router.register(r'register', views.UserCreateAPIView)
# router.register(r'profile-picture', views.ProfilePictureView)
# router.register(r'login', views.UserLoginAPIView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register/$', views.UserCreateAPIView.as_view(), name='register'),
    url(r'^user/$', views.UserAccountView.as_view(), name='profile'),
    url(r'^profile-picture/$', views.ProfilePictureView.as_view(), name='profile-picture'),
    url(r'^login/$', views.UserLoginAPIView.as_view(), name='login'),
    url(r'^comments/$', views.CommentView.as_view(), name='comments'),
    url(r'^article/(?P<pk>[0-9]+)$', views.ArticleViewSet.as_view(), name='article-detail'),
    url(r'^user/(?P<pk>[0-9]+)$',  views.UserUpdateAPIView.as_view(), name='password_reset'),
    url(r'^account/(?P<pk>[0-9]+)$',  views.UserAccountUpdateView.as_view(), name='profile_update'),
    url(r'^comment/(?P<pk>[0-9]+)$',  views.CommentUpdateView.as_view(), name='comment_update'),
]
