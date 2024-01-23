import pygame
from settings import *
import time
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Измените путь к файлам, у меня по другому не работает!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Gun:
    def __init__(self):
        self.i = 0
        # Загрузка спрайтов
        self.gun_animation = [pygame.image.load(f"Sk/Картинки/gun/gun_{i}.png") for i in range(1,5)]
        for i in range(3, 0, -1):
            self.gun_animation.append(pygame.image.load(f"Sk/Картинки/gun/gun_{i}.png"))
        self.fire_animation = list()
        self.fire_animation.append(pygame.image.load(f"Sk/Картинки/gun/fire_1.png"))
        self.fire_animation.append(pygame.image.load(f"Sk/Картинки/gun/fire_2.png"))
        self.fire_animation.append(pygame.image.load(f"Sk/Картинки/gun/fire_1.png"))

        self.ivanface = pygame.image.load(f"Sk/Картинки/ivanface.png")

    def shot(self, screen, draw, player, clock):
        clock.tick(25)
        # Анимация огня выстрела
        if self.i < 3:
            screen.blit(self.fire_animation[self.i], (WIDTH // 3 + 50, HEIGHT // 3))
            screen.blit(self.gun_animation[0], (WIDTH // 4, HEIGHT // 3))
        # Анимация ствола выстрела
        if self.i >= 3:
            self.i -= 3
            screen.fill(BLACK)
            draw.background(player.angle)
            draw.world(player.pos, player.angle)
            draw.mini_map(player)
            screen.blit(self.gun_animation[self.i], (WIDTH // 4, HEIGHT // 2.5))
            self.i += 3
        self.i += 1




