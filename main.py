import sys
import time
import pygame

#создаем поле
pygame.init()
size = width, height = 1280, 720
screen = pygame.display.set_mode(size)


# главное меню
class StartWindow:
    def __init__(self):
        # все картинки для главного меню
        # бэкграунд
        menu_background = pygame.image.load('Картинки/картинка меню.png')
        screen.fill((0, 0, 0))
        screen.blit(menu_background, (0, 0))

        # Кнопка "играть"
        self.start_button = pygame.image.load('Картинки/играть.png')
        self.start_button = pygame.transform.scale(self.start_button, (678, 95))
        self.start_button_rect = self.start_button.get_rect(topleft=(302, 250))
        screen.blit(self.start_button, self.start_button_rect)

        # Кнопка "настройки"
        self.settings_button = pygame.image.load('Картинки/настройки.png')
        self.settings_button = pygame.transform.scale(self.settings_button, (678, 95))
        self.settings_button_rect = self.settings_button.get_rect(topleft=(302, 400))
        screen.blit(self.settings_button, self.settings_button_rect)

        # Кнопка "выход"
        self.exit_button = pygame.image.load('Картинки/выход.png')
        self.exit_button = pygame.transform.scale(self.exit_button, (678, 95))
        self.exit_button_rect = self.exit_button.get_rect(topleft=(302, 550))
        screen.blit(self.exit_button, self.exit_button_rect)

        # Ховер кнопка "Играть"
        self.hover_start_button = pygame.image.load('Картинки/играть реверс.png')
        self.hover_start_button = pygame.transform.scale(self.hover_start_button, (678, 95))
        self.hover_start_button_rect = self.hover_start_button.get_rect(topleft=(302, 250))

        # Ховер кнопка "Настройки"
        self.hover_settings_button = pygame.image.load('Картинки/настройки реверс.png')
        self.hover_settings_button = pygame.transform.scale(self.hover_settings_button, (678, 95))
        self.hover_settings_button_rect = self.hover_settings_button.get_rect(topleft=(302, 400))

        # Ховер кнопка "Выход"
        self.hover_exit_button = pygame.image.load('Картинки/выход реверс.png')
        self.hover_exit_button = pygame.transform.scale(self.hover_exit_button, (678, 95))
        self.hover_exit_button_rect = self.hover_exit_button.get_rect(topleft=(302, 550))

        # музыка и звуки в менюшке
        # главная тема
        pygame.mixer.music.load("Звуки/Main Theme.mp3")
        pygame.mixer.music.play(-1)

        # звук при нажатии кнопки
        self.buttonclick_sound = pygame.mixer.Sound("Звуки/click button.mp3")


# класс начала игры
class StartGame:
    def __init__(self):
        pass


# Окно настроек
class SettingsGame(StartWindow):
    # я ваще хз как сделать так чтобы она была выше всех, разберемся
    def settings(self):
        # Главное окно
        self.settings_window = pygame.image.load('Картинки/окно настроек.png')
        self.settings_window = pygame.transform.scale(self.settings_window, (1280, 720))
        self.settings_window_rect = self.settings_window.get_rect(topleft=(0, 30))
        screen.blit(self.settings_window, self.settings_window_rect)

        # Кнопка "легко" для изменения режима игры
        self.mode = pygame.image.load('Картинки/легко.png')
        self.mode = pygame.transform.scale(self.mode, (319, 72))
        self.mode_rect = self.settings_window.get_rect(topleft=(750, 210))
        screen.blit(self.mode, self.mode_rect)

        # Квадрат на котором будет расположена галочка
        self.kvadrat = pygame.image.load('Картинки/квадрат для галочки.png')
        self.kvadrat = pygame.transform.scale(self.kvadrat, (114, 104))
        self.kvadrat_rect = self.settings_window.get_rect(topleft=(570, 420))
        screen.blit(self.kvadrat, self.kvadrat_rect)

        # Галочка для вкл/выкл звука
        self.check_mark = pygame.image.load('Картинки/зеленая галочка.png')
        self.check_mark = pygame.transform.scale(self.check_mark, (159, 125))
        self.check_mark_rect = self.settings_window.get_rect(topleft=(570, 400))
        screen.blit(self.check_mark, self.check_mark_rect)


# функция для выхода из игры
def exit_game():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    pygame.init()
    settings_window = SettingsGame()
    start_window = StartWindow()
    pygame.display.flip()
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            # изменить кнопку на ховер версию, если наводимся мышкой на кнопку "играть"
            elif event.type == pygame.MOUSEMOTION and start_window.start_button_rect.collidepoint(event.pos):
                screen.blit(start_window.hover_start_button, start_window.hover_start_button_rect)
            # издать звук и начать игру, если кликаем по кнопке "играть"
            elif event.type == pygame.MOUSEBUTTONDOWN and start_window.start_button_rect.collidepoint(event.pos):
                start_window.buttonclick_sound.play()
                StartGame()

            # изменить кнопку на ховер версию, если наводимся мышкой на кнопку "настройки"
            elif event.type == pygame.MOUSEMOTION and start_window.settings_button_rect.collidepoint(event.pos):
                screen.blit(start_window.hover_settings_button, start_window.hover_settings_button_rect)
            # издать звук и открыть окно с настройками, если кликаем по кнопке "настройки"
            elif event.type == pygame.MOUSEBUTTONDOWN and start_window.settings_button_rect.collidepoint(event.pos):
                start_window.buttonclick_sound.play()
                SettingsGame.settings(self=SettingsGame)

            # изменить кнопку на ховер версию, если наводимся мышкой на кнопку "выход"
            elif event.type == pygame.MOUSEMOTION and start_window.exit_button_rect.collidepoint(event.pos):
                screen.blit(start_window.hover_exit_button, start_window.hover_exit_button_rect)
            # издать звук и выйти из игры, если кликаем по кнопке "выход"
            elif event.type == pygame.MOUSEBUTTONDOWN and start_window.exit_button_rect.collidepoint(event.pos):
                start_window.buttonclick_sound.play()
                time.sleep(1.2)
                exit_game()

            # если никакого действия нет, то вернуть все в исходное положение
            else:
                screen.blit(start_window.start_button, start_window.start_button_rect)
                screen.blit(start_window.settings_button, start_window.settings_button_rect)
                screen.blit(start_window.exit_button, start_window.exit_button_rect)

        pygame.display.flip()



