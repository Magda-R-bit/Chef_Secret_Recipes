import json

with open('recipe.json', 'r') as file:
    recipe = json.load(file)


def add_new_recipe():
    """
    Add new recipe to Chef Secret Recipes Book in recipe.json file
    """
    name = input("Enter the recipe name: ").strip()
    ingredients = input("Enter ingredients separated by commas: ").split(",")
    instructions = input("Enter instructions: ").strip()

    recipe[name] = {"Ingredients": ingredients, "Instructions": instructions}
    print(f"Recipe '{name}' added successfully.")

def main():
    """
    Main function to display user options
    """
    while True:
        print("\nChef Secret Recipes Book:")
        print("1. Add a new recipe")

        choice = input("Choose one option: ").strip()
        if choice == "1":
            add_new_recipe()

# Call the main function
if __name__ == "__main__":
    main()