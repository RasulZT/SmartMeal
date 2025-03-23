
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")


from django.core.management.base import BaseCommand
import os, json
from food.models import Category, Recipe
from tqdm import tqdm  # Установи: pip install tqdm


class Command(BaseCommand):
    help = "Импортирует рецепты из data.json в базу данных"

    def handle(self, *args, **kwargs):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"❌ Ошибка загрузки файла: {e}"))
            return

        total_recipes = 0

        for category_data in tqdm(data, desc="📦 Импорт категорий"):
            category_name = category_data.get("category")
            category_link = category_data.get("category_link")
            category_obj, _ = Category.objects.get_or_create(name=category_name, defaults={"link": category_link})

            recipes = category_data.get("recipes", [])
            for recipe_data in tqdm(recipes, desc=f"🍲 {category_name}", leave=False):
                recipe, created = Recipe.objects.update_or_create(
                    link=recipe_data["link"],
                    defaults={
                        "category": category_obj,
                        "name": recipe_data["name"],
                        "img_url": recipe_data.get("img_url"),
                        "description": recipe_data.get("descr"),
                        "cooking_time": recipe_data.get("cooking_time"),
                        "cuisine": recipe_data.get("cuisine"),
                        "main_ingredient": recipe_data.get("main_ingredient"),
                        "dish_type": recipe_data.get("dish_type"),
                        "ingredients": recipe_data.get("ingridients"),
                        "calories": recipe_data.get("calories"),
                        "bzu": recipe_data.get("bzu", {}),
                        "rating": recipe_data.get("rating"),
                        "votes": recipe_data.get("votes"),
                        "author": recipe_data.get("author"),
                        "steps": recipe_data.get("steps", []),
                    },
                )
                total_recipes += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Импорт завершён. Всего обработано рецептов: {total_recipes}"))
