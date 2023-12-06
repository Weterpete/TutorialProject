import pygame
import config
import math
from player import Player
from game_state import GameState

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.object = []
        self.game_state = GameState.NONE
        self.map = []
        self.camera = [0, 0]
        self.playerHasMoved = False

    def set_up(self):
        player = Player(1, 26)
        self.player = player
        self.object.append(player)
        print("Do set up")
        self.game_state = GameState.RUNNING

        self.loadMap("01")

    def update(self):
        self.playerHasMoved = False
        self.screen.fill(config.BLACK)
        # print("Update")
        self.handleEvents()

        self.renderMap(self.screen)

        for object in self.object:
            object.render(self.screen, self.camera)
        if self.playerHasMoved:
            self.determine_game_events()

    def determine_game_events(self):
        mapTile = self.map[self.player.position[1]][self.player.position[0]]
        print(mapTile)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            # handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.move_unit(self.player, [0, -1])
                    # old = self.player.update_position(0, -1)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.move_unit(self.player, [0, 1])
                    # old = self.player.update_position(0, 1)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.move_unit(self.player, [-1, 0])
                    # old = self.player.update_position(-1, 0)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.move_unit(self.player, [1, 0])
                    # old = self.player.update_position(1, 0)
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
        self.determineCamera()
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = mapTileImage[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE - (self.camera[1] * config.SCALE), config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1
            y_pos = y_pos + 1

    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]
        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 1):
            return
        if new_position[1] < 0 or new_position[1] > (len(self.map) - 1):
            return
        if self.map[new_position[1]][new_position[0]] == "W":
            return
        self.playerHasMoved = True
        unit.update_position(new_position)

    def determineCamera(self):
        max_y_position = len(self.map) - config.SCREEN_HEIGHT / config.SCALE
        y_position = self.player.position[1] - math.ceil(round(config.SCREEN_HEIGHT / config.SCALE / 2))

        if y_position <= max_y_position and y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position


mapTileImage = {
    "G" : pygame.transform.scale(pygame.image.load("imgs/grass2.png"), (config.SCALE, config.SCALE)),
    "W": pygame.transform.scale(pygame.image.load("imgs/water.png"), (config.SCALE, config.SCALE))
}