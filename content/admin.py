from django.contrib import admin
from .models import Blog, Article, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "author__username")

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "published_at")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("published_at",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'text', 'created_at', 'recipe', 'blog', 'parent')
    search_fields = ('text', 'user__username')
    list_filter = ('created_at',)
