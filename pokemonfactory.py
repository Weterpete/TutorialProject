import configpokemon
import utilities
from pokemon import Pokemon


class PokemonFactory:
    def __init__(self):
        self.count = 0

    def create_pokemon(self, pokemon_type):
        randomNumber = -1

        if pokemon_type == "G":
            randomNumber = utilities.generate_random_number(configpokemon.ENCOUNTER_RANGE_START, configpokemon.ENCOUNTER_RANGE_END)

        pokemon = Pokemon(pokemon_type, randomNumber)
        self.count = self.count + 1

        return pokemon