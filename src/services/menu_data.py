# Req 3
import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.dishies_recipes(source_path)

    def dishies_recipes(self, source_path: str) -> None:
        with open(source_path) as dishies_file:
            read = csv.DictReader(dishies_file)
            dishes = {}
            for row in read:
                name = row['dish']
                price = float(row['price'])
                ingredient_name = row['ingredient']
                amount = int(row['recipe_amount'])

                dish = dishes.get(name)
                if dish is None:
                    dish = Dish(name, price)
                    dishes[name] = dish
                    self.dishes.add(dish)

                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, amount)
