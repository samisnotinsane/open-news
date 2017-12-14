from .models import Section, Article, Photo
from rest_framework import viewsets, generics
from api.serializers import SectionSerializer, ArticleSerializer, PhotoSerializer

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .serializers import (UserCreateSerializer, UserLoginSerializer, 
    AccountSerializer, CommentSerializer, ProfilePictureSerializer,
    AccountUpdateSerializer, UserUpdateSerializer, CommentUpdateSerializer
)

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import Account, Comment, ProfilePicture

User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class UserAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]

class ProfilePictureView(generics.CreateAPIView):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer
    permission_classes = [AllowAny]

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    print("Phase 1")

    def post (self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data = data)
        if serializer.is_valid(raise_exception = True):
            new_data = serializer.data
            return Response(new_data, status = HTTP_200_OK)
        return Response(serializer.errors,status = HTTP_400_BAD_REQUEST)

class CommentView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

# ---

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class ArticleViewSet(generics.RetrieveUpdateAPIView):
    queryset = Article.objects.all().order_by('-like')
    serializer_class = ArticleSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class UserUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserUpdateSerializer
	
class UserAccountUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountUpdateSerializer
    permission_classes = [AllowAny]
	
class CommentUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [AllowAny]