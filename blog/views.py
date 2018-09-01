from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


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


class EditPostAPI(generics.UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class DestroyPostAPI(generics.DestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly, )

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)


class RetrieveUserPosts(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(owner=self.kwargs.get('pk'))
