# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x, y, color):
    sd.circle(sd.get_point(x, y), radius=40, color=color, width=1)
    sd.line(sd.get_point(x, y-10), sd.get_point(x, y+10), color=color, width=1)
    sd.line(sd.get_point(x-15, y - 20), sd.get_point(x+15, y -20), color=color, width=1)
    sd.line(sd.get_point(x - 15, y - 20), sd.get_point(x - 20, y - 10), color=color, width=1)
    sd.line(sd.get_point(x + 15, y - 20), sd.get_point(x + 20, y - 10), color=color, width=1)
    sd.circle(sd.get_point(x-17, y+10), radius=5, color=color, width=1)
    sd.circle(sd.get_point(x + 17, y + 10), radius=5, color=color, width=1)


for _ in range(10):
    smile(sd.random_point().x, sd.random_point().y, sd.COLOR_DARK_CYAN)
sd.pause()
