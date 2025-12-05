from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


from news.models import NewsPage
# Create your views here.


from .serializers import NewsSerializer



class NewsOps(viewsets.ViewSet):
    """
        Will do custom GET queries on News model.
    """
    @action(methods=['get'], detail=False)
    def get_pages(self, request):
        """
        should return all pages.
        """
        pages = NewsPage.objects.all()
        pages_serialized = NewsSerializer(pages, many=True)

        if pages_serialized.is_valid:
            return Response(pages_serialized.data)
        
        return Response({"error": "Could not serialize data"})