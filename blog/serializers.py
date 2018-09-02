from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'text', 'title', 'owner', 'created_at')
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'read_only': True},
            'created_at': {'read_only': True}
        }


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'owner', 'post', 'created_at')
        extra_kwargs = {
            'id': {'read_only': True},
            'owner': {'read_only': True},
            'created_at': {'read_only': True}
        }
