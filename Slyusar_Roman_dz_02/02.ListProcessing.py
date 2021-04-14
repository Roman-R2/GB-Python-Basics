"""
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число кавычками и дополнить нулём до двух разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+5', '"', 'градусов']

Новый список не создавать! Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов
"""

original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+50', 'градусов']


def isint(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def signfilter(element):
    try:
        temp_list = list(element)
        if temp_list[0] == '+' or temp_list[0] == '-':
            return True
    except ValueError:
        return False


def insertbreakers(i):
    original_list.insert((i + 1), "\"")
    original_list.insert(i, "\"")
    return 1


def intfilter(element, i):
    if len(element) == 1:
        element = "0" + element
        original_list[i] = element
    if element[0] == '+' or element[0] == '-':
        tmp_list = list(element)
        if len(tmp_list) == 2:
            tmp_list.insert(1, "0")
            element = ''.join(tmp_list)
            original_list[i] = element
    return element


trigger = 0

print("Исходный лист: ", original_list)

for i, element in enumerate(original_list):
    if trigger == 1:
        trigger = 0
        continue
    if (element.isdigit() and isint(element)) or signfilter(element):
        intfilter(element, i)
        insertbreakers(i)
        trigger = 1

original_list_to_string = ' '.join(original_list)

print("Результирующая строка: ", original_list_to_string)
