import json
import os

class RecipeManager:
    def __init__(self, data_file):
        self.data_file = data_file
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                file.write('[]')
        else:
            self.data = {"recipes": []}
    
    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_recipe(self, title, ingredients, instructions):
        recipe = {
            "title": title,
            "ingredients": ingredients,
            "instructions": instructions
        }
        self.data["recipes"].append(recipe)
        self.save_data()

    def list_recipes(self):
        return self.data["recipes"]





