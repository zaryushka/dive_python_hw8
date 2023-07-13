# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться. name, id, level
# словарь - {level: {id: name}}



import json

def users_dostup():

    try:
        with open('user_data.json', 'r', encoding='utf-8') as f:
            data_all = json.load(f)
    except FileNotFoundError:
        data_all = {}

    while True:
        name = input('введите имя (или "выход"): ')
        if name.lower() == 'выход':
            break

        id = input('введите идентификатор: ')
        level = input('введите уровень доступа (от 0 до 7): ')

        for i in data_all.values():
            if id in i:
                print('такой id уже существует')
                break
        else:
            user_dict = {id: name}

            if level in data_all:
                data_all[level].update(user_dict)
            else:
                data_all[level] = user_dict

            with open('user_data.json', 'w', encoding='utf-8') as f:
                json.dump(data_all, f, ensure_ascii=False, indent=2)
            print(f'пользователь {name} успешно добавлен')

users_dostup()