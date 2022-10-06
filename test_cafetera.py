import unittest
from cafetera import CoffeeMachinePlus


class Test(unittest.TestCase):

    def testCase_just_coffee(self):
        cafetera = CoffeeMachinePlus()
        cafetera.add_resource('coins')
        cafetera.add_resource("coffee", 31)
        result = cafetera.make_coffee("coffee_alone")
        self.assertTrue(result)

    def testCase_coffee_no_resources(self):
        cafetera = CoffeeMachinePlus()
        result = cafetera.make_coffee("coffee_alone")
        self.assertFalse(result)

    def testCase_check_resources(self):
        cafetera = CoffeeMachinePlus()
        result = cafetera.is_it_enough("coffee_alone")
        self.assertFalse(result)

    def testCase_sum_resources(self):
        cafetera = CoffeeMachinePlus()
        cafetera.add_resource("coffee", 29)
        cafetera.add_resource("coffee", 1)
        # print(cafetera.resources['coffee'])
        result = cafetera.resources['coffee']
        self.assertEqual(result, 30)

    def testCase_insert_sugar(self):
        cafetera = CoffeeMachinePlus()
        cafetera.add_resource("sugar", 29)
        result = cafetera.resources['sugar']
        self.assertEqual(result, 29)

    def testCase_make_latte(self):
        cafetera = CoffeeMachinePlus()
        cafetera.add_resource('coins')
        cafetera.add_resource("sugar", 100)
        cafetera.add_resource("milk", 100)
        cafetera.add_resource("coffee", 100)
        result = cafetera.make_coffee("latte")
        self.assertTrue(result)
        self.assertEqual(cafetera.resources["coffee"], 100-30)
        self.assertEqual(cafetera.resources["milk"], 100-70)
        self.assertEqual(cafetera.resources["coins"], 0)

    def testCase_how_much_recipes(self):
        cafetera = CoffeeMachinePlus()
        cafetera.add_resource("coffee", 300)
        cafetera.add_resource("coins", 5)
        result = cafetera.how_much_recipes('coffee_alone')
        self.assertEqual(result, 5)

    def testCase_how_much_recipes_2(self):
        cafetera = CoffeeMachinePlus()
        cafetera.add_resource("coffee", 300)
        cafetera.add_resource("coins", 15)
        result = cafetera.how_much_recipes('coffee_alone')
        self.assertEqual(result, 10)
        
    def testCase_resources(self):
        cafetera = CoffeeMachinePlus()
        cafetera.add_resource("coffee", 300)
        cafetera.add_resource("coins", 15)
        cafetera.add_resource("sugar", 2)
        cafetera.change_recipe_item('coffee_alone', 'sugar', 5)
        self.assertEqual(cafetera.recipes['coffee_alone']['sugar'], 25)


if __name__ == "__main__":
    unittest.main()
