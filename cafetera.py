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
        """
        It takes a recipe, an item, and a new quantity, and then changes the quantity of that item in
        the recipe to the new quantity
        
        :param recipe: the name of the recipe
        :param item: the item to be changed
        :param new_quantity: the new quantity of the item in the recipe
        """
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
        """
        If there are enough resources to make the recipe, return True. Otherwise, return False
        
        :param recipe: the name of the recipe you want to make
        :return: A boolean value.
        """
        recipe_elements = self.recipes[recipe].items()
        for element, quantity in recipe_elements:
            if self.resources[element] < quantity:
                return False
        return True

    def how_much_recipes(self, recipe_name):
        """
        We get the recipe elements, and then we divide the resource quantity by the recipe quantity
        
        :param recipe_name: The name of the recipe you want to make
        :return: The min amount of recipes that can be made.
        """
        recipe_elements = self.recipes[recipe_name].items()
        return min([self.resources[elem] // qty for elem, qty in recipe_elements if qty])

    def substract_items(self, recipe):
        for element, quantity in self.recipes[recipe].items():
            self.resources[element] -= int(quantity)
        return True

    def add_resource(self, type, amount=1):
        self.resources[type] += amount
