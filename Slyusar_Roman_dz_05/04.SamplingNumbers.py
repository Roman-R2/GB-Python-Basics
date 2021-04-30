"""
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]


Подсказка: использовать возможности python, изученные на уроке.
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
"""

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def list_generator(original_list):
    last_num = original_list[0]
    for num in original_list:
        if last_num < num:
            yield num
        last_num = num


choice_list_gen = list_generator(src)
choice_list = list(choice_list_gen)

print(type(choice_list_gen))
print(type(choice_list))
print(choice_list)
