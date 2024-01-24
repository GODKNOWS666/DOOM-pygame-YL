import pygame
from settings import *
from player import Player
import math
from map import world_map
from drawing import Drawing
from gun import Gun
from enemy import Enemy
from interface import Interface
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
drawing = Drawing(screen, sc_map)
# Список врагов
enemies = list()
enemies.append([Enemy()])
gun = Gun()
interface = Interface()
while True:
    if gun.i >= 7:
        gun.i = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gun.shot(screen, drawing, player, clock)
            if event.key == pygame.K_g:
                player.HP -= 1
                print(player.HP)
    player.movement()
    screen.fill(BLACK)

    drawing.background(player.angle)
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)            
    # Анимация оружия    
    screen.blit(gun.gun_animation[0], (WIDTH // 4, HEIGHT // 2.5))
    if gun.i != 0:
        gun.shot(screen, drawing, player, clock)
    # Отрисовка интерфейса
    interface.draw_interface(screen)
    interface.draw_HP(screen, player.HP)
    drawing.mini_map(player)
    # КОНЕЦ ИГРЫ
    if player.HP <= 0:
        pass
#действия врагов{
                
    enemies[0][0].following(player)
    pygame.draw.circle(screen, (155, 0, 0), enemies[0][0].pos, 10)
    pygame.draw.line(screen, (155, 0, 0), enemies[0][0].pos, (player.x, player.y))

#}  


    pygame.display.flip()
    clock.tick(18)