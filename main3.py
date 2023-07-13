from pathlib import Path
import shutil
import os


# Path('some_dir/another_dir/dir').mkdir(parents=True)

# Path('test_dir/one_dir').mkdir(parents=True)

# shutil.copy('result.txt', 'some_dir')

# print(Path.cwd)

# shutil.copy('user_data.json', 'test_dir')

# shutil.copy('user_data.json', 'test_dir/one_dir')

# os.remove('temp.py')

# shutil.copy('my_file_alsu.txt', 'test_dir/one_dir')

shutil.copy('result.txt', 'test_dir/one_dir')

# text = 'тренировка создания и удаления файлов, копирования файлов, создания директорий'
# with open('my_file_alsu.txt', 'a', encoding='utf-8') as f_alsu:
#     res = f_alsu.write(text)

# text = '\nдобавлю еще текста\n'
# with open('my_file_alsu.txt', 'a', encoding='utf-8') as f_alsu:
#     res = f_alsu.write(text)

# text = "\n{1: 'a', 2: 'b', 3: 'c'}\nфункция write() добавляет только строковые аргументы???\n"
# with open('my_file_alsu.txt', 'a', encoding='utf-8') as f_alsu:
#     res = f_alsu.write(text)

# text = "\n{1: 'a', 2: 'b', 3: 'c'}\nфункция write() добавляет только строковые аргументы???\n"
# with open('my_file_alsu.txt', 'a', encoding='utf-8') as f_alsu:
#     res = f_alsu.write(text)

# text = "\nпотому что формат файла ткст, надо использовать для словаря json\n"
# with open('my_file_alsu.txt', 'a', encoding='utf-8') as f_alsu:
#     res = f_alsu.write(text)

# text_new = "\nкогда сделала на все тексты одну переменную, все добавилось, уф\n"
# with open('my_file_alsu.txt', 'a', encoding='utf-8') as f_alsu:
#     res = f_alsu.write(text_new)

# text_new_new = "\nвсе ще дублируется текст??\n"
# with open('my_file_alsu.txt', 'a', encoding='utf-8') as f_alsu:
#     res = f_alsu.write(text_new_new)