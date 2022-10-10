# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
sd.resolution = (1200, 720)

# points_list = [sd.get_point(50, 50), sd.get_point(350, 450)]
# width = 4
# step = 5
#
# for color in rainbow_colors:
#     sd.lines(point_list=points_list, color=color, width=width)
#     points_list[0].x += step
#     points_list[1].x += step

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
point = sd.get_point(700, -100)

width = 30
step = 600

for color in rainbow_colors:
    sd.circle(center_position=point, radius=step, color=color, width=width)
    step += 30

sd.pause()
