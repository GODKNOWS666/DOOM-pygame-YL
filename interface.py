import pygame
from settings import *
class Interface:
    def __init__(self):
        self.Interface = pygame.image.load("Sk/Картинки/ivanface.png")
    
    def draw_interface(self, screen):
        screen.blit(self.Interface, (0, 80))

    def draw_HP(self, screen, HP):
        font = pygame.font.Font(None, 100)
        text = font.render(f"{(HP * 100) // MAX_XP}", True, (255, 10, 10))
        screen.blit(text, (240, 685))

