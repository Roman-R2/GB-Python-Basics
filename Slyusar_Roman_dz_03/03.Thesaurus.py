"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
содержащие имена, начинающиеся с соответствующей буквы. Например:

thesaurus("Иван", "Мария", "Петр", "Илья")
{
"И": ["Иван", "Илья"],
"М": ["Мария"],
"П": ["Петр"]
}

Подумайте: полезен ли будет вам оператор распаковки?
Как поступить, если потребуется
сортировка по ключам?
Можно ли использовать словарь в этом случае?
"""


def thesaurus(*args):
    """ A function that takes employee names as arguments, and returning employee dictionary"""
    name_dict = {}
    for value in args:
        first_char = value[0]
        if not name_dict.get(first_char):
            name_dict.update({first_char: [value]})
        else:
            print(name_dict[first_char].append(value))
    return name_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Subzero", "Superman"))
