import unittest

from cafetera import *


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.cafetera = CoffeeMachinePlus()
        return super().setUp()

    def testCase_just_coffee(self):
        self.cafetera.add_resource("coins")
        self.cafetera.add_resource("coffee", 32)
        result = self.cafetera.make_coffee("coffee_alone")
        self.assertTrue(result)

    def testCase_coffee_no_resources(self):
        result = self.cafetera.make_coffee("capuccino")
        self.assertFalse(result)

    def testCase_check_resources(self):
        result = self.cafetera.is_it_enough("tea_simple")
        self.assertFalse(result)

    def testCase_sum_resources(self):
        self.cafetera.add_resource("coffee", 29)
        self.cafetera.add_resource("coffee", 1)
        # print(self.cafetera.resources['coffee'])
        result = self.cafetera.resources["coffee"]
        self.assertEqual(result, 30)

    def testCase_insert_sugar(self):
        self.cafetera.add_resource("sugar", 29)
        result = self.cafetera.resources["sugar"]
        self.assertEqual(result, 29)

    def testCase_make_latte(self):
        self.cafetera.add_resource("coins")
        self.cafetera.add_resource("sugar", 100)
        self.cafetera.add_resource("milk", 100)
        self.cafetera.add_resource("coffee", 100)
        result = self.cafetera.make_coffee("latte")
        self.assertTrue(result)
        self.assertEqual(self.cafetera.resources["coffee"], 100 - 30)
        self.assertEqual(self.cafetera.resources["milk"], 100 - 70)
        self.assertEqual(self.cafetera.resources["coins"], 0)

    def testCase_how_much_recipes(self):
        self.cafetera.add_resource("coffee", 300)
        self.cafetera.add_resource("coins", 5)
        result = self.cafetera.how_much_recipes("coffee_alone")
        self.assertEqual(result, 5)

    def testCase_resources(self):
        self.cafetera.add_resource("coffee", 300)
        self.cafetera.add_resource("coins", 15)
        self.cafetera.add_resource("sugar", 2)
        self.cafetera.change_recipe_item("coffee_alone", "sugar", 5)
        self.assertEqual(self.cafetera.recipes["coffee_alone"]["sugar"], 25)


if __name__ == "__main__":
    unittest.main()
