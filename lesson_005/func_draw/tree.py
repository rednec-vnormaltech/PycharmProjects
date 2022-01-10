# -*- coding: utf-8 -*-
from random import choice
import random as r
import simple_draw as sd


def random_color():
    """ Выдать случайный цвет из набора предопределенных """
    colors = [sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_DARK_YELLOW, sd.COLOR_DARK_GREEN, ]
    return choice(colors)


def draw_branches(start_point, angle, branches_length):
    if branches_length > 2:
        zero_point_0, zero_point_1 = start_point, start_point
        zero_angle_0, zero_angle_1 = angle, angle
        zero_length_0, zero_length_1 = branches_length, branches_length

        v0 = sd.get_vector(zero_point_0, zero_angle_0, zero_length_0, width=1)
        v0.draw(random_color())
        next_point = v0.end_point
        zero_angle_0 += r.randint(20, 40)
        zero_length_0 *= r.uniform(0.6, 0.9)
        draw_branches(start_point=next_point, angle=zero_angle_0, branches_length=zero_length_0, )

        v1 = sd.get_vector(zero_point_1, zero_angle_1, zero_length_1, width=1)
        v1.draw(random_color())
        next_point_1 = v1.end_point
        zero_angle_1 -= r.randint(0, 45)
        zero_length_1 *= r.uniform(0.6, 0.9)
        draw_branches(start_point=next_point_1, angle=zero_angle_1, branches_length=zero_length_1, )
