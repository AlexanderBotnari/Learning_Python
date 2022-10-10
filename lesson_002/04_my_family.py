#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mama', 'tata', 'Sandu', 'Mihai', 'Marina', 'Giku']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['mama', 160],
    ['tata', 170],
    ['Sandu', 180],
    ['Mihai', 190],
    ['Marina', 165],
    ['Giku', 182]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("Рост ", my_family[1], " - ", my_family_height[1][1], "см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum = my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1] + my_family_height[3][1] + my_family_height[4][1] + my_family_height[5][1]
print('Общий рост моей семьи - ', sum, ' см ')
