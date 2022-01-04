# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    #sd.circle(point, radius, width=2)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def draw(point, step, ):
    """
    Функция принимает параметры:
    1)x,y для точки центра окружности
    2) r радиус окружности
    """
    radius =15
    for _ in range(70):
        radius += 10
        sd.circle(point, radius, width=2)





# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
def draw10(x, y, r):
    """
    Функция принимает параметры:
    1)x,y для точки центра окружности
    2) r радиус окружности

    Функция рисует 10 пузырьков в ряд
    """
    radius = r
    for _ in range(10):
        point = sd.get_point(x, y)
        x += 50
        sd.circle(point, radius, width=2)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
def draw10po3(x, y, r):
    """
    Функция принимает параметры:
    1)x,y для точки центра окружности
    2) r радиус окружности

    Функция рисует 10 пузырьков в 3 ряда
    """
    radius = r
    for _ in range(3):
        y += 30
        x= 30
        for _ in range(10):
            point = sd.get_point(x, y)
            x += 30
            sd.circle(point, radius, width=2)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

def draw100():
    """
        Функция рисует 100 пузырьков в случайных местах случайным цветом
        """

    for _ in range(10000):
        radius = random.randint(5,50)
        point = sd.random_point()
        z =sd.random_color()
        sd.circle(point, radius,color = z, width=1)


#draw10(100,50,20)
#draw10po3(50, 50, 20)
draw100()
#draw(point,5)

point = sd.get_point(300, 300)

sd.pause()
