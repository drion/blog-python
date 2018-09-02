from django.db import models
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType


class Post(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User,
        related_name="posts",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=512)
    owner = models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
