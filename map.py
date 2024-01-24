from settings import *
import pygame

text_map = [
    '1111111111111',
    '12.....1....1',
    '1....1...1..1',
    '1....1..11..1',
    '1..1....1...1',
    '1..1...11.2.1',
    '1....1......1',
    '1111111111111'
]

world_map = {}
mini_map = set()
collision_walls = []
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            collision_walls.append(pygame.Rect(i * TILE, j * TILE, TILE, TILE))
            if char == '1':
                world_map[(i * TILE, j * TILE)] = '1'
            elif char == '2':
                world_map[(i * TILE, j * TILE)] = '2'