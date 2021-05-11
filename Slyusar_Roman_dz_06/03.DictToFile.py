"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.

Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.

Сохранить словарь в файл.

Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
скрипта с кодом «1».

При решении задачи считать, что объём данных в файлах во много раз
меньше объема ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович

Фрагмент файла с данными о хобби  (hobby.csv):
скалолазание,охота
горные лыжи
"""
import json

NAMES = "users.csv"
HOBBY = "hobby.csv"
JSON_FILE = "user_hobby.json"


def clear_string(in_str):
    return in_str.replace("\n", "")


def clear_commas(in_str):
    return in_str.replace(",", "")


def get_attr_list(file_name):
    with open(file_name, "r") as f:
        return f.readlines()


def save_to_json_file(to_json_file, save_dict):
    with open(to_json_file, 'w+') as f:
        f.write(str(save_dict))


def create_dict():
    names_list = get_attr_list(NAMES)
    hobby_list = get_attr_list(HOBBY)
    if len(hobby_list) > len(names_list):
        return 1
    rez_dict = {}
    count = 0
    for name in names_list:
        hobby = hobby_list[count] if count < len(hobby_list) else "None"
        rez_dict.update({
            clear_commas(clear_string(name)): clear_string(hobby)
        })
        count += 1
    save_to_json_file(JSON_FILE, rez_dict)
    print("Файл сохранен с именем ", JSON_FILE)
    return 0


print(create_dict())
