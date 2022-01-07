import simple_draw as sd
import random as r

sd.resolution= (1200,800)

def draw_branches(point, angle, length):
    if length < 3:
        return
    else:

        angle_delta = r.randint(0, 25)
        length_delta = r.uniform(0.6, 0.9)
        angle_left = angle + angle_delta
        angle_right = angle - angle_delta
        v1 = sd.get_vector(start_point=point, angle=angle_left, length=length, width=1)
        v2 = sd.get_vector(start_point=point, angle=angle_right, length=length, width=1)
        v1.draw()
        v2.draw()

        length_delta = r.uniform(0.6, 0.9)
        next_point = v1.end_point
        next_length = length * length_delta
        next_angle = angle_left + r.randint(0, 20)
        draw_branches(point=next_point, angle=next_angle, length=next_length)

        length_delta = r.uniform(0.6, 0.9)
        next_point = v2.end_point
        next_length = length * length_delta
        next_angle = angle_right - r.randint(0, 20)
        draw_branches(point=next_point, angle=next_angle, length=next_length)




root_point = sd.get_point(600, 30)
draw_branches(point=root_point, angle=90, length=100)

sd.pause()