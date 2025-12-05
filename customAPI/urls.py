from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NewsOps



router = DefaultRouter()
router.register(r'posts', NewsOps, basename='entrants' )

urlpatterns = [
    path('', include(router.urls)),
]