# -*- coding: utf-8 -*-
import os, time, shutil
import zipfile

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

import os
import shutil
import time


class File:
    def __init__(self, path):
        self.path = path
        self.created_time = os.path.getmtime(self.path)

    def get_year_month(self):
        time_tuple = time.gmtime(self.created_time)
        return time_tuple.tm_year, time_tuple.tm_mon

    def copy_to_directory(self, destination_dir):
        year, month = self.get_year_month()
        year_dir = os.path.join(destination_dir, str(year))
        month_dir = os.path.join(year_dir, '{:02d}'.format(month))
        os.makedirs(month_dir, exist_ok=True)
        shutil.copy2(self.path, os.path.join(month_dir, os.path.basename(self.path)))


class PhotoOrganizer:
    def __init__(self, source_dir, destination_dir):
        self.source_dir = source_dir
        self.destination_dir = destination_dir

    def organize_photos(self):
        for root, _, files in os.walk(self.source_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file = File(file_path)
                file.copy_to_directory(os.path.join(self.destination_dir, 'icons_by_year'))


if __name__ == '__main__':
    src_dir = 'icons'
    dest_dir = 'icons_by_year'
    photo_organizer = PhotoOrganizer(src_dir, dest_dir)
    photo_organizer.organize_photos()
