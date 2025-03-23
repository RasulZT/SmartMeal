from django.db import models
from django.utils.text import slugify

from my_auth.models import CustomUser

from smartmeal import settings


# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_recipes")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    img_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    ingredients = models.JSONField(default=list)
    steps = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments")
    recipe = models.ForeignKey("food.Recipe", on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    blog = models.ForeignKey("Blog", on_delete=models.CASCADE, related_name="comments", null=True, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:30]}"
