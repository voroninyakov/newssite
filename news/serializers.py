from rest_framework import serializers
from .models import News, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('text',)
        
class NewsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)
    class Meta:
        model = News
        fields = ("title", "text", "views", "tags")