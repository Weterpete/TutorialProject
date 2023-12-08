from pokemon import Pokemon


class PokemonFactory:
    def __init__(self):
        self.count = 0

    def create_pokemon(self, pokemon_type):
        pokemon = Pokemon(pokemon_type)
        self.count = self.count + 1
        return pokemon