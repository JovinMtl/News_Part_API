from rest_framework import serializers


from news.models import NewsPage


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPage
        fields = '__all__'