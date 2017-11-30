from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Section, Article, Account, Comment, ProfilePicture, Photo

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    CharField,
    IntegerField,
    DateField,
    EmailField,
    DateTimeField,
    ImageField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedModelSerializer,
    ValidationError
)
from django.db.models import Q
from django.core.validators import RegexValidator

User = get_user_model()


class ArticleSerializer(HyperlinkedModelSerializer):
    headline = CharField()
    like = IntegerField(read_only=True)
    dislike = IntegerField(read_only=True)
    body = CharField()

    class Meta:
        model = Article
        fields = ('headline', 'like', 'dislike', 'body',)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)


class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')
    first_name = CharField()
    last_name = CharField()

    class Meta:
        model = User
        fields = ('username', 'email', 'email2',
                  'first_name', 'last_name', 'password')
        extra_kwargs = {"password": {"write_only": True}}

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match")
        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This email had already been registered.")

        return value

    def create(self, validate_data):
        username = validate_data['username']
        email = validate_data['email']
        password = validate_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validate_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(label='Email Address', required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'token')
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        user_obj = None
        email = data.get('email', None)
        username = data.get('username', None)
        password = data['password']
        if not email and not username:
            raise ValidationError("A username or email is required to login.")

        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact="")
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This username/email is not valid.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError(
                    "Incorrect credentials please try again.")

        data["token"] = "Some Random Token"
        return data


class AccountSerializer(ModelSerializer):
    user = UserCreateSerializer
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # validators should be a list
    phone_number = CharField(
        validators=[phone_regex], max_length=15, allow_null=True)
    birth_date = DateField(allow_null=True)
    location = CharField(allow_null=True)

    class Meta:
        model = Account
        fields = ('user', 'phone_number', 'birth_date', 'location')


class ProfilePictureSerializer(ModelSerializer):
    pic = ImageField()
    profile = AccountSerializer

    class Meta:
        model = ProfilePicture
        fields = ('profile', 'pic')


class CommentSerializer(ModelSerializer):
    user = UserCreateSerializer
    article = ArticleSerializer
    content = CharField(max_length=500)
    like = IntegerField(read_only=True)
    dislike = IntegerField(read_only=True)

    class Meta:
        model = Comment
        fields = ('user', 'article', 'content', 'like', 'dislike')


# ----
class SectionSerializer(HyperlinkedModelSerializer):
    name = serializers.CharField(allow_blank=False)

    class Meta:
        model = Section
        fields = ('name',)
        read_only_fields = ('name',)


class PhotoSerializer(HyperlinkedModelSerializer):
    photo = ImageField(allow_null=True)
    article_id = ArticleSerializer

    class Meta:
        model = Photo
        fields = ('photo', 'article_id')
