from database import Database
from helper.writeAJson import writeAJson

class Pokedex:

    def __init__(self, database: Database):
        self.database = database
    
    def getPokemonByName(self, name: str):
        pokemon_data = self.database.collection.find({"name": name})
        writeAJson(pokemon_data, "pokemons_by_name_" + name)
        return pokemon_data

    def getPokemonsByType(self, type: str):
        pokemon_data =  self.database.collection.find({"type": type})
        writeAJson(pokemon_data, "pokemons_by_type_" + type)
        return pokemon_data

    def getPokemonsByWeight(self, weight: str):
        pokemon_data = self.database.collection.find({"weight": weight})
        writeAJson(pokemon_data, "pokemons_by_weight_" + weight.replace(" ", ""))
        return pokemon_data

    def getPokemonsByWeakness(self, weakness: str):
        pokemon_data = self.database.collection.find({"weaknesses": weakness})
        writeAJson(pokemon_data, "pokemons_by_weakness_" + weakness)
        return pokemon_data

    def getPokemonsEvolutionTo(self, name: str):
        pokemon_data = self.database.collection.find({"next_evolution.name": name})
        writeAJson(pokemon_data, "pokemons_evolution_to_" + name)
        return pokemon_data
