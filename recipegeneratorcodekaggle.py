#Name: Kaylyn Sullivan
#Email: ksulliv3@stevens.edu
#Date: 11/17/2026
#File Name: recipegeneratorcode.py
#Description: Finds recipes in the Kaggle dataset

import pandas as pd

class Recipe:
    """Stores one recipe: name, ingredients and steps"""
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def uses(self, food):
        """Returns True if a word in any ingredient starts with this food (ham won't match graham)"""
        for ingredient in self.ingredients:
            if (" " + food) in (" " + ingredient):
                return True
        return False

    def __str__(self):
        text = f"{self.name}\n\nIngredients:\n"
        for ingredient in self.ingredients:
            text = text + f"- {ingredient}\n"
        text = text + "\nSteps:\n"
        for number, step in enumerate(self.steps):
            text = text + f"{number + 1}. {step}\n" #enumerate starts at 0
        return text

    def __lt__(self, other):
        """Fewer ingredients counts as less than"""
        return len(self.ingredients) < len(other.ingredients)

def text_to_list(text):
    """Turns text into a list"""
    text = text[2:-2]
    text = text.replace('", ', "', ")
    text = text.replace(', "', ", '")
    return text.split("', '")

def load_recipes(file_name):
    """Reads the CSV file and returns a list of recipe objects"""
    table = pd.read_csv(file_name)
    recipes = []
    rows = zip(table["name"], table["ingredients"], table["steps"])
    for name, ingredients, steps in rows:
        recipes.append(Recipe(name, text_to_list(ingredients), text_to_list(steps)))
    return recipes

def ask_for_foods():
    """Asks until the user types at least one ingredient, returns a list"""
    foods = []
    while len(foods) == 0:
        text = input("Type your ingredients, separated by commas: ")
        foods = [food.strip().lower() for food in text.split(",") if food.strip() != ""]
    return foods

def find_recipes(recipes, foods):
    """Returns the 5 shortest recipes that use every food"""
    matches = [recipe for recipe in recipes if all((recipe.uses(food) for food in foods))]
    matches.sort()  # uses __lt__, so fewest ingredients first
    return matches[:5]

def choose_recipe(matches):
    """Shows the matches and returns the one the user picks"""
    for number, recipe in enumerate(matches):
        print(f"{number + 1}. {recipe.name} ({len(recipe.ingredients)} ingredients)")
    while True:
        choice = input(f"Pick a recipe (1-{len(matches)}): ")
        try:
            number = int(choice)
            if 1 <= number <= len(matches):
                return matches[number - 1]
        except ValueError:  # user didn't type a number
            print("Please type a number.")

#only runs when this file is run directly, not when imported
if __name__ == "__main__":
    all_recipes = load_recipes("RAW_recipes.csv")
    matches = find_recipes(all_recipes, ask_for_foods())
    if len(matches) == 0:
        print("No recipes use all of those ingredients")
    else:
        print(choose_recipe(matches))