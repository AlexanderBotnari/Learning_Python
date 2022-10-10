# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 720)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg
# TODO здесь ваш код
# def triangle(start_point, angle, length):
#     v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle+120, length=length)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle+240, length=length)
#     v3.draw()
#
#
# def square(start_point, angle, length):
#     v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle+90, length=length)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle+180, length=length)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle+270, length=length)
#     v4.draw()
#
#
# def pentagon(start_point, angle, length):
#     v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 70, length=length)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 140, length=length)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 210, length=length)
#     v4.draw()
#
#     sd.line(start_point=start_point, end_point=v4.end_point)
#
#
# def hexagon(start_point, angle, length):
#     v1 = sd.get_vector(start_point=start_point, angle=angle, length=length)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point=v1.end_point, angle=angle + 60, length=length)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point=v2.end_point, angle=angle + 120, length=length)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length)
#     v5.draw()
#
#     sd.line(start_point=start_point, end_point=v5.end_point)
#
#
# point_triangle = sd.get_point(200, 200)
# point_square = sd.get_point(200, 400)
# point_pentagon = sd.get_point(800, 200)
# point_hexagon = sd.get_point(800, 400)
#
# triangle(point_triangle, angle=0, length=200)
# square(start_point=point_square, angle=30, length=200)
# pentagon(point_pentagon, 30, 100)
# hexagon(point_hexagon, 0, 100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)
# TODO code
def common_func(point, angle, length, grade, *nr_of_sides):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()

    v2 = sd.get_vector(start_point=v1.end_point, angle=v1.angle + grade, length=length)
    v2.draw()

    v3 = sd.get_vector(start_point=v2.end_point, angle=v2.angle + grade, length=length)
    v3.draw()

    return v3


def triangle(start_point, angle, length):
    common_func(point=start_point, angle=angle, length=length, grade=120)


def square(start_point, angle, length):
    v3 = common_func(point=start_point, angle=angle, length=length, grade=90)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 270, length=length)
    v4.draw()


def pentagon(start_point, angle, length):
    v3 = common_func(point=start_point, angle=angle, length=length, grade=70)
    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 210, length=length)
    v4.draw()

    sd.line(start_point=start_point, end_point=v4.end_point)


def hexagon(start_point, angle, length):
    v3 = common_func(point=start_point, angle=angle, length=length, grade=60)

    v4 = sd.get_vector(start_point=v3.end_point, angle=angle + 180, length=length)
    v4.draw()

    v5 = sd.get_vector(start_point=v4.end_point, angle=angle + 240, length=length)
    v5.draw()

    sd.line(start_point=start_point, end_point=v5.end_point)


point_triangle = sd.get_point(200, 200)
point_square = sd.get_point(200, 400)
point_pentagon = sd.get_point(800, 200)
point_hexagon = sd.get_point(800, 400)

triangle(point_triangle, angle=0, length=200)
square(start_point=point_square, angle=30, length=200)
pentagon(point_pentagon, 30, 100)
hexagon(point_hexagon, 0, 100)
# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
