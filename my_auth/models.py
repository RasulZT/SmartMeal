from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    saved_recipes = models.ManyToManyField("food.Recipe", related_name="saved_by", blank=True)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    vegetarian = models.BooleanField(default=False)
    allergic_ingredients = models.JSONField(default=list, blank=True)  # список ингредиентов
    favorite_cuisines = models.JSONField(default=list, blank=True)     # список кухонь
    disliked_ingredients = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"Анкета: {self.user.username}"



