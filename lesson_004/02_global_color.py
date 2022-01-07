# -*- coding: utf-8 -*-
import simple_draw as sd
import sys
#sd.resolution = (1200, 800)

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
print('Возможные цвета:')
menu_list = ['0 : red', '1 : orange', '2 : yellow', '3 : green', '4 : cyan', '5 : blue', '6 : purple', ]
color_list = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

print(*menu_list, sep="\n")
try:
    color_count = int(input("Введите номер цвета: "))
    print('Вы ввели', menu_list[color_count])
except:
    print("\033[31m {}".format('\nВведены некорректные данные'))
    sys.exit()


def count_angle(start_point, zero_angle, side_length, count_sides, count_colores):
    end_point = start_point
    angle_shift = int(360 / count_sides)
    for angle in range(0, 360 - angle_shift, angle_shift):
        v = sd.get_vector(start_point, angle + zero_angle, side_length)
        v.draw(color_list[count_colores])
        start_point = v.end_point
    sd.line(start_point, end_point, color_list[count_colores])


point = sd.get_point(100, 100)
count_angle(start_point=point, zero_angle=45, side_length=100, count_sides=3, count_colores=color_count)

point = sd.get_point(400, 100)
count_angle(start_point=point, zero_angle=45, side_length=100, count_sides=4, count_colores=color_count)

point = sd.get_point(100, 300)
count_angle(start_point=point, zero_angle=45, side_length=100, count_sides=5, count_colores=color_count)

point = sd.get_point(400, 300)
count_angle(start_point=point, zero_angle=45, side_length=100, count_sides=6, count_colores=color_count)

# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код

sd.pause()
