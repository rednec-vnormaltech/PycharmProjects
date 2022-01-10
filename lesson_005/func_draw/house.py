import simple_draw as sd


def draw_house():
    left_bottom_str1 = sd.get_point(300, 0)
    right_top_str1 = sd.get_point(350, 25)
    left_bottom_str2 = sd.get_point(325, 25)
    right_top_str2 = sd.get_point(375, 50)
    for i in range(6):
        for j in range(6):
            sd.rectangle(left_bottom_str1, right_top_str1, color=sd.COLOR_BLUE, width=3)
            left_bottom_str1.x += 50
            right_top_str1.x += 50
        left_bottom_str1.y += 50
        right_top_str1.y += 50
        left_bottom_str1.x = 300
        right_top_str1.x = 350

    for i1 in range(6):
        for j1 in range(6):
            sd.rectangle(left_bottom_str2, right_top_str2, color=sd.COLOR_BLUE, width=3)
            left_bottom_str2.x += 50
            right_top_str2.x += 50
        left_bottom_str2.y += 50
        right_top_str2.y += 50
        left_bottom_str2.x = 325
        right_top_str2.x = 375
