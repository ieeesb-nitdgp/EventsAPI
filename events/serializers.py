from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'updated_on', 'content', 'image', 'image_1', 'image_2', 'image_3', 'created_on', 'status', 'event_date')