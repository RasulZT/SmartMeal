from rest_framework import serializers
from .models import Blog, Article, Comment
from my_auth.serializers import CustomUserSerializer


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Blog
        fields = "__all__"
        read_only_fields = ("id", "author", "created_at")


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ("id", "slug", "published_at", "updated_at")

class CommentSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'user', 'recipe', 'blog', 'text', 'created_at', 'parent', 'replies']

    def get_replies(self, obj):
        return CommentSerializer(obj.replies.all(), many=True).data
