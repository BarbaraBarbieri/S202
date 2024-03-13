from database import Database
from dataset.pokemon_dataset import pokemonDataset
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase(pokemonDataset)

pokedex = Pokedex(db)

pokemon_info = pokedex.getPokemonByName("Bulbasaur")
print(pokemon_info)

fire_pokemons = pokedex.getPokemonsByType("Fire")
print(fire_pokemons)

heavy_pokemons = pokedex.getPokemonsByWeight("85.5 kg")
print(heavy_pokemons)

water_weakness_pokemons = pokedex.getPokemonsByWeakness("Water")
print(water_weakness_pokemons)

evolved_pokemons = pokedex.getPokemonsEvolutionTo("Venusaur")
print(evolved_pokemons)
