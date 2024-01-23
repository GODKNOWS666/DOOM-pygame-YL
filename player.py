from settings import *
import pygame
import math
from map import collision_walls


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle
        self.delta_time = delta_time()
        self.side = 20
        self.rect = pygame.Rect(*player_pos, self.side, self.side)

    @property
    def pos(self):
        return (self.x, self.y)

    def detect_collision(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(collision_walls)
        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = collision_walls[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top
            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        self.rect.center = self.x, self.y
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            exit()
        if keys[pygame.K_w]:
            dx = player_speed * cos_a * self.delta_time
            dy = player_speed * sin_a * self.delta_time
            self.detect_collision(dx, dy)
        if keys[pygame.K_s]:
            dx = -player_speed * cos_a * self.delta_time
            dy = -player_speed * sin_a * self.delta_time
            self.detect_collision(dx, dy)
        if keys[pygame.K_a]:
            dx = player_speed * sin_a * self.delta_time
            dy = -player_speed * cos_a * self.delta_time
            self.detect_collision(dx, dy)
        if keys[pygame.K_d]:
            dx = -player_speed * sin_a * self.delta_time
            dy = player_speed * cos_a * self.delta_time
            self.detect_collision(dx, dy)
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02 * self.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02 * self.delta_time