# -*- coding: utf-8 -*-

import random as r
import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку
sd.resolution = (600, 600)


class Snowflake:

    def __init__(self, ):
        self.point = sd.get_point(r.randint(100, 300), r.randint(450, 600))
        self.length = r.randint(5, 30)
        self.color = sd.COLOR_DARK_YELLOW
        self.factor_a = 0.6
        self.factor_b = 0.35
        self.factor_c = r.randint(5, 90)

    def create_snowfally(self):
        sd.snowflake(self.point, self.length, self.color, self.factor_a, self.factor_b, self.factor_c)

    def clear_previous_picture(self):
        sd.clear_screen()

    def move(self):
        flake.clear_previous_picture()
        flake.draw(self.point)
        self.point.x += 2
        self.point.y -= 10
        if self.point.x > 600:
            self.point.x = 100
        if self.point.y < 10:
            self.point.y = r.randint(450, 600)
            flake.factor_c = r.randrange(5, 45, 5)
            flake.length = r.randrange(5, 45, 5)

    def draw(self, point):
        sd.snowflake(point, self.length, self.color, self.factor_a, self.factor_b, self.factor_c)







while True:
    flake = Snowflake()

    # flake.clear_previous_picture()


    flake.move()






    sd.sleep(0.5)

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
