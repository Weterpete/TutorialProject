import pygame
import config
from game_state import GlobalGameState

from game import Game
from menu import Menu

pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

pygame.display.set_caption("POKEMON CLONE")

clock = pygame.time.Clock()

game = Game(screen)

menu = Menu(screen, game)
menu.set_up()

while game.game_state != GlobalGameState.ENDED:
  clock.tick(50)
  if game.game_state == GlobalGameState.NONE:
    menu.update()
  if game.game_state == GlobalGameState.RUNNING:
    game.update()
  pygame.display.flip()
