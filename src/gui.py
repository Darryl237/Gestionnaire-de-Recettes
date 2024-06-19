import tkinter as tk
import customtkinter as ctk
from recipe_manager import RecipeManager

def gui_interface():
    manager = RecipeManager('src/data/recipes.json')

    app = ctk.CTk()
    app.geometry("400x400")
    app.title("Recipe Manager")

    def add_recipe():
        title = title_entry.get()
        ingredients = ingredients_entry.get().split(',')
        instructions = instructions_entry.get()
        manager.add_recipe(title, ingredients, instructions)
        update_recipe_list()
        title_entry.delete(0, tk.END)
        ingredients_entry.delete(0, tk.END)
        instructions_entry.delete(0, tk.END)

    def update_recipe_list():
        recipes = manager.list_recipes()
        recipes_listbox.delete(0, tk.END)
        for recipe in recipes:
            recipes_listbox.insert(tk.END, recipe["title"])

    title_label = ctk.CTkLabel(app, text="Title:")
    title_label.pack()
    title_entry = ctk.CTkEntry(app)
    title_entry.pack()

    ingredients_label = ctk.CTkLabel(app, text="Ingredients (comma separated):")
    ingredients_label.pack()
    ingredients_entry = ctk.CTkEntry(app)
    ingredients_entry.pack()

    instructions_label = ctk.CTkLabel(app, text="Instructions:")
    instructions_label.pack()
    instructions_entry = ctk.CTkEntry(app)
    instructions_entry.pack()

    add_button = ctk.CTkButton(app, text="Add Recipe", command=add_recipe)
    add_button.pack()

    recipes_listbox = tk.Listbox(app)
    recipes_listbox.pack(fill=tk.BOTH, expand=True)

    update_recipe_list()
    app.mainloop()

if __name__ == "__main__":
    gui_interface()
