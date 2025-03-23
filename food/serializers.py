from rest_framework import serializers
from .models import Category, Recipe

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'link']


class RecipeSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # если нужно отобразить всю категорию
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Recipe
        fields = [
            'id',
            'category',
            'category_id',
            'name',
            'link',
            'img_url',
            'description',
            'cooking_time',
            'cuisine',
            'main_ingredient',
            'dish_type',
            'ingredients',
            'calories',
            'domain',
            'bzu',
            'rating',
            'votes',
            'author',
            'steps',
        ]
