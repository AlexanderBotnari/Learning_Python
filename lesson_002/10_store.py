#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
tables_cost_1 = store[goods['Стол']][0]['quantity'] * store[goods['Стол']][0]['price']
tables_cost_2 = store[goods['Стол']][1]['quantity'] * store[goods['Стол']][1]['price']

table_code = goods['Стол']
tables_item_1 = store[table_code][0]
tables_item_2 = store[table_code][1]
tables_quantity_1 = tables_item_1['quantity']
tables_quantity_2 = tables_item_2['quantity']
tables_price_1 = tables_item_1['price']
tables_price_2 = tables_item_2['price']
tables_cost_1 = tables_quantity_1 * tables_price_1
tables_cost_2 = tables_quantity_2 * tables_price_2
print('Стол 1 -', tables_quantity_1, 'шт, стоимость', tables_cost_1, 'руб')
print('Стол 2 -', tables_quantity_2, 'шт, стоимость', tables_cost_2, 'руб')


sames_cost_1 = store[goods['Диван']][0]['quantity'] * store[goods['Диван']][0]['price']
sames_cost_2 = store[goods['Диван']][1]['quantity'] * store[goods['Диван']][1]['price']

same_code = goods['Диван']
sames_item_1 = store[same_code][0]
sames_item_2 = store[same_code][1]
sames_quantity_1 = sames_item_1['quantity']
sames_quantity_2 = sames_item_2['quantity']
sames_price_1 = sames_item_1['price']
sames_price_2 = sames_item_2['price']
sames_cost_1 = sames_quantity_1 * sames_price_1
sames_cost_2 = sames_quantity_2 * sames_price_2
print('Диван 1 -', sames_quantity_1, 'шт, стоимость', sames_cost_1, 'руб')
print('Диван 2 -', sames_quantity_2, 'шт, стоимость', sames_cost_2, 'руб')


chairs_cost_1 = store[goods['Стул']][0]['quantity'] * store[goods['Стул']][0]['price']
chairs_cost_2 = store[goods['Стул']][1]['quantity'] * store[goods['Стул']][1]['price']
chairs_cost_3 = store[goods['Стул']][2]['quantity'] * store[goods['Стул']][2]['price']

chair_code = goods['Стул']
chairs_item_1 = store[chair_code][0]
chairs_item_2 = store[chair_code][1]
chairs_item_3 = store[chair_code][2]
chairs_quantity_1 = chairs_item_1['quantity']
chairs_quantity_2 = chairs_item_2['quantity']
chairs_quantity_3 = chairs_item_3['quantity']
chairs_price_1 = chairs_item_1['price']
chairs_price_2 = chairs_item_2['price']
chairs_price_3 = chairs_item_3['price']
chairs_cost_1 = chairs_quantity_1 * chairs_price_1
chairs_cost_2 = chairs_quantity_2 * chairs_price_2
chairs_cost_3 = chairs_quantity_3 * chairs_price_3

print('Стул 1 -', chairs_quantity_1, 'шт, стоимость', chairs_cost_1, 'руб')
print('Стул 2 -', chairs_quantity_2, 'шт, стоимость', chairs_cost_2, 'руб')
print('Стул 3 -', chairs_quantity_3, 'шт, стоимость', chairs_cost_3, 'руб')
##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################






