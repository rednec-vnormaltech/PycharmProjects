# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


def draw_rainbow(centr, radius_0, width_0):
    rainbow_colors = [
        sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
        sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE
    ]

    for x in rainbow_colors:
        sd.circle(center_position=centr, radius=radius_0, color=x, width=width_0)
        radius_0 += 10


# rb_point_centr = sd.get_point(300, -450)
# rb_start_radius = 1100
# rb_line_width = 10
#
# draw_rainbow(rb_point_centr, rb_start_radius, rb_line_width)
# sd.pause()
