from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticleQuery



router = DefaultRouter()
router.register(r'news', ArticleQuery, basename='posts' )

urlpatterns = [
    path('', include(router.urls)),
]