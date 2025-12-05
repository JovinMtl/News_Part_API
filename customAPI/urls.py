from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NewsOps



router = DefaultRouter()
router.register(r'news', NewsOps, basename='posts' )

urlpatterns = [
    path('', include(router.urls)),
]