import pygame
from settings import *
from player import Player
import math
from map import world_map
from drawing import Drawing
from gun import Gun

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen, sc_map)

gun = Gun()

while True:
    if gun.i >= 7:
        gun.i = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gun.shot(screen, drawing, player, clock)


    player.movement()
    screen.fill(BLACK)

    drawing.background(player.angle)
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    drawing.mini_map(player)
                
    screen.blit(gun.gun_animation[0], (WIDTH // 4, HEIGHT // 2.5))
    if gun.i != 0:
        gun.shot(screen, drawing, player, clock)



    pygame.display.flip()
    clock.tick(18)