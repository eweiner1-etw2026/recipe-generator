# recipe-generator

Project Title: Recipe Generator

Project Description: A Python program that allows the user to input food items to generate a list of possible recipes using those ingredients. The purpose is for when you want to make dinner from what you already have at home. The program searches a Kaggle database of recipes for the inputted food item and returns a list of recipes that contain those items. The generated recipes will also include nutrition information (calories, macronutrients, etc.). Once a recipe is selected by the user, the program will search a UDSA database for the nutritional information of the ingridents in that recipe to calculate and return the total macronutrients. 

Project File/Module Structure:


Project Dependencies/Environments/Libraries:


Meeting Project Requirements and Rubric:
Part 1 Requirements:
  1. We have two well-defined classes: class Ingredient and class Recipe. Both of these classes have constructors, attributes, methods, and instance objects. [These two classes must have a relationship: either inheritance or composition.] These are meaningful classes that contain functional logic relevant to the problem of searching databases for either inputted ingredients or selected recipe ingredient nutrional information. These are not empty or trivial structures.
  2. The recipegeneratorcodekaggle.py module defines five meaningful, well-defined functions that contribute directly to solving the identified problem. They work to read a CSV file and return a list of recipe objects, ask the user to input least one ingredient and return a list, determine the five shortest recipes that use every inputted ingredient, turn the data insto a list, and display the matches and return the one the user picks.
  3. We use two advanced Python libraries for data and processing, Pandas and [Requests # Does this one count?]. The libraries provide critical functionality to the program and are not used in a superfluous way. The Pandas library allows us to manipulate and analyze tabular data efficiently from the Kaggle database CSV file so we can best search for recipes that contain user-inputted ingredients. [The Requests library allows us to send HTTP requests, interact with web resources, and retrieve information from the online USDA FoodData Central database server so ingredient nutritional information can be accessed with our API key.] 
  4. Include at least two distinct exception-handling scenarios (e.g., invalid input, file/data loading errors, type errors, runtime/math errors) and at least two functional Pytest test cases validating program logic.
  5. We perform meaningful data I/O by reading from a CSV file from a Kaggle database to access potential recipes and web scraping to access nutritional data from the online USDA FoodData Central database.
  6. Loop statements, both for and while, are used numerous times throughout both user-defined modules and within the main.ipynb. Many if statements also are used thorughout both user-defined modules and within the main.ipynb. These statements all demonstrate logical control flow by [wip].
  7. [We use two mutable types: lists and a dictonary. We also use two immutable types: number (int) and string. # Confirm nothing else was used with others.] 
  8. __str__()  is implemented in both of our user-defined modules. Two additional operator overloads __lt__() and __eq__() are also used. 
  9. [A proper docstring, header information, and meaningful comments for each module, class, and function. Docstrings must be placed immediately below the definition (class, function) or at the very beginning of a module.]
  10. __name__ is used in both of our user-defined modules to distinguish between the main program code and the module code, making it easier to test our code. This allows us to test the individual modules [with Pytest #?] without running the entire program when __name__ == “__main__”.

Part 2
  1. List comp
  2. Built-in library
  3. Generator
  4. One special function (zip)

Rubric:
  1. Program correctness (20 points). The program executes successfully and produces correct results for representative inputs, including relevant edge cases. Invalid inputs and errors are handled appropriately.
  2. Part 1 requirements (20 points). The project satisfies all ten Part 1 requirements, including meaningful classes and their relationship, functions, advanced libraries, exception handling, at least two functional PyTest test cases, data I/O, control flow, mutable and immutable types, special methods, documentation, and appropriate use of __name__.
  3. Part 2 requirements (10 points). The project meaningfully implements at least four components from Part 2 and identifies them in the README.md.
  4. Proper code structure (5 points). The main program is in main.ipynb, with supporting functions and classes organized into meaningful .py modules.
  4. Meaningful names and consistent formatting (5 points). Variables, functions, classes, and modules use descriptive names that follow Python naming conventions. Formatting is clear and consistent.
  5. Clear docstrings, header information, and meaningful comments (5 points). Modules, classes, and functions are appropriately documented. Comments explain relevant logic and design decisions.
  6. Logical program flow (5 points). Code is readable, logically organized, and avoids unnecessary complexity or duplication.
  7. Comprehensive README.md and submission completeness (8 points). The repository includes all required files and documentation, including data sources, dependencies, environment and kernel information, detailed setup and execution instructions, requirement mappings, and team contributions.
  8. Video: Project pitch (5 points). The first 1–2 minutes clearly explain the problem, intended users, key features, benefits, and what the program achieves. The presentation communicates why someone should use the program.
  9. Video: Live demonstration and technical explanation (7 points). The next 2 minutes demonstrate the working program with actual inputs and outputs, explain its features, and briefly describe how the notebook, modules, classes, and data connect.

Instructions for Running Program:
1. 

Group Members:
- Rian Chowdhury (ID: 10460792) - rchowdh2@stevens.edu
- Kaylyn Sullivan (ID: 20006570) - ksulliv3@stevens.edu
- Emily Weiner (ID: 20013972) - eweiner1@stevens.edu

Contributions:
- Rian: Coding, testing, and debugging ingredients.py module. Editing README.md.
- Kaylyn: Coding, testing, and debugging recipegeneratorcodekaggle.py module. Editing README.md.
- Emily: Coding, testing, and debugging main.ipynb. Writing README.md.

Project Video Link:


Include in this file based on Overall Requirements for the project:
DONE [Project title]
DONE [Project description, including project overview and functionalities]
Project file/module structure
Project dependencies/environments/libraries, and how to install them on Windows or Mac. For Jupyter Notebook, specify the kernel information
[WIP] How the project requirements (both Parts 1 and 2) and grading rubrics (on page 3) are met
Step-by-step and detailed instructions on how to run the program on Windows or Mac.
DONE [Group member names, emails, and Stevens IDs]
DONE [Main contributions of each group member]
Project Video - YouTube Unlisted Link
