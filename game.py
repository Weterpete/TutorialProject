import pygame

import config
from player import Player
from game_state import GameState

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.object = []
        self.game_state = GameState.NONE
        self.map = []

    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.object.append(player)
        print("Do set up")
        self.game_state = GameState.RUNNING

        self.loadMap("01")

    def update(self):
        self.screen.fill(config.BLACK)
        print("Update")
        self.handleEvents()

        self.renderMap(self.screen)

        for object in self.object:
            object.render(self.screen)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            # handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_UP:
                    self.player.update_position(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.player.update_position(0, 1)
                elif event.key == pygame.K_LEFT:
                    self.player.update_position(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.update_position(1, 0)
                elif event.key == pygame.K_f:
                    config.gender = "f"
                    print("girl mode")
                elif event.key == pygame.K_m:
                    config.gender = "m"
                    print("boy mode")

    def loadMap(self, file_name):
        with open("maps/" + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)
            print(self.map)

    def renderMap(self, screen):
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = mapTileImage[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE, config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1
            y_pos = y_pos + 1

mapTileImage = {
    "G" : pygame.transform.scale(pygame.image.load("imgs/grass1.png"), (config.SCALE, config.SCALE)),
    "W": pygame.transform.scale(pygame.image.load("imgs/water.png"), (config.SCALE, config.SCALE))
}