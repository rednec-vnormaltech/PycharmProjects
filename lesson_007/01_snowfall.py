# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self, centr, length, color, factor_a, factor_b, factor_c):
        self.centr = centr
        self.length = length
        self.color = color
        self.factor_a = factor_a
        self.factor_b = factor_b
        self.factor_c = factor_c

    def clear_previous_picture(self):
        sd.clear_screen()

    def move(self):
        pass

    def draw(self, centr):
        sd.snowflake(centr, self.length, self.color, self.factor_a, self.factor_b, self.factor_c)


x, y = 100, 600
x1, y1 = 200, 550

flake = Snowflake(sd.get_point(x, y), 30, sd.COLOR_DARK_YELLOW, 0.6, 0.35, 15)
flake1 = Snowflake(sd.get_point(x1, y1), 30, sd.COLOR_DARK_YELLOW, 0.6, 0.35, 15)

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw(sd.get_point(x, y))
    x += 2
    y -= 10
    if x > 600:
        x = 100
    if y < 10:
        y = 10
        x -= 2

    flake1.draw(sd.get_point(x1, y1))
    x1 += 2
    y1 -= 10
    if x1 > 600:
        x1 = 100
    if y1 < 10:
        y1 = 600


    sd.sleep(0.05)


    # if not flake.can_fall():
    #     break
    # sd.sleep(0.1)
    # if sd.user_want_exit():
    #     break
# sd.pause()



# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
