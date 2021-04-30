"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [23, 1, 3, 10, 4, 11]


Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

"""

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


# Применил частотный анализ
def list_frequency_analysis(original_list):
    rez_dict = {}
    for num in original_list:
        if rez_dict.get(num) is None:
            rez_dict.update({num: 1})
        else:
            freq = rez_dict.get(num) + 1
            rez_dict.update({num: freq})
    return rez_dict


def unique_generator(original_dict):
    for key, value in original_dict.items():
        if value == 1:
            yield key


unique_list = list(unique_generator(list_frequency_analysis(src)))

print(unique_list)
