import json

with open('recipe.json', 'r') as file:
    recipe = json.load(file)

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.MAGENTA + """
          ╔═╗┬ ┬┌─┐┌─┐  ╔═╗┌─┐┌─┐┬─┐┌─┐┌┬┐  ╦═╗┌─┐┌─┐┬┌─┐┌─┐┌─┐
          ║  ├─┤├┤ ├┤   ╚═╗├┤ │  ├┬┘├┤  │   ╠╦╝├┤ │  │├─┘├┤ └─┐
          ╚═╝┴ ┴└─┘└    ╚═╝└─┘└─┘┴└─└─┘ ┴   ╩╚═└─┘└─┘┴┴  └─┘└─┘""")
print(Fore.GREEN + """
                 _________________     _________________
              .:|                 '. .'                 |:.
              |||    Chef Secret    |  - Spaghetti      |||
              |||      Recipes      |  - Carbonara      |||
              |||                   |  - Risotto        |||
              |||                   |  - Wontons        |||
              |||     .------.      |  - Hungarian      |||
              |||  ::`  Soup  `::   |    Hash Browns    |||
              |||    '.______.'     |                   |||
              |||_________________  | __________________|||
              |.'================== | =================='.|
              '-------------------~___~-------------------' """)


def add_new_recipe():
    """
    Add new recipe to Chef Secret Recipes Book in recipe.json file
    """
    while True:
        name = input(
            Fore.LIGHTYELLOW_EX + "Enter the recipe name (letters only): "
            ).strip()

        if all(part.isalpha() for part in name.split()):
            name = name.title()
            break
        else:
            print(Fore.RED + "Invalid name. Please use letters only.")

    ingredients = [ingredient.strip() for ingredient in input(
        Fore.LIGHTYELLOW_EX + "Enter ingredients separated by commas: "
        ).split(",")]

    instructions = [instruction.strip() for instruction in input(
        Fore.LIGHTYELLOW_EX + "Enter instructions: "
        ).split(",")]

    recipe[name] = {"Ingredients": ingredients, "Instructions": instructions}
    print(Fore.GREEN + f"Recipe '{name}' added successfully.")
    save()
    display_recipe(name)


def add_secret_ingredient():
    """
    Add the secret ingredient to the chosen recipe
    """
    name = input(
        Fore.LIGHTYELLOW_EX +
        "Enter the recipe name to add secret ingredient to: "
        ).strip().title()

    if name in recipe:
        secret_ingredient = input(
            Fore.LIGHTYELLOW_EX +
            "Enter the secret ingredient(prefix secret ingredient with *): "
            ).strip().lower()
        recipe[name]["Ingredients"].append(secret_ingredient)
        print(
            Fore.GREEN +
            "Secret Ingredient" +
            Fore.CYAN + f"'{secret_ingredient}'" + Style.RESET_ALL +
            Fore.GREEN + f"added to recipe" + Style.RESET_ALL +
            Fore.CYAN + f" '{name}'."
            )
    else:
        print(Fore.RED + f"'{name}' not found in the Chef Secret Recipes.")
    save()
    display_recipe(name)


def save():
    """
    Save changes in recipe.json file when adding or deleting
    recipes or ingredients
    """
    with open('recipe.json', "w") as file:
        json.dump(recipe, file, indent=4)


def search_recipe():
    """
    Search for a recipe by name
    """
    name = input(
        Fore.LIGHTYELLOW_EX + "Enter the recipe name to search: "
        ).strip().title()
    if name in recipe:
        print(Fore.LIGHTYELLOW_EX + f"\nRecipe for {name}:")
        # Display list with one ingredient per line
        print(Fore.LIGHTYELLOW_EX + "\nIngredients:")
        for ingredient in recipe[name]["Ingredients"]:
            print(f"- {ingredient}")
        # Display instruction with numbered steps
        print(Fore.LIGHTYELLOW_EX + "\nInstructions:")
        for step, instruction in enumerate(
            recipe[name]["Instructions"], start=1
        ):
            print(f"{step}. {instruction}")
    else:
        print(Fore.RED + f"'{name}' not found.")


