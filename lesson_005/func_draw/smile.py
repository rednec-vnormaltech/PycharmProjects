import simple_draw as sd


def draw_smile(x, y, color):
    # рисуем голову и лицо
    point_left = sd.get_point(x - 120, y - 100)
    point_right = sd.get_point(x, y)
    sd.ellipse(point_left, point_right, color)
    circle_point = sd.get_point(x - 35, y - 35)
    sd.circle(circle_point, 8, sd.invert_color(color))
    circle_point = sd.get_point(x - 85, y - 35)
    sd.circle(circle_point, 8, sd.invert_color(color))

    # рисуем улыбку
    points = [
        sd.get_point(x - 85, y - 65),
        sd.get_point(x - 80, y - 70),
        sd.get_point(x - 75, y - 72),
        sd.get_point(x - 65, y - 74),
        sd.get_point(x - 61, y - 74),
        sd.get_point(x - 57, y - 74),
        sd.get_point(x - 47, y - 72),
        sd.get_point(x - 42, y - 70),
        sd.get_point(x - 37, y - 65),

        sd.get_point(x - 42, y - 75),
        sd.get_point(x - 47, y - 79),
        sd.get_point(x - 50, y - 81),
        sd.get_point(x - 57, y - 82),
        sd.get_point(x - 61, y - 82),
        sd.get_point(x - 65, y - 82),
        sd.get_point(x - 72, y - 80),
        sd.get_point(x - 75, y - 78),
        sd.get_point(x - 80, y - 75),
        sd.get_point(x - 85, y - 65),
    ]

    sd.lines(points, sd.invert_color(color))


# draw_smile(500, 500, sd.COLOR_CYAN)
#
# sd.pause()
