from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Category,
    Recipe
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    search_fields = ('name',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'cooking_time', 'rating')
    list_filter = ('cuisine', 'dish_type', 'category')
    search_fields = ('name', 'main_ingredient')
    autocomplete_fields = ['category']