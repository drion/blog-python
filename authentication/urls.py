from django.urls import path

from .views import RegistrationAPI, LoginAPI, UserAPI

urlpatterns = [
    path('login/', LoginAPI.as_view()),
    path('register/', RegistrationAPI.as_view()),
    path('user/', UserAPI.as_view()),
]
