from django.db import models
from django.contrib.auth.models import User


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
