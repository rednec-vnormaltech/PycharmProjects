# -*- coding: utf-8 -*-
import random as r
import simple_draw as sd
from random import choice, randint

sd.resolution = (1200, 1000)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 4

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код


list_point = [sd.get_point(300, 800),sd.get_point(400, 800),sd.get_point(500, 800),sd.get_point(600, 800)]
list_snowflake_p = [0.6, 0.35, 60]


def snowfall():
    x = 300
    y = 800

    x1 = 300
    y1 = 800

    while True:
        point = sd.get_point(x, y)
        point1 = sd.get_point(x1, y1)

        for ret in range(N):


            sd.snowflake(center=list_point[ret], length=20, color=sd.COLOR_WHITE, factor_a=list_snowflake_p[0],
                     factor_b=list_snowflake_p[1], factor_c=list_snowflake_p[2])
            sd.finish_drawing()

            sd.sleep(0.05)

            sd.start_drawing()

            sd.snowflake(center=point, length=20, color=sd.background_color, factor_a=list_snowflake_p[0],
                         factor_b=list_snowflake_p[1], factor_c=list_snowflake_p[2])


        y -= 5


        if y < 50:
            y = 800
            list_snowflake_p[0]=r.uniform(0.1,0.9)
            list_snowflake_p[2] = r.uniform(0.1, 0.9)
            list_snowflake_p[2] = r.randint(1, 180)
        x = r.randint(x - 15, x + 15)




def random_color():
    """
        Выдать случайный цвет из набора предопределенных
    """
    colors = [

        sd.COLOR_YELLOW,
        sd.COLOR_GREEN,
        sd.COLOR_DARK_YELLOW,
        sd.COLOR_DARK_GREEN,
    ]
    return choice(colors)


def draw_branches(start_point, angle, branches_length):
    if branches_length > 5:
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


root_point = sd.get_point(600, 0)
# draw_branches(start_point=root_point, angle=90, branches_length=50)

snowfall()
snowfall()

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
