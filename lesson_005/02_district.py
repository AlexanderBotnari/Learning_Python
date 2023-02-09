# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код
from district.central_street.house1 import room1 as chr1_1
from district.central_street.house1 import room2 as chr1_2
from district.central_street.house2 import room1 as chr2_1
from district.central_street.house2 import room2 as chr2_2
from district.soviet_street.house1 import room1 as shr1_1
from district.soviet_street.house1 import room2 as shr1_2
from district.soviet_street.house2 import room1 as shr2_1
from district.soviet_street.house2 import room2 as shr2_2

cs = chr1_1.folks + chr1_2.folks + chr2_1.folks + chr2_2.folks
ss = shr1_1.folks + shr1_2.folks + shr2_1.folks + shr2_2.folks

print('На районе живут : ', cs + ss)




