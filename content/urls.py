from django.urls import path
from .views import *

urlpatterns = [
    # Blog
    path("blogs/", BlogListCreateAPIView.as_view(), name="blog-list-create"),
    path("blogs/<int:pk>/", BlogRetrieveUpdateDestroyAPIView.as_view(), name="blog-detail"),

    # Article
    path("articles/", ArticleListCreateAPIView.as_view(), name="article-list-create"),
    path("articles/<int:pk>/", ArticleRetrieveUpdateDestroyAPIView.as_view(), name="article-detail"),

    path("comments/", CommentListCreateAPIView.as_view(), name="recipe-comments"),
]
