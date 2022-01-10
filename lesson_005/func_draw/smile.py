import simple_draw as sd


def draw_smile(x, y, color):
    # рисуем голову и лицо
    # координаты головы и размер
    point_left = sd.get_point(x - 60, y - 50)
    point_right = sd.get_point(x, y)
    sd.ellipse(point_left, point_right, color)

    # правй глаз
    circle_point = sd.get_point(x - 17, y - 17)
    sd.circle(circle_point, 8, sd.invert_color(color))

    # левый глаз
    circle_point = sd.get_point(x - 43, y - 17)
    sd.circle(circle_point, 8, sd.invert_color(color))

    # рисуем улыбку
    points = [
        sd.get_point(x - 42.5, y - 32.5),
        sd.get_point(x - 40, y - 35),
        sd.get_point(x - 37.5, y - 35),
        sd.get_point(x - 32.5, y - 37),
        sd.get_point(x - 30.5, y - 37),
        sd.get_point(x - 28.5, y - 37),
        sd.get_point(x - 23.5, y - 36),
        sd.get_point(x - 21, y - 35),
        sd.get_point(x - 18.5, y - 32.5),

        sd.get_point(x - 21, y - 37.5),
        sd.get_point(x - 23.5, y - 39.5),
        sd.get_point(x - 25, y - 40.5),
        sd.get_point(x - 28.5, y - 41),
        sd.get_point(x - 30.5, y - 41),
        sd.get_point(x - 32.5, y - 41),
        sd.get_point(x - 35.5, y - 40),
        sd.get_point(x - 37.5, y - 39),
        sd.get_point(x - 40, y - 37.5),
        sd.get_point(x - 42.5, y - 32.5),
    ]

    sd.lines(points, sd.invert_color(color))


# draw_smile(500, 500, sd.COLOR_CYAN)
#
# sd.pause()
