from django.urls import path
from .views import *

urlpatterns = [
    # Category
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),

    # Recipe
    path('recipes/', RecipeListAPIView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroyAPIView.as_view(), name='recipe-detail'),
    path('recipes/popular/', PopularRecipesAPIView.as_view(), name='recipes-popular'),
    path('recipes/random/', RandomRecipesAPIView.as_view(), name='recipes-random'),
    path('recipes/related/', RelatedRecipesAPIView.as_view(), name='recipes-related'),
    path('recipes/by-ingredients/', RecipesByIngredientsAPIView.as_view(), name='recipes-by-ingredients'),
    path('recipes/by-category-name/', RecipesByCategoryNameAPIView.as_view(), name='recipes-by-category-name'),

]
