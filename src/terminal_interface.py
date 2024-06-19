from recipe_manager import RecipeManager

def terminal_interface():
    manager = RecipeManager('src/data/recipes.json')

    while True:
        print("1. Add Recipe")
        print("2. List Recipes")
        print("3. Quit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            ingredients = input("Ingredients (comma separated): ").split(',')
            instructions = input("Instructions: ")
            manager.add_recipe(title, ingredients, instructions)
            print("Recipe added successfully.")
        elif choice == '2':
            recipes = manager.list_recipes()
            for i, recipe in enumerate(recipes):
                print(f"{i + 1}. {recipe['title']}")
                print(f"   Ingredients: {', '.join(recipe['ingredients'])}")
                print(f"   Instructions: {recipe['instructions']}")
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")
