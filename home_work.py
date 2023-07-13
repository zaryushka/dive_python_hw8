# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

import os
import json
import csv
import pickle

def walk_dir(directory):
    objects = []
    
# рекурсивно обходим все каталоги от заданной директории. формируем путь до каждого текущего объекта
    for dir_path, dir_name, file_name in os.walk(directory):
        for object_name in dir_name + file_name:
            object_path = os.path.join(dir_path, object_name)
            print(object_path)
            
# проверка объекта - файл или директория, если файл то добавим его в список с информацией о файле
# если директория - в список с информацией о директории
            if os.path.isfile(object_path):
                object_info = {
                    'name': object_name,
                    'parent_dir': dir_path,
                    'type': 'file',
                    'size': os.path.getsize(object_path)
                }
                objects.append(object_info)
                
            elif os.path.isdir(object_path):
                object_info = {
                    'name': object_name,
                    'parent_dir': dir_path,
                    'type': 'directory',
                    'size': dir_size(object_path)
                }
                objects.append(object_info)
    print(objects)
    
# открываем файлы для записи форматов json, csv, pickle
    with open('result_dir.json', 'w', encoding='utf-8') as json_file:
        json.dump(objects, json_file, indent=2)
    
    with open('result_dir.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['name', 'parent_dir', 'type', 'size']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect='excel-tab', delimiter=' ')
        writer.writeheader()
        writer.writerows(objects)
    
    with open('result_dir.pickle', 'wb') as pickle_file:
        pickle.dump(objects, pickle_file)


# обходим все каталоги и считаем размер содержимого директорий
def dir_size(directory):
    total_size = 0
    
    for dir_path, dir_name, file_name in os.walk(directory):
        for f in file_name:
            f_path = os.path.join(dir_path, f)
            total_size += os.path.getsize(f_path)
            
    return total_size

# Пример использования функции
walk_dir('test_dir')