# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
class Water:

    def __init__(self):
        self.element = "water"

    def __str__(self):
        return self.element

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm.element
        elif isinstance(other, Fire):
            return Mist.element
        elif isinstance(other, Earth):
            return Dirt.element
        else:
            return None


class Air:
    def __init__(self):
        self.element = "air"

    def __str__(self):
        return self.element

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm.element
        elif isinstance(other, Fire):
            return Lightning.element
        elif isinstance(other, Earth):
            return Dust.element
        else:
            return None


class Fire:
    def __init__(self):
        self.element = "fire"

    def __str__(self):
        return self.element

    def __add__(self, other):
        if isinstance(other, Water):
            return Mist.element
        elif isinstance(other, Air):
            return Lightning.element
        elif isinstance(other, Earth):
            return Lava.element
        else:
            return None


class Earth:
    def __init__(self):
        self.element = "earth"

    def __str__(self):
        return self.element

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt.element
        elif isinstance(other, Air):
            return Dust.element
        elif isinstance(other, Fire):
            return Lava.element
        else:
            return None


class Storm:
    element = 'Storm'

    def __str__(self):
        return self.element


class Mist:
    element = "Mist"

    def __str__(self):
        return self.element


class Dirt:
    element = "Dirt"

    def __str__(self):
        return self.element


class Lightning:
    element = "Lightning"

    def __str__(self):
        return self.element


class Dust:
    element = "Dust"

    def __str__(self):
        return self.element


class Lava:
    element = "Lava"

    def __str__(self):
        return self.element


print(Water(), '+', Air(), '=', Air() + Water())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Fire(), '+', Air(), '=', Air() + Fire())
print(Earth(), '+', Air(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
