
import PIL.ImageDraw
import pygame
import PIL



player = pygame.image.load("assets\\player.png")
enemy = pygame.image.load("assets\\enemies.png")
projectile_enemy = pygame.image.load("assets\\projectile.png")
projectile_player = pygame.image.load("assets\\projectile-p.png")
background = pygame.image.load(PIL.Image.new("RGB", (800, 600), (255, 255, 255)))



class Player():
    def __init__(self):
        pass


class Enemy():
    def __init__(self):
        pass

class Projectile():
    def __init__(self):
        pass

class Game():
    player = Player()
    enemies = list[Enemy]
    projectiles = list[Projectile]
    def __init__(self):
        pass
    
    def update(self):
        pass