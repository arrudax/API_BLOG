from django.urls import path
from posts.views import PostCreateView

urlpatterns = [
    path("posts/", PostCreateView.as_view()),
]
