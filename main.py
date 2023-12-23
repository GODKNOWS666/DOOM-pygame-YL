import sys
import time
import pygame

pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)


class StartWindow:
    def __init__(self):
        menu_background = pygame.image.load('картинка меню.png')
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        self.start_button = pygame.image.load('играть.png')
        self.start_button = pygame.transform.scale(self.start_button, (678, 95))
        self.start_button_rect = self.start_button.get_rect(topleft=(302, 250))
        screen.blit(self.start_button, self.start_button_rect)

        self.settings_button = pygame.image.load('настройки.png')
        self.settings_button = pygame.transform.scale(self.settings_button, (678, 95))
        self.settings_button_rect = self.settings_button.get_rect(topleft=(302, 400))
        screen.blit(self.settings_button, self.settings_button_rect)

        self.exit_button = pygame.image.load('выход.png')
        self.exit_button = pygame.transform.scale(self.exit_button, (678, 95))
        self.exit_button_rect = self.exit_button.get_rect(topleft=(302, 550))
        screen.blit(self.exit_button, self.exit_button_rect)

        self.hover_start_button = pygame.image.load('играть реверс.png')
        self.hover_start_button = pygame.transform.scale(self.hover_start_button, (678, 95))
        self.hover_start_button_rect = self.hover_start_button.get_rect(topleft=(302, 250))

        self.hover_settings_button = pygame.image.load('настройки реверс.png')
        self.hover_settings_button = pygame.transform.scale(self.hover_settings_button, (678, 95))
        self.hover_settings_button_rect = self.hover_settings_button.get_rect(topleft=(302, 400))

        self.hover_exit_button = pygame.image.load('выход реверс.png')
        self.hover_exit_button = pygame.transform.scale(self.hover_exit_button, (678, 95))
        self.hover_exit_button_rect = self.hover_exit_button.get_rect(topleft=(302, 550))

        # музыка и звуки в менюшке
        pygame.mixer.music.load("Main Theme.mp3")
        pygame.mixer.music.play(-1)

        self.buttonclick_sound = pygame.mixer.Sound("buttondown_sound.mp3")

class StartGame:
    def __init__(self):
        pass


class SettingsGame(StartWindow):
    pass


def exit_game():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()
    start_window = StartWindow()
    pygame.display.flip()
    running = True

    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEMOTION and start_window.start_button_rect.collidepoint(event.pos):
                screen.blit(start_window.hover_start_button, start_window.hover_start_button_rect)
            elif event.type == pygame.MOUSEBUTTONDOWN and start_window.start_button_rect.collidepoint(event.pos):
                start_window.buttonclick_sound.play()
                StartGame()

            elif event.type == pygame.MOUSEMOTION and start_window.settings_button_rect.collidepoint(event.pos):
                screen.blit(start_window.hover_settings_button, start_window.hover_settings_button_rect)
            elif event.type == pygame.MOUSEBUTTONDOWN and start_window.settings_button_rect.collidepoint(event.pos):
                start_window.buttonclick_sound.play()
                SettingsGame()

            elif event.type == pygame.MOUSEMOTION and start_window.exit_button_rect.collidepoint(event.pos):
                screen.blit(start_window.hover_exit_button, start_window.hover_exit_button_rect)
            elif event.type == pygame.MOUSEBUTTONDOWN and start_window.exit_button_rect.collidepoint(event.pos):
                start_window.buttonclick_sound.play()
                time.sleep(1.2)
                exit_game()

            else:
                screen.blit(start_window.start_button, start_window.start_button_rect)
                screen.blit(start_window.settings_button, start_window.settings_button_rect)
                screen.blit(start_window.exit_button, start_window.exit_button_rect)

        pygame.display.flip()



