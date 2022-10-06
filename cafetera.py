class CoffeeMachinePlus:
    def __init__(self):
        self.resources = {
            "coffee": 0,
            "milk": 0,
            "sugar": 0,
            "tea": 0,
            "coins": 0
        }
        self.recipes = {
            "coffee_alone": {
                "coffee": 30,
                "coins": 1,
                "sugar": 0,
            },
            "coffee_double": {
                "coffee": 60,
                "coins": 1,
                "sugar": 0,
            },
            "tea_simple": {
                "tea": 10,
                "coins": 1,
                "sugar": 0,
            },
            "latte": {
                "coffee": 30,
                "milk": 70,
                "coins": 1,
                "sugar": 0,
            },
            "capuccino": {
                "coffee": 40,
                "milk": 60,
                "coins": 1,
                "sugar": 0,
            },
        }

    def change_recipe_item(self, recipe, item, new_quantity):
        recipe_elements = self.recipes[recipe].items()
        for element, quantity in recipe_elements:
            if element == item:
                self.recipes[recipe][item] = 5 * new_quantity  # five levels of sugar

    def make_coffee(self, recipe, sugar=0):
        if self.is_it_enough(recipe):
            self.substract_items(recipe)
            return True
        return False

    def is_it_enough(self, recipe):
        recipe_elements = self.recipes[recipe].items()
        for element, quantity in recipe_elements:
            # Loop trough specific recipe elements.
            # Ej : Element == coffe and qty == 30
            if self.resources[element] < quantity:
                return False
        return True

    def how_much_recipes(self, recipe_name):
        recipes_counter = []
        # get items from each recipe Ej: {'coffee' : 30}
        recipe_elements = self.recipes[recipe_name].items()
        for element, quantity in recipe_elements:
            try:
                recipes_counter.append(self.resources[element] // quantity)
            except ZeroDivisionError:
                raise ValueError('No puedes dividir por 0')
        return min(recipes_counter)

    def substract_items(self, recipe):
        for element, quantity in self.recipes[recipe].items():
            self.resources[element] -= int(quantity)
        return True

    def add_resource(self, type, amount=1):
        self.resources[type] += amount
