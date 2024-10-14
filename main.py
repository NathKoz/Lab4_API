# pokemon_info.py
import requests

# Function to get Pokémon data from the API
def get_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    print(f"Error: Pokémon '{pokemon_name}' not found.")
    return None

# Function to display Pokémon details
def display_pokemon_info(pokemon_data):
    if pokemon_data:
        name = pokemon_data['name'].capitalize()
        pokemon_id = pokemon_data['id']
        height = pokemon_data['height']
        weight = pokemon_data['weight']
        types = [t['type']['name'].capitalize() for t in pokemon_data['types']]
        abilities = [a['ability']['name'].capitalize() for a in pokemon_data['abilities']]

        print(f"\nPokémon: {name}")
        print(f"ID: {pokemon_id}")
        print(f"Height: {height / 10} m")
        print(f"Weight: {weight / 10} kg")
        print(f"Type(s): {', '.join(types)}")
        print(f"Abilities: {', '.join(abilities)}")
    else:
        print("No data to display.")

# Main function to interact with the user
def main():
    print("Welcome to the Pokémon Info Finder!")
    while True:
        pokemon_name = input("\nEnter the name of a Pokémon (or 'exit' to quit): ").strip()
        
        if pokemon_name.lower() == 'exit':
            print("Goodbye!")
            break

        pokemon_data = get_pokemon_data(pokemon_name)
        display_pokemon_info(pokemon_data)

# Run the main function
if __name__ == '__main__':
    main()
