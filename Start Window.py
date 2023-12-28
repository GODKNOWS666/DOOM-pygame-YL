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
        self.menu_background = pygame.image.load('Картинки/картинка меню.png')
        screen.fill((0, 0, 0))
        screen.blit(self.menu_background, (0, 0))

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


    def settings(self):
        # Главное окно
        self.settings_window = pygame.image.load('Картинки/окно настроек.png')
        self.settings_window = pygame.transform.scale(self.settings_window, (1280, 720))
        self.settings_window_rect = self.settings_window.get_rect(topleft=(0, 30))
        screen.blit(self.settings_window, self.settings_window_rect)

        # Кнопка "сложно" для изменения режима игры
        self.mode_hard = pygame.image.load('Картинки/сложно.png')
        self.mode_hard = pygame.transform.scale(self.mode_hard, (337, 61))
        self.mode_hard_rect = self.settings_window.get_rect(topleft=(727, 210))
        screen.blit(self.mode_hard, self.mode_hard_rect)

        # Кнопка "легко" для изменения режима игры
        self.mode_easy = pygame.image.load('Картинки/легко.png')
        self.mode_easy = pygame.transform.scale(self.mode_easy, (337, 61))
        self.mode_easy_rect = self.settings_window.get_rect(topleft=(727, 210))
        screen.blit(self.mode_easy, self.mode_easy_rect)

        # Квадрат без галочки
        self.no_check_mark = pygame.image.load('Картинки/квадрат без галочки.png')
        self.no_check_mark = pygame.transform.scale(self.no_check_mark, (114, 104))
        self.no_check_mark_rect = self.settings_window.get_rect(topleft=(570, 425))
        screen.blit(self.no_check_mark, self.no_check_mark_rect)

        # Квадрат с галочкой
        self.check_mark = pygame.image.load('Картинки/квадрат с галочкой.png')
        self.check_mark = pygame.transform.scale(self.check_mark, (114, 104))
        self.check_mark_rect = self.settings_window.get_rect(topleft=(570, 425))
        screen.blit(self.check_mark, self.check_mark_rect)

        # кнопка выхода из настроек
        self.exit_settings = pygame.image.load('Картинки/Кнопка выхода из настроек.png')
        self.exit_settings = pygame.transform.scale(self.exit_settings, (115, 115))
        self.exit_settings_rect = self.settings_window.get_rect(topleft=(1055, 105))
        screen.blit(self.exit_settings, self.exit_settings_rect)

    # функция для выхода из игры
    def exit_game(self):
        pygame.quit()
        sys.exit()


# класс начала игры
class StartGame:
    def __init__(self):
        pass


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    start_window = StartWindow()
    pygame.display.flip()
    # переменные для проверки чего-либо
    # переменная для проверки на то, выведено ли окно настроек на экран
    setting_true = True
    # переменная для проверки галочки
    checkmark_check = False
    # переменная для проверки на сложность режима
    easy_or_hard = 0

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            # если окно настроек не выведено
            if setting_true:
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
                    start_window.settings()
                    setting_true = False

                # изменить кнопку на ховер версию, если наводимся мышкой на кнопку "выход"
                elif event.type == pygame.MOUSEMOTION and start_window.exit_button_rect.collidepoint(event.pos):
                    screen.blit(start_window.hover_exit_button, start_window.hover_exit_button_rect)

                # издать звук и выйти из игры, если кликаем по кнопке "выход"
                elif event.type == pygame.MOUSEBUTTONDOWN and start_window.exit_button_rect.collidepoint(event.pos):
                    start_window.buttonclick_sound.play()
                    time.sleep(1.2)
                    start_window.exit_game()

                # если никакого действия нет, то вернуть все в исходное положение
                else:
                    screen.blit(start_window.menu_background, (0, 0))
                    screen.blit(start_window.start_button, start_window.start_button_rect)
                    screen.blit(start_window.settings_button, start_window.settings_button_rect)
                    screen.blit(start_window.exit_button, start_window.exit_button_rect)

            # если окно настроек выведено
            else:
                if event.type == pygame.QUIT:
                    running = False

                # если стоит сложный режим, то выводим картинку со сложным режимом
                elif event.type == pygame.MOUSEBUTTONDOWN and start_window.mode_easy_rect.collidepoint(event.pos) and easy_or_hard == 0:
                    start_window.buttonclick_sound.play()
                    screen.blit(start_window.mode_hard, start_window.mode_hard_rect)
                    easy_or_hard += 1

                # если стоит легкий режим, то выводим картинку с легким режимом
                elif event.type == pygame.MOUSEBUTTONDOWN and start_window.mode_hard_rect.collidepoint(event.pos) and easy_or_hard == 1:
                    start_window.buttonclick_sound.play()
                    screen.blit(start_window.mode_easy, start_window.mode_easy_rect)
                    easy_or_hard -= 1

                # если checkmark_check == True, то выводим картинки с галочкой
                elif event.type == pygame.MOUSEBUTTONDOWN and start_window.check_mark_rect.collidepoint(event.pos) and checkmark_check:
                    pygame.mixer.music.set_volume(1)
                    start_window.buttonclick_sound.set_volume(1)
                    start_window.buttonclick_sound.play()
                    screen.blit(start_window.check_mark, start_window.check_mark_rect)
                    checkmark_check = False

                # если checkmark_check == False, то выводим картинку без галочки
                elif event.type == pygame.MOUSEBUTTONDOWN and start_window.no_check_mark_rect.collidepoint(event.pos) and not checkmark_check:
                    pygame.mixer.music.set_volume(0)
                    start_window.buttonclick_sound.set_volume(0)
                    start_window.buttonclick_sound.play()
                    screen.blit(start_window.no_check_mark, start_window.no_check_mark_rect)
                    checkmark_check = True

                elif event.type == pygame.MOUSEBUTTONDOWN and start_window.exit_settings_rect.collidepoint(event.pos):
                    start_window.buttonclick_sound.play()
                    setting_true = True

        pygame.display.flip()



