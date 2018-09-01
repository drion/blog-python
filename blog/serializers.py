from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'title', 'owner', 'created_at')
        extra_kwargs = {'owner': {'read_only': True}}
