from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer


class ListPostAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RetrievePostAPI(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
