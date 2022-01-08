# -*- coding: utf-8 -*-
import random as r
import simple_draw as sd

sd.resolution = (1500, 1200)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код

list_point = [sd.get_point(100, 800), sd.get_point(300, 800), sd.get_point(500, 800), ]
list_snowflake_parameters = [r.uniform(0.1, 0.9), r.uniform(0.1, 0.9), r.randint(2, 150), ]


def snowfall():
    length_snowflake = 50
    # x, y = 100, 1200

    while True:
        sd.clear_screen()
        sd.snowflake(center=list_point[0], length=length_snowflake, factor_a=list_snowflake_parameters[0],
                     factor_b=list_snowflake_parameters[1], factor_c=list_snowflake_parameters[2])
        list_point[0].y -= 6
        if list_point[0].y < 50:
            list_point[0].y = 1100

        sd.snowflake(center=list_point[1], length=length_snowflake, factor_a=list_snowflake_parameters[0],
                     factor_b=list_snowflake_parameters[1], factor_c=list_snowflake_parameters[2])
        list_point[1].y -= 5
        list_point[1].x += 2 / .5
        if list_point[1].y < 50:
            list_point[1].y = 900
            list_point[1].x = 350

        sd.snowflake(center=list_point[2], length=length_snowflake, factor_a=list_snowflake_parameters[0],
                     factor_b=list_snowflake_parameters[1], factor_c=list_snowflake_parameters[2])
        list_point[2].y -= 7
        list_point[2].x += 2 / .9
        if list_point[2].y < 50:
            # break
            list_point[2].y = 1000
            list_point[2].x = 550
            list_snowflake_parameters[0] = r.uniform(0.1, 0.9)
            list_snowflake_parameters[1] = r.uniform(0.1, 0.9)
            list_snowflake_parameters[2] = r.randint(2, 150)

        sd.sleep(0.01)
        if sd.user_want_exit():
            break


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
