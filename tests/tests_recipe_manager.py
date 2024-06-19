import unittest
from src.recipe_manager import RecipeManager
import os
import json

class TestRecipeManager(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_recipes.json'
        self.manager = RecipeManager(self.test_file)
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_recipe(self):
        self.manager.add_recipe('Test Recipe', ['ingredient1', 'ingredient2'], 'Test instructions')
        recipes = self.manager.list_recipes()
        self.assertEqual(len(recipes), 1)
        self.assertEqual(recipes[0]['title'], 'Test Recipe')
    
    def test_list_recipes(self):
        self.manager.add_recipe('Test Recipe 1', ['ingredient1'], 'Instructions 1')
        self.manager.add_recipe('Test Recipe 2', ['ingredient2'], 'Instructions 2')
        recipes = self.manager.list_recipes()
        self.assertEqual(len(recipes), 2)
        self.assertEqual(recipes[0]['title'], 'Test Recipe 1')
        self.assertEqual(recipes[1]['title'], 'Test Recipe 2')

if __name__ == '__main__':
    unittest.main()
