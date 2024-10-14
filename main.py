import requests
from PIL import Image
from io import BytesIO

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
