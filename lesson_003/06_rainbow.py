# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
sd.resolution = (1200, 600)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код

x1, x2 = 350, 650
y1, y2 = 50, 250

for x in rainbow_colors:
    line1 = sd.line(sd.get_point(x1, y1), sd.get_point(x2, y2), x, width=100)
    x1 += 20
    x2 += 20
    # y1+=50
    # y2+=50

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
x = 600
y = -390
r = 800

for clr in rainbow_colors:
    line1 = sd.circle(sd.get_point(x, y), radius= r,color=clr, width=30)
    r+=30


sd.pause()
