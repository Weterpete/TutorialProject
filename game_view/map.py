import pygame
import config
import math
import utilities
class Map:
    def __init__(self, screen):
        self.screen = screen
        self.map_array = []
        self.camera = [0, 0]

    def load(self, file_name):
        with open(f"maps/{file_name}.txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map_array.append(tiles)
            print(self.map_array)

    def render(self, screen, player, objects):
        self.determineCamera(player)
        y_pos = 0
        for line in self.map_array:
            x_pos = 0
            for tile in line:
                image = mapTileImage[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1
            y_pos = y_pos + 1

        for object in objects:
            object.render(self.screen, self.camera)

    def determineCamera(self, player):
        max_y_position = len(self.map_array) - config.SCREEN_HEIGHT / config.SCALE
        y_position = player.position[1] - math.ceil(round(config.SCREEN_HEIGHT / config.SCALE / 2))

        if y_position <= max_y_position and y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position

mapTileImage = {
    config.MAP_TILE_GRASS: pygame.transform.scale(pygame.image.load("imgs/grass2.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_WATER: pygame.transform.scale(pygame.image.load("imgs/water.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_PATH: pygame.transform.scale(pygame.image.load("imgs/path.png"), (config.SCALE, config.SCALE))
}