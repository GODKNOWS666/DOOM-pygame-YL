from settings import *
from math import *
import pygame
from random import randint
from player import *


player = Player
class Enemy:
    def __init__(self):
        self.pos = [randint(100,500), randint(100,500)]
        self.speed = 1000
        self.delta = 0
        self.zone = 20
        self.zone_vison = 250
        self.HP = 2

    def enemy_dead(self):
        pass
    
    def danger_zone(self, player):
        player.HP -= 1

    def following(self, player):
        x_pl, y_pl = player.x, player.y

        if self.pos[0] < x_pl - self.zone and (self.pos[0] > x_pl - self.zone_vison):
            if self.pos[1] > y_pl - self.zone_vison and (self.pos[1] < y_pl + self.zone_vison):
                self.pos[0] += enemy_speed

        elif self.pos[0] > x_pl + self.zone and (self.pos[0] < x_pl + self.zone_vison):
            if self.pos[1] > y_pl - self.zone_vison and (self.pos[1] < y_pl + self.zone_vison):
                self.pos[0] -= enemy_speed

        if self.pos[1] < y_pl - self.zone and (self.pos[1] > y_pl - self.zone_vison):
            if self.pos[0] > x_pl - self.zone_vison and (self.pos[0] < x_pl + self.zone_vison):
                self.pos[1] += enemy_speed

        elif self.pos[1] > y_pl + self.zone and (self.pos[1] < y_pl + self.zone_vison):
            if self.pos[0] > x_pl - self.zone_vison and (self.pos[0] < x_pl + self.zone_vison):
                self.pos[1] -= enemy_speed
