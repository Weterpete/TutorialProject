import pygame
import config
import math
import random
import utilities
from player import Player
from game_state import GlobalGameState

class Menu:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def set_up(self):
        self.menu_image = pygame.image.load("imgs/menu.png")
        pass

    def update(self):
        self.screen.fill(config.BLACK)
        rect = pygame.Rect(1, 1, 2, 2)
        self.screen.blit(self.menu_image, rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GlobalGameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GlobalGameState.ENDED
                elif event.key == pygame.K_RETURN:  # up
                    self.game.set_up()
                    self.game.game_state = GlobalGameState.RUNNING