def search_recipe_by_ingredient():
    """
    Search for recipes that contain a specific ingredient,
    including secret ingredients marked with '*'
    """
    ingredient = input(
        Fore.LIGHTYELLOW_EX + "Enter the ingredient to search for: "
        ).strip().lower()
    found_recipes = [
        recipe_name for recipe_name, recipe_data in recipe.items()
        if any(ingredient == ingr.lstrip("*").strip().lower()
               for ingr in recipe_data["Ingredients"])
    ]

    if found_recipes:
        print(Fore.GREEN + f"\nRecipes that contain '{ingredient}':")
        for recipe_name in found_recipes:
            print(f"- {recipe_name}")
            # Indicate the Secret Ingredients
            for ingr in recipe[recipe_name]["Ingredients"]:
                if ingredient == ingr.lstrip("*").strip().lower():
                    if ingr.startswith("*"):
                        print(
                            f" * Secret Ingredient: {ingr.lstrip("*").strip()}"
                        )
                    else:
                        print(f" Ingredient: {ingr.strip()}")
    else:
        print(
            Fore.RED +
            f"No recipes found with the ingredient '{ingredient}'.")


def display_all_recipes():
    """
    Display all recipes stored in
    the Chef Secret Recipes Book
    """
    if recipe:
        print(Fore.LIGHTMAGENTA_EX + "\nAvailable recipes:")
        for recipe_name in recipe:
            print(f"- {recipe_name}")
    else:
        print(Fore.RED + "No recipes available.")


def delete_recipe():
    """
    Delete a recipe by name
    """
    name = input(
        Fore.LIGHTYELLOW_EX + "Enter the recipe name to delete: "
        ).strip().title()

    if name in recipe:
        del recipe[name]
        print(Fore.GREEN + f"Recipe '{name}' deleted successfully.")
    else:
        print(Fore.RED + f"'{name}' not found in the recipe book.")
    save()


def delete_ingredient():
    """
    Delete an ingredient from a recipe by name
    """
    name = input(
        Fore.LIGHTYELLOW_EX +
        "Enter the recipe name to delete an ingredient from: "
        ).strip().title()

    if name in recipe:
        ingredients = recipe[name]["Ingredients"]
        ingredient_to_delete = input(
            "Enter the name of the ingredient to delete: ").lower()
        if ingredient_to_delete in ingredients:
            ingredients.remove(ingredient_to_delete)
            print(
                Fore.GREEN +
                f"Ingredient '{ingredient_to_delete}' "
                f"deleted from recipe '{name}'."
                )
            save()
        else:
            print(
                Fore.RED +
                f"Ingredient '{ingredient_to_delete}'"
                f"not found in recipe '{name}'."
                )
    else:
        print(Fore.RED + f"'{name}' not found in the Chef Secret Recipes.")
    display_recipe(name)


def display_recipe(name):
    """
    Display the specified recipe by name, including updated ingredients
    """
    recipe_data = recipe[name]

    print(Fore.LIGHTYELLOW_EX + f"\nRecipe '{name}':")
    print(Fore.LIGHTYELLOW_EX + "\nIngredients:")
    for ingredient in recipe_data["Ingredients"]:
        if ingredient.startswith("*"):
            print(f" - Secret Ingredient: {ingredient.lstrip('*').strip()}")
        else:
            print(f" - {ingredient}")

    print(Fore.LIGHTYELLOW_EX + "\nInstruction:")
    for step_number, instruction in enumerate(
         recipe_data["Instructions"], start=1):
        print(f" Step {step_number}: {instruction}")


def main():
    """
    Main function to display user options
    """
    while True:
        print(Fore.LIGHTMAGENTA_EX + "\nChef Secret Recipes Book:")
        print("1. Add a new recipe")
        print("2. Add a secret ingredient to a recipe")
        print("3. Search for a recipe by name")
        print("4. Search for recipes by an ingredient you have in the fridge")
        print("5. Display all recipes")
        print("6. Delete a recipe")
        print("7. Delete an ingredient from a recipe")
        print("8. Exit")

        choice = input(Fore.CYAN + "Choose one option: ").strip()
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
        elif choice == "6":
            delete_recipe()
        elif choice == "7":
            delete_ingredient()
        elif choice == "8":
            print(Fore.GREEN + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice, please try again.")


# Call the main function
if __name__ == "__main__":
    main()
