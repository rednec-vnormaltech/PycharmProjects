import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
screen_width = 800
screen_height = 600

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))

# Определение символов, которые будут использоваться для отображения эффекта матрицы
symbols = ["1", "2", "3", "4", "5", "6"]

# Создание списка для хранения падающих символов
falling_symbols = []

# Задание цвета фона и цвета символов
bg_color = (0, 0, 0)
symbol_color = (0, 255, 0)

# Цикл для отображения падающих символов
while True:
    # Создание нового символа со случайным значением и случайными координатами
    new_symbol = {
        "symbol": random.choice(symbols),
        "x": random.randint(0, screen_width),
        "y": 0,
        "speed": random.randint(5, 15)
    }

    # Добавление нового символа в список падающих символов
    falling_symbols.append(new_symbol)

    # Очистка экрана и установка цвета фона
    screen.fill(bg_color)

    # Отображение падающих символов на экране
    for symbol in falling_symbols:
        # Создание текстовой поверхности для символа
        symbol_surface = pygame.font.SysFont("Consolas", 20).render(symbol["symbol"], True, symbol_color)
        # Отображение символа на экране
        screen.blit(symbol_surface, (symbol["x"], symbol["y"]))
        # Изменение координат символа для следующего кадра
        symbol["y"] += symbol["speed"]
        # Удаление символа из списка, если он ушел за границы экрана
        if symbol["y"] > screen_height:
            falling_symbols.remove(symbol)

    # Обновление экрана
    pygame.display.update()

    # Задержка между отображениями символов
    time.sleep(0.02)

    # Обработка событий Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
