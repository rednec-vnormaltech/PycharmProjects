# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

menu_figure = ['\t1: точка', '\t2: прямая', '\t3: треугольник', '\t4: квадрат', '\t5: пентагон', '\t6: гексагон', ]
print('Возможные фигуры:')
print(*menu_figure, sep="\n")

user_count = int(input("Выберите фигуру из стандарного списка или Введите число граней: "))
print('Вы ввели', menu_figure[user_count - 1])

clrlst = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
print('\nВозможные цвета:')
menu_list = ['\t0: red', '\t: orange', '\t2: yellow', '\t3: green', '\t4: cyan', '\t5: blue', '\t6: purple', ]

print(*menu_list, sep="\n")
user_input_color_count = int(input("Введите номер цвета: "))
print('Вы ввели', menu_list[user_input_color_count])


def count_angle(start_point, zero_angle, side_length, count_sides, count_colores):
    end_point = start_point
    angle_shift = int(360 / count_sides)
    for angle in range(0, 360 - angle_shift, angle_shift):
        v = sd.get_vector(start_point, angle + zero_angle, side_length)
        v.draw(clrlst[count_colores])
        start_point = v.end_point
    sd.line(start_point, end_point, clrlst[count_colores])


point = sd.get_point(300, 150)
count_angle(point, zero_angle=45, side_length=200, count_sides=user_count, count_colores=user_input_color_count)

sd.pause()
