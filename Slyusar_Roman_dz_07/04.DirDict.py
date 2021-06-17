"""
4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:

{
100: 15,
1000: 3,
10000: 7,
100000: 2
}

Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...

Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""
import os

INSPECT_DIR = 'some_data'


def boundary_definition(byte_size):
    """Функция вернет верхнюю границу размера файла, кратную 10"""
    search = True
    multiplicity = 10
    result = 10
    while search:
        if int(byte_size / result) == 0:
            return result
        else:
            result = result * multiplicity


def generate_statistic_dict(inspect_directory):
    """Функция сгенерирует словарь частот по верхней границе размеров файла"""
    statistics = {}
    for item in os.walk(inspect_directory):
        for file_name in item[2]:
            size_in_bytes = os.stat(os.path.join(INSPECT_DIR, file_name)).st_size
            boundary = boundary_definition(size_in_bytes)
            if statistics.get(boundary) is None:
                statistics.update({boundary: 1})
            else:
                freq = statistics.get(boundary) + 1
                statistics.update({boundary: freq})
    return dict(sorted(statistics.items()))


print(generate_statistic_dict(INSPECT_DIR))
