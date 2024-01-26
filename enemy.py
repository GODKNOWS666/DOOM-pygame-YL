from settings import *
from math import *
import pygame
from random import randint
from player import *


player = Player
class Enemy:
    def __init__(self, all_enemies):
        self.pos = [randint(100,500), randint(100,500)]
        self.speed = 2
        self.delta = 0
        self.dange_zone = 10
        self.zone_vison = 250
        self.HP = 2
        self.attack = 25
        self.enemy_index = len(all_enemies)
        
    def enemy_dead(self, all_enemies):
        all_enemies.pop(self.enemy_index)

    # Следует за игроком
    def following(self, player):
        x_pl, y_pl = player.x, player.y

        if self.pos[0] < x_pl - self.dange_zone and (self.pos[0] > x_pl - self.zone_vison):
            if self.pos[1] > y_pl - self.zone_vison and (self.pos[1] < y_pl + self.zone_vison):
                self.pos[0] += self.speed

        elif self.pos[0] > x_pl + self.dange_zone and (self.pos[0] < x_pl + self.zone_vison):
            if self.pos[1] > y_pl - self.zone_vison and (self.pos[1] < y_pl + self.zone_vison):
                self.pos[0] -= self.speed

        if self.pos[1] < y_pl - self.dange_zone and (self.pos[1] > y_pl - self.zone_vison):
            if self.pos[0] > x_pl - self.zone_vison and (self.pos[0] < x_pl + self.zone_vison):
                self.pos[1] += self.speed

        elif self.pos[1] > y_pl + self.dange_zone and (self.pos[1] < y_pl + self.zone_vison):
            if self.pos[0] > x_pl - self.zone_vison and (self.pos[0] < x_pl + self.zone_vison):
                self.pos[1] -= self.speed
        # Условие атаки
        if self.pos[0] >= x_pl - self.dange_zone\
            and self.pos[0] <= x_pl + self.dange_zone\
            or self.pos[1] >= y_pl - self.dange_zone\
            and self.pos[1] <=  y_pl == self.dange_zone :

            if self.attack % 25 == 0:
                player.HP -= 1
            self.attack += 1

    def enemy_event(self, screen, player, all_enemies):
        self.following(player)
        pygame.draw.circle(screen, (155, 0, 0), self.pos, 10)
        pygame.draw.line(screen, (155, 0, 0), self.pos, (player.x, player.y))
        
        if self.HP <= 0:
            self.enemy_dead(all_enemies)
