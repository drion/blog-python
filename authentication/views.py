from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.response import Response

from knox.models import AuthToken

from .serializers import (
    CreateUserSerializer,
    UserSerializer,
    LoginUserSerializer
)


class RegistrationAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user).data,
            "token": AuthToken.objects.create(user)
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user).data,
            "token": AuthToken.objects.create(user)
        })


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RetrieveUserAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
