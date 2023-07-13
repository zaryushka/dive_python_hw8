# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json

def create_json_file(file_name):
    my_dict = {}
    with open(file_name, 'r', encoding='utf-8') as f_old:
        for line in f_old:
            name, num = line.split()
            name = name.capitalize()
            num = float(num)
            my_dict[name] = num

    with open(f'{file_name[:-3]}.json', 'w', encoding='utf-8') as f_json:
        json.dump(my_dict, f_json, ensure_ascii=False, indent=2)



create_json_file('result.txt')