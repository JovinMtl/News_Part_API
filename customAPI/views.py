from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from wagtail.users.models import UserProfile as UserWagtail


from news.models import CategorieArticle



from .serializers import ArticleCategorySerializer, \
    UserSerializer, UserWagtailSerializer



# Endpoints managed in the following classes.

class ArticleQuery(viewsets.ViewSet):
    """
        Will do custom GET queries on Article model.
    """
    @action(methods=['get'], detail=False)
    def get_article_category(self, request):
        """
        should return all categories.
        """
        categorie = CategorieArticle.objects.all()
        categorie_serialized = ArticleCategorySerializer(categorie, many=True)

        if categorie_serialized.is_valid:
            return Response(categorie_serialized.data)
        
        return Response({"error": "Could not serialize data"})


# About Users
    @action(methods=['get'], detail=False)
    def get_users(self, request):
        """
        should return all users.
        """
        users = User.objects.all()
        users_serialized = UserSerializer(users, many=True)

        if users_serialized.is_valid:
            return Response(users_serialized.data)
        
        return Response({"error": "Could not serialize data"})
    
    @action(methods=['get'], detail=False)
    def get_avatar(self, request):
        """
        should return all avatars with User ID.
        """
        users = UserWagtail.objects.all()
        users_serialized = UserWagtailSerializer(users, many=True)

        if users_serialized.is_valid:
            return Response(users_serialized.data)
        
        return Response({"error": "Could not serialize data"})

