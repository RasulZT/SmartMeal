from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
import random
from django.db.models import Q

# ---------- CATEGORY CRUD ----------
class CategoryListCreateAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------- RECIPE CRUD ----------
class RecipeListCreateAPIView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class RecipeListAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all().order_by("id")
    serializer_class = RecipeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'cuisine', 'main_ingredient', 'dish_type']  # фильтры
    search_fields = ['name', 'description', 'ingredients']  # поиск
    ordering_fields = ['rating', 'votes']  # сортировка

class PopularRecipesAPIView(generics.ListAPIView):
    queryset = Recipe.objects.order_by('-rating', '-votes')[:20]
    serializer_class = RecipeSerializer



class RandomRecipesAPIView(APIView):
    def get(self, request):
        all_ids = list(Recipe.objects.values_list('id', flat=True))
        selected_ids = random.sample(all_ids, min(20, len(all_ids)))
        recipes = Recipe.objects.filter(id__in=selected_ids)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

class RelatedRecipesAPIView(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        cuisine = self.request.query_params.get('cuisine')
        dish_type = self.request.query_params.get('dish_type')
        return Recipe.objects.filter(cuisine=cuisine, dish_type=dish_type)[:20]



class RecipesByIngredientsAPIView(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        items = self.request.query_params.get('items', '')
        ingredients = [item.strip().lower() for item in items.split(',') if item]
        query = Q()
        for ingr in ingredients:
            query &= Q(ingredients__icontains=ingr)
        return Recipe.objects.filter(query)

class RecipesByCategoryNameAPIView(ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        name = self.request.query_params.get("name", "").strip().lower()
        category = Category.objects.filter(name__icontains=name).first()
        if category:
            return Recipe.objects.filter(category=category).order_by("id")
        return Recipe.objects.none()