from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    link = models.URLField(unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes")
    name = models.CharField(max_length=255)
    link = models.URLField(unique=True)
    img_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    cooking_time = models.CharField(max_length=100, blank=True, null=True)
    cuisine = models.CharField(max_length=100, blank=True, null=True)
    main_ingredient = models.CharField(max_length=100, blank=True, null=True)
    dish_type = models.CharField(max_length=100, blank=True, null=True)
    ingredients = models.JSONField(default=list)  # Список ингредиентов
    calories = models.CharField(max_length=50, blank=True, null=True)
    bzu = models.JSONField(default=dict)  # Белки, жиры, углеводы
    domain = models.CharField(max_length=255, blank=True, null=True)
    rating = models.CharField(max_length=10, blank=True, null=True)
    votes = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    steps = models.JSONField(default=list)  # Шаги приготовления

    def __str__(self):
        return self.name
