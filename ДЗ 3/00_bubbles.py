# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
# point = sd.get_point(100, 100)
# radius = 50
# for _ in range(3):
#     radius += 5
#     sd.circle(point, radius)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код
def print_bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(point, radius)


# point = sd.get_point(300, 300)
# print_bubble(point, 10)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код
# for x in range(100, 1100, 100):
#     point = sd.get_point(x, 300)
#     print_bubble(point, 5)


# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код
# for x in range(100, 1100, 100):
#     for y in range(100, 400, 100):
#         point = sd.get_point(x, y)
#         print_bubble(point, 5)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код
for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    width = sd.randint(1, 10)
    sd.circle(center_position=point, width=width, color=color)

sd.pause()
