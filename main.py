
import pygame
from settings import *
from player import Player
import math
from map import world_map
from drawing import Draw

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Draw(sc, sc_map)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    drawing.back()
    drawing.walls(player.pos, player.angle)
    drawing.fps(clock)
    # drawing.mini_map(player)

    pygame.display.flip()
    clock.tick()