from django.urls import path

from .views import ListPostAPI, RetrievePostAPI

urlpatterns = [
    path('', ListPostAPI.as_view()),
    path('<int:pk>/', RetrievePostAPI.as_view()),
]
