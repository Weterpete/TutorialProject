import random

import pygame
import config
import math
import utilities
from game_state import GlobalGameState

class Battle:
    def __init__(self, screen, pokemon, player):
        self.screen = screen
        self.pokemon = pokemon
        self.player = player

    def load(self, file_name):
        pass

    def render(self):
        self.screen.fill(config.WHITE)

        rect = pygame.Rect(1, 1, 2, 2)
        self.screen.blit(self.pokemon.image, rect)

        self.screen.blit(self.player.image, (320, 40))

        font = pygame.font.SysFont(None, 24)
        img = font.render(f"Health: {self.pokemon.health}/{self.pokemon.totalHealth}", True, config.BLACK)
        self.screen.blit(img, (20, 120))
        img = font.render(f"Attack: {self.pokemon.attack}", True, config.BLACK)
        self.screen.blit(img, (20, 140))
        img = font.render(f"Defense: {self.pokemon.defense}", True, config.BLACK)
        self.screen.blit(img, (20, 160))
        img = font.render(f"Special Attack: {self.pokemon.specialAttack}", True, config.BLACK)
        self.screen.blit(img, (20, 180))
        img = font.render(f"Special Defense: {self.pokemon.specialDefense}", True, config.BLACK)
        self.screen.blit(img, (20, 200))
        img = font.render(f"Speed: {self.pokemon.speed}", True, config.BLACK)
        self.screen.blit(img, (20, 220))

        img = font.render("Press enter to attack!", True, config.BLACK)
        self.screen.blit(img, (20, 260))


        pass

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GlobalGameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GlobalGameState.ENDED
                if event.key == pygame.K_RETURN:
                    self.pokemon.health = self.pokemon.health - random.randint(1,16)
