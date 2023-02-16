from django.urls import path
from comments.views import CommentCreateView

urlpatterns = [
    path("comments/", CommentCreateView.as_view()),
]
