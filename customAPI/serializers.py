from django.contrib.auth.models import User
from rest_framework import serializers
from wagtail.users.models import UserProfile as UserWagtail

from news.models import NewsPage, Articles, CategorieArticle


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPage
        fields = '__all__'

class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorieArticle
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # fields=['id','username']
class UserWagtailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWagtail
        # fields = '__all__'
        # depth = 1
        fields=['id','avatar']


class ArticlesSerializerBanContent(serializers.ModelSerializer):
    class Meta:
        model = Articles
        # fields = '__all__'
        depth = 1
        # exclude = ['contenu']
        fields = ['latest_revision']