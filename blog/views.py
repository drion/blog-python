from rest_framework import generics, permissions

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
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


class ListUserPosts(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(owner=self.kwargs.get('pk'))


class ListCommentsAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs.get('post'))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, post=Post.objects.get(pk=self.request.data.get('post')))
