import pygame
import config
import math
import random

import pokemonfactory
from pokemonfactory import PokemonFactory
import utilities
from player import Player
from game_state import GlobalGameState, CurrentGameState
from game_view.map import Map
from game_view.battle import Battle

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.object = []
        self.game_state = GlobalGameState.NONE
        self.current_game_state = CurrentGameState.MAP
        self.camera = [0, 0]
        self.playerHasMoved = False
        self.pokemon_factory = PokemonFactory()
        self.map = Map(screen)
        self.battle = None
        self.hitList = []

    def set_up(self):
        player = Player(1, 26)
        self.player = player
        self.object.append(player)
        print("Do set up")
        self.game_state = GlobalGameState.RUNNING

        self.map.load("01")

    def update(self):
        if self.current_game_state == CurrentGameState.MAP:
            self.playerHasMoved = False
            self.screen.fill(config.BLACK)
            # print("Update")
            self.handleEvents()

            self.map.render(self.screen, self.player, self.object)

            if self.playerHasMoved:
                self.determine_game_events()
        elif self.current_game_state == CurrentGameState.BATTLE:
            self.battle.update()
            self.battle.render()
            if self.battle.pokemon.health <= 0:
                self.current_game_state = CurrentGameState.MAP

    def determine_game_events(self):
        mapTile = self.map.map_array[self.player.position[1]][self.player.position[0]]
        print(mapTile)
        if mapTile == config.MAP_TILE_PATH:
            return
        self.determine_pokemon_found(mapTile)

    def determine_pokemon_found(self, mapTile):
        randomNumber = utilities.generate_random_number(1, 10)

        if randomNumber <= 1:
            foundPokemon = self.pokemon_factory.create_pokemon(mapTile)
            self.hitList.append(foundPokemon)
            print("A wild pokemon appeared!")
            print(f"Type: {foundPokemon.type}")
            print(f"Its stats are {foundPokemon.health}, {foundPokemon.attack}, {foundPokemon.defense}, {foundPokemon.specialAttack}, {foundPokemon.specialDefense}, {foundPokemon.speed}")

            self.battle = Battle(self.screen, foundPokemon, self.player)
            self.current_game_state = CurrentGameState.BATTLE

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GlobalGameState.ENDED
            # handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GlobalGameState.NONE
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.move_unit(self.player, [1, 0])
                elif event.key == pygame.K_f:
                    config.gameOrigin = random.randint(1,2)
                    config.gender = "f"
                    print("girl mode")
                elif event.key == pygame.K_m:
                    config.gameOrigin = random.randint(1,2)
                    config.gender = "m"
                    print("boy mode")
                elif event.key == pygame.K_SPACE:
                    print(f"You have slain {len(self.hitList)} Pokemon.\nThe last one was {self.hitList[:-1]}")

    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]
        if new_position[0] < 0 or new_position[0] > (len(self.map.map_array[0]) - 1):
            return
        if new_position[1] < 0 or new_position[1] > (len(self.map.map_array) - 1):
            return
        if self.map.map_array[new_position[1]][new_position[0]] == config.MAP_TILE_WATER:
            return
        self.playerHasMoved = True
        unit.update_position(new_position)

