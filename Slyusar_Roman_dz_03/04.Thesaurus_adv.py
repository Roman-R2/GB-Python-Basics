"""
4. *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
записи, в которых фамилия начинается с соответствующей буквы. Например:

thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}

Как поступить, если потребуется сортировка по ключам?
"""


def split_for_names(*args):
    name_dict = {}
    for value in args:
        if not isinstance(value, str):  # Проверим, что нам пришли строки, иначе пропустим цикл
            break

        first_char = value[0]

        if not name_dict.get(first_char):
            name_dict.update({first_char: [value]})
        else:
            print(name_dict[first_char].append(value))

    return name_dict


def thesaurus_adv(*args):
    surname_dict = {}

    for value in args:
        if not isinstance(value, str):  # Проверим, что нам пришли строки, иначе пропустим цикл
            break

        first_char = value.split()[1][0]

        if not surname_dict.get(first_char):
            surname_dict.update({first_char: [value]})
        else:
            print(surname_dict[first_char].append(value))

    for key, list_of_value in surname_dict.items():
        temp_dict = split_for_names(*list_of_value)
        surname_dict.update({key: temp_dict})

    return surname_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева",
                    "Spider Man", "Iron Man"))
