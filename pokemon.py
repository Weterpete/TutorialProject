import random

import pygame

import pokemon_stats
from pokemon_stats import Stats

class Pokemon:
  def __init__(self, pokemon_type, id):
    print("pokemon created")
    self.type = pokemon_type
    self.id = id
    self.image = pygame.image.load("imgs/pokemon/" + f"{self.id:03d}" + ".png")
    self.health = random.randint(50,150)
    self.totalHealth = self.health
    self.attack = random.randint(50,150)
    self.defense = random.randint(50,150)
    self.specialAttack = random.randint(50,150)
    self.specialDefense = random.randint(50,150)
    self.speed =  random.randint(50,150)