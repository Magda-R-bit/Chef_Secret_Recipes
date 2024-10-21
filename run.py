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
    save()

def add_secret_ingredient():
    """
    Add the secret ingredient to the chosen recipe
    """
    name = input("Enter the recipe name to add secret ingredient to: ").strip()

    if name in recipe:
        secret_ingredient = input("Enter the secret ingredient: ").strip()
        recipe[name]["Ingredients"].append(secret_ingredient)
        print(f"Ingredient '{secret_ingredient}' added to recipe '{name}'.")
    else:
        print(f"'{name}' not found in the Chef Secret Recipes.")
    save()

def save():
    """
    Save changes in recipe.json file when adding or deleting
    recipes or ingredients
    """
    with open('recipe.json', "w") as file:
        json.dump(recipe, file, indent=4)

def search_recipe():
    """
    Search for a recipe
    """
    name = input("Enter the recipe name to search: ").strip()
    if name in recipe:
        print(f"\nRecipe for {name}:")
        print("Ingredients:", recipe[name]["Ingredients"])
        print("Instructions:", recipe[name]["Instructions"])
    else:
        print(f"'{name}' not found.")

def search_recipe_by_ingredient():
    """
    Search recipes that contain a specific ingredient
    """
    ingredient = input("Enter the ingredient to search for: ").strip()
    found_recipes = [recipe_name for recipe_name, recipe_data in recipe.items() 
                    if any(ingredient == ingr.strip() for ingr in recipe_data["Ingredients"])]
    
    if found_recipes:
        print(f"\nRecipes that contain '{ingredient}':")
        for recipe_name in found_recipes:
            print(f"- {recipe_name}")
    else:
        print(f"No recipes found with the ingredient '{ingredient}'.")

def display_all_recipes():
    """
    Displays all recipes stored in the Chef Secret Recipes Book
    """
    if recipe:
        print("\nAvailable recipes:")
        for recipe_name in recipe:
            print(f"- {recipe_name}")
    else:
        print("No recipes available.")

def main():
    """
    Main function to display user options
    """
    while True:
        print("\nChef Secret Recipes Book:")
        print("1. Add a new recipe")
        print("2. Add a secret ingredient to a recipe")
        print("3. Search for a recipe by name")
        print("4. Search for recipes by an ingredient you have in the fridge")
        print("5. Display all recipes")

        choice = input("Choose one option: ").strip()
        if choice == "1":
            add_new_recipe()
        elif choice == "2":
            add_secret_ingredient()
        elif choice == "3":
            search_recipe()
        elif choice == "4":
            search_recipe_by_ingredient()
        elif choice == "5":
            display_all_recipes()
            break
        else:
            print("Invalid choice, please try again.")

# Call the main function
if __name__ == "__main__":
    main()