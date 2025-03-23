from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import RegisterSerializer, CustomUserSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from food.models import Recipe
from food.serializers import RecipeSerializer

class SavedRecipesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        recipes = request.user.saved_recipes.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        recipe_id = request.data.get("recipe_id")
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            request.user.saved_recipes.add(recipe)
            return Response({"message": "Рецепт сохранён"})
        except Recipe.DoesNotExist:
            return Response({"error": "Рецепт не найден"}, status=404)

    def delete(self, request):
        recipe_id = request.data.get("recipe_id")
        try:
            recipe = Recipe.objects.get(id=recipe_id)
            request.user.saved_recipes.remove(recipe)
            return Response({"message": "Рецепт удалён из сохранённых"})
        except Recipe.DoesNotExist:
            return Response({"error": "Рецепт не найден"}, status=404)


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


