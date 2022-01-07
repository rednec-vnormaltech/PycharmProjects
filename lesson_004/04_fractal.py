# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


def draw_branches(start_point, angle, branches_length):
    x=100
    zero_point_0, zero_point_1 = start_point, start_point
    zero_angle_0, zero_angle_1 = angle, angle
    zero_length_0, zero_length_1 = branches_length, branches_length

    for _ in range(x):
        v0 = sd.get_vector(zero_point_0, zero_angle_0, zero_length_0, width=5)
        v0.draw(sd.COLOR_DARK_CYAN)
        zero_point_0 = v0.end_point
        zero_angle_0 -= 30
        zero_length_0 *= .75
        if zero_length_0 < 10:
            break

    for _ in range(x):
        v1 = sd.get_vector(zero_point_1, zero_angle_1, zero_length_1, width=5)
        v1.draw(sd.COLOR_DARK_CYAN)
        zero_point_1 = v1.end_point
        zero_angle_1 += 30
        zero_length_1 *= .75
        if zero_length_1 < 10:
            break


root_point = sd.get_point(600, 0)
draw_branches(start_point=root_point, angle=90, branches_length=200, )

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви












# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
