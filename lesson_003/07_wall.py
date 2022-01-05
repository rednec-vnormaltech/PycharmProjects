# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.caption = 'Brick wall'
sd.background_color = sd.COLOR_DARK_CYAN
sd.resolution = (600, 600)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# 1 нарисовать кирпич
left_bottom_str1 = sd.get_point(0, 0)
right_top_str1 = sd.get_point(100, 50)
left_bottom_str2 = sd.get_point(50, 50)
right_top_str2 = sd.get_point(150, 100)
# sd.rectangle(left_bottom, right_top, color=sd.COLOR_BLUE, width=5)

# 2 используя for размножить кирпич в ряд по оси х
for i in range(6):
    for j in range(6):
        sd.rectangle(left_bottom_str1, right_top_str1, color=sd.COLOR_BLUE, width=3)
        #sd.line(sd.get_point(0, left_bottom.y), sd.get_point(600, left_bottom.y), width=7)
        left_bottom_str1.x += 100
        right_top_str1.x += 100
    left_bottom_str1.y += 100
    right_top_str1.y += 100
    left_bottom_str1.x = 00
    right_top_str1.x = 100

for i1 in range(6):
    for j1 in range(6):
        sd.rectangle(left_bottom_str2, right_top_str2, color=sd.COLOR_BLUE, width=3)
        #sd.line(sd.get_point(0, left_bottom.y), sd.get_point(600, left_bottom.y), width=7)
        left_bottom_str2.x += 100
        right_top_str2.x += 100
    left_bottom_str2.y += 100
    right_top_str2.y += 100
    left_bottom_str2.x = 50
    right_top_str2.x = 150






sd.pause()
