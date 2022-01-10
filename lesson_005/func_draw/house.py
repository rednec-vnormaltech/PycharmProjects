import simple_draw as sd


def draw_house():
    # блок рисования кирпичей
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

    # блок рисования каркаса дома
    # линия 1
    house_line0_start = sd.get_point(300, 0)  # левая стена начало
    house_line0_finish = sd.get_point(300, 300)

    # линия 2
    house_line1_start = house_line0_finish  # потолок начало
    house_line1_finish = sd.get_point(625, 300)

    # линия 3
    house_line2_start = house_line1_finish  # левая стена начал
    house_line2_finish = sd.get_point(625, 000)

    sd.line(house_line0_start, house_line2_finish, color=sd.COLOR_BLUE, width=3)  # рисование пола
    sd.line(house_line0_start, house_line0_finish, color=sd.COLOR_BLUE, width=3) # рисование левой стены
    sd.line(house_line1_start, house_line1_finish, color=sd.COLOR_BLUE, width=3)  # рисование потолка
    sd.line(house_line2_start, house_line2_finish, color=sd.COLOR_BLUE, width=3)  # рисование правой стены
