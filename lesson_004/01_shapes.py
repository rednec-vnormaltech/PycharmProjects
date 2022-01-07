# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 1200)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:


# - треугольника
def triangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 120, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 240, length=length, width=3)
    v3.draw()


# triangle(point=point_0, angle=0, length=length_0)
# for angle_0 in range(0, 361, 60):
#     triangle(point=point_0, angle=angle_0, length=length_0)

# - квадрата
def forangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 90, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 180, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length, width=3)
    v4.draw()


# point_1 = sd.get_point(x=800, y=300)
# forangle(point=point_0, angle=45, length=length_0)

# - пятиугольника
def fiveangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 72, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 144, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 216, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 288, length=length, width=3)
    v5.draw()


# point_2 = sd.get_point(x=300, y=800)
# fiveangle(point=point_0, angle=0, length=length_0)

# - шестиугольника
def sixangle(point, angle, length):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length, width=3)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length, width=3)
    v3.draw()

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length, width=3)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length, width=3)
    v5.draw()

    v6 = sd.get_vector(start_point=v5.end_point, angle=angle + 300, length=length, width=3)
    v6.draw()


# point_3 = sd.get_point(x=800, y=800)
# sixangle(point=point_0, angle=0, length=length_0)

# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# length_0 = 200
# angle_0 = 45
#
# point_0 = sd.get_point(x=300, y=300)
# triangle(point=point_0, angle=angle_0, length=length_0)
#
# point_1 = sd.get_point(x=800, y=300)
# forangle(point=point_1, angle=angle_0, length=length_0)
#
# point_2 = sd.get_point(x=300, y=800)
# fiveangle(point=point_2, angle=angle_0, length=length_0)
#
# point_3 = sd.get_point(x=800, y=800)
# sixangle(point=point_3, angle=angle_0, length=length_0)

user_input = input("Введите число граней: ")
face_count = int(user_input)
print('Вы ввели', face_count)

def count_angle(start_point, zero_angle, side_length, count_sides):
    end_point = start_point
    angle_shift = int(360 / count_sides)
    for angle in range(0, 360 - angle_shift, angle_shift):
        v = sd.get_vector(start_point, angle + zero_angle, side_length)
        v.draw()
        start_point = v.end_point
    sd.line(start_point, end_point)


point = sd.get_point(400, 100)
count_angle(start_point=point, zero_angle=45, side_length=400, count_sides=face_count)



# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
