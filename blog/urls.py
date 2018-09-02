from django.urls import path

from .views import ListPostAPI, RetrievePostAPI, EditPostAPI, DestroyPostAPI, ListCommentsAPI

urlpatterns = [
    path('', ListPostAPI.as_view()),
    path('<int:pk>/', RetrievePostAPI.as_view()),
    path('<int:pk>/edit/', EditPostAPI.as_view()),
    path('<int:pk>/delete/', DestroyPostAPI.as_view()),
    path('<int:post>/comments/', ListCommentsAPI.as_view())
]
