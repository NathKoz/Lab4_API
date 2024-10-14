import os
import requests
from PIL import Image
from io import BytesIO

# Function to clear the console based on the user's operating system
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get Pokémon data from the API
def get_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    print(f"Error: Pokémon '{pokemon_name}' not found.")
    return None

# Function to get Ability data from the API
def get_ability_data(ability_name):
    url = f'https://pokeapi.co/api/v2/ability/{ability_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    print(f"Error: Ability '{ability_name}' not found.")
    return None

# Function to get Move data from the API
def get_move_data(move_name):
    url = f'https://pokeapi.co/api/v2/move/{move_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    print(f"Error: Move '{move_name}' not found.")
    return None

# Function to display Pokémon details and sprite
def display_pokemon_info(pokemon_data):
    if pokemon_data:
        name = pokemon_data['name'].capitalize()
        pokemon_id = pokemon_data['id']
        height = pokemon_data['height']
        weight = pokemon_data['weight']
        types = [t['type']['name'].capitalize() for t in pokemon_data['types']]
        abilities = [a['ability']['name'].capitalize() for a in pokemon_data['abilities']]
        sprite_url = pokemon_data['sprites']['front_default']  # Get the front sprite URL

        print(f"\nPokémon: {name}")
        print(f"ID: {pokemon_id}")
        print(f"Height: {height / 10} m")
        print(f"Weight: {weight / 10} kg")
        print(f"Type(s): {', '.join(types)}")
        print(f"Abilities: {', '.join(abilities)}")
        
        # Display the front sprite if it exists
        if sprite_url:
            display_sprite(sprite_url)
        else:
            print("No sprite available for this Pokémon.")
    else:
        print("No data to display.")

# Function to display the Pokémon's sprite
def display_sprite(sprite_url):
    response = requests.get(sprite_url)
    
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.show()  # This will open the sprite in the default image viewer
    else:
        print("Error: Unable to retrieve the sprite.")

# Function to display Ability details in English
def display_ability_info(ability_data):
    if ability_data:
        name = ability_data['name'].capitalize()
        generation = ability_data['generation']['name'].capitalize()

        # Extract the English effect and short effect from effect_entries
        english_effect = None
        english_short_effect = None

        for entry in ability_data['effect_entries']:
            if entry['language']['name'] == 'en':  # Check for English entries
                english_effect = entry['effect']
                english_short_effect = entry['short_effect']
                break

        if english_effect and english_short_effect:
            print(f"\nAbility: {name}")
            print(f"Effect: {english_effect}")
            print(f"Short Effect: {english_short_effect}")
            print(f"Generation: {generation}")
        else:
            print("No English description available for this ability.")
    else:
        print("No data to display.")


# Function to display Move details
def display_move_info(move_data):
    if move_data:
        name = move_data['name'].capitalize()
        power = move_data.get('power', 'N/A')
        pp = move_data['pp']
        type_ = move_data['type']['name'].capitalize()
        generation = move_data['generation']['name'].capitalize()
        accuracy = move_data.get('accuracy', 'N/A')

        print(f"\nMove: {name}")
        print(f"Power: {power}")
        print(f"PP: {pp}")
        print(f"Type: {type_}")
        print(f"Generation: {generation}")
        print(f"Accuracy: {accuracy}")
    else:
        print("No data to display.")

# Main function to interact with the user
def main_menu():
    while True:
        clear_console()
        print("Welcome to the Pokémon Info Finder!")
        print("Choose an option:")
        print("1. Search for Pokémon")
        print("2. Search for Ability")
        print("3. Search for Move")
        print("4. Exit")

        choice = input("\nEnter your choice (1, 2, 3, or 4): ").strip()

        if choice == '1':
            search_pokemon()
        elif choice == '2':
            search_ability()
        elif choice == '3':
            search_move()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

# Function to search for Pokémon
def search_pokemon():
    clear_console()
    pokemon_name = input("\nEnter the name of a Pokémon: ").strip()
    pokemon_data = get_pokemon_data(pokemon_name)
    display_pokemon_info(pokemon_data)
    input("\nPress Enter to return to the main menu...")

# Function to search for Ability
def search_ability():
    clear_console()
    ability_name = input("\nEnter the name of an Ability: ").strip()
    ability_data = get_ability_data(ability_name)
    display_ability_info(ability_data)
    input("\nPress Enter to return to the main menu...")

# Function to search for Move
def search_move():
    clear_console()
    move_name = input("\nEnter the name of a Move: ").strip()
    move_data = get_move_data(move_name)
    display_move_info(move_data)
    input("\nPress Enter to return to the main menu...")

# Run the main function
if __name__ == '__main__':
    main_menu()
