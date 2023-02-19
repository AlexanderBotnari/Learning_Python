# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
# import io
#
#
# class LogParser:
#     temp_data = ''
#
#     def __init__(self, analysis_file, result_file):
#         self.analysis_file = analysis_file
#         self.result_file = result_file
#
#     def write_file(self):
#         with open(self.result_file, 'w', encoding='utf8') as file_with_errors:
#             file_with_errors.writelines(self.temp_data)
#
#     def write_errors_minute(self):
#         with open(self.analysis_file, 'r', encoding='utf8') as file:
#             for line in file:
#                 if line.__contains__('NOK'):
#                     self.temp_data += line
#                 else:
#                     pass
#         self.write_file()
#
#     def print_time(self):
#         with open(self.analysis_file, 'r', encoding='utf8') as file:
#             print(file.read(28))
#
#
# log = LogParser('events.txt', 'errors.txt')
# # log.write_errors_minute()
# log.print_time()

with open('events.txt', 'r') as f:
    events = f.readlines()

nok_events = {}
for event in events:
    if 'NOK' in event:
        event_time = event[1:17]  # extrage data si ora evenimentului
        event_minute = event_time[:-3] + '00'  # taie secundele de la ora evenimentului
        if event_minute in nok_events:
            nok_events[event_minute] += 1
        else:
            nok_events[event_minute] = 1

with open('nok_events.txt', 'w') as f:
    for event_time, count in nok_events.items():
        f.write(f"[{event_time}:00.000000] NOK {count}\n")