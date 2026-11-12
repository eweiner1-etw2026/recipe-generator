# Name: Rian Chowdhury, Kaylyn Sullivan, Emily Weiner
# Email: rchowdh2@stevens.edu, ksulliv3@stevens.edu, eweiner1@stevens.edu
# Date: 12/16/2026
# File Name: ingredients.py
# Interpreter: Python 3.14.7
# Description: Module used for importing the Ingredient class.

import os
import requests

class Ingredient:
    """
    This class is used to define the food items the user has available, which will subsequently be used as recipe ingredients.
    To construct the instance objects, the program must connect to the USDA FoodData Central database via an API.

    This class has the following class attributes:
        api: The API key, stored in a .env file for security purposes.
        base_url: The URL used to retrieve information from the FoodData Central database.

    This class has the following instance attributes:
        name: The name of the food item (input by the user).
        data_list: A list of the top 5 results when retrieving information from the database (TEMPORARY).
        item_description: The description of the selected item (after narrowing down options).
        item_id: The FoodData Central ID of the selected item (after narrowing down options).
        nutrition_data: All the available nutrient data available for the selected item (after narrowing down options).

    This class has the following instance methods:
        __init__: The constructor. Sets the instance attributes according to the other instance methods.
        search: The initial search query for the database. Outputs the top 5 results based on the item name.
        select_item: Allows the user to narrow down their options to 1 result.
        nutrition: Performs another database query to retrieve nutritional data for the selected item.
        display_nutritional_data: Prints the nutritional data retrieved from the database.
        __str__: Operator overloading for "print".
        __eq__: Operator overloading for " == ".
    """

    # CLASS ATTRIBUTES
    api = os.environ['USDA_API_KEY'] # API KEY WILL BE INCLUDED IN .env FILE
    base_url = 'https://api.nal.usda.gov/fdc/v1'

    # CONSTRUCTOR
    def __init__(self, name):
        self.name = name
        self.data_list = self.search() # INSTANCE METHODS ARE USED TO UPDATE INSTANCE ATTRIBUTES
        selection = self.select_item()
        if selection is not None:
            [self.item_description, self.item_id] = selection # SETS DESCRIPTION AND ID OF SELECTED RESULT
        else:
            self.item_description = None
            self.item_id = 'N/A'
        self.nutrition_data = self.nutrition()
        delattr(self, 'data_list') # TEMPORARY INSTANCE ATTRIBUTE IS REMOVED ONCE ITEM ID AND NUTRITIONAL DATA ARE RETRIEVED

    # INSTANCE METHODS
    def search(self):
        try:
            full_url = f'{self.base_url}/foods/search'
            search_parameters = {'api_key': self.api, 'query': self.name, 'pageSize': 5} # LIMIT SEARCH RESULTS TO TOP 5
            response = requests.get(full_url, params = search_parameters)
        except requests.exceptions.ConnectionError:
            print('Connection Error')
            return 0
        if response.status_code == 200: # STATUS CODE 200 INDICATES SUCCESSFUL CONNECTION TO DATABASE
            data = response.json()
            print('\n')
            for food in data.get('foods', []): # get METHOD RETRIEVES DICTIONARY VALUES BASED ON KEY NAME, WITHOUT RISK OF KeyError
                print(f'Description: {food.get('description')}')
                print(f'FDC ID: {food.get('fdcId')}')
                print('---')
            return [food for food in data.get('foods', [])]
        else:
            print(f'Error: {response.status_code}')
            return 0

    def select_item(self):
        if self.data_list != 0:
            x = (input('\nSelect an option (1-5), or press 0 to try again: ')) # MUST PICK ONE OF THE TOP 5 OPTIONS
            if x.isdigit():
                int_x = int(x)
                if int_x == 0:
                    self.name = input('Please enter the name of the item: ')
                    self.data_list = self.search()
                    self.select_item()
                elif int_x not in range(1,6):
                    print('Invalid: must be a number from 1-5')
                    return None
                else:
                    selected_item = self.data_list[int_x - 1]
                    description = selected_item.get('description')
                    id = selected_item.get('fdcId')
                    return [description, id]
            else:
                print('Invalid: must input a number')
                return None
        else:
            return None

    def nutrition(self):
        url = f'{self.base_url}/food/{self.item_id}?api_key={self.api}'
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            print('Connection Error')
            return 0
        if response.status_code == 200:
            details = response.json()
            return details.get('foodNutrients', [])
        else:
            print(f'Error: {response.status_code}')
            return 0

    def display_nutrient_data(self):
        if self.nutrition_data == 0:
            print('No nutrient data is available.')
        else:
            print('Nutrients per 100 g/mL:\n') # PRINT ALL AVAILABLE NUTRITIONAL DATA FOR SELECTED RESULT
            for nutrient in self.nutrition_data:
                name = nutrient.get('nutrient', {}).get('name')
                amount = nutrient.get('amount')
                unit = nutrient.get('nutrient', {}).get('unitName')
                if amount is not None:
                    print(f'{name}: {amount} {unit}')

    # OPERATOR OVERLOADING
    def __str__(self): # WILL PRINT SELECTED ITEM NAME, DESCRIPTION, AND ID
        return f'Name: {self.name}\nDescription: {self.item_description}\nFoodData Central ID: {self.item_id}'

    def __eq__(self, other): # WILL CHECK TO SEE IF TWO FOOD ITEMS HAVE MATCHING ID NUMBERS
        if self.item_id == other.item_id:
            return f'Item "{self.name}" and item "{other.name}" are the same (ID: {self.item_id}).'
        else:
            return f'Item "{self.name}" (ID: {self.item_id}) and item "{other.name}" (ID: {other.item_id}) are not the same.'

print(__name__) # IS DEFINED AS __main__ ONLY WHEN RUNNING THE FILE DIRECTLY
# THE TEST CODE BELOW WILL NOT RUN IF THE MODULE IS IMPORTED
if __name__ == '__main__':
    x = input('Please enter the name of the item: ')
    test_ingredient = Ingredient(x)
    print('\n')
    print(test_ingredient)
    print('\n')
    test_ingredient.display_nutrient_data()
    print('\n')
    for key in test_ingredient.__dict__:
        print(key) # PRINTS ALL OF THE INSTANCE ATTRIBUTES THAT CURRENTLY EXIST FOR THE OBJECT (KEYS)
    print('\n')
    print(test_ingredient.__dict__) # PRINTS BOTH THE KEYS AND VALUES IN __dict__

    print('\n')
    y = input('Please enter the name of another item: ')
    test_ingredient2 = Ingredient(y)
    print('\n')
    print(test_ingredient2)
    print('\n')
    test_ingredient2.display_nutrient_data()
    print('\n')
    print(test_ingredient == test_ingredient2)