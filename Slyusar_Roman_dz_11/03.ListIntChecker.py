"""
Создать собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел.

Проверить работу исключения на реальном примере.

Запрашивать у пользователя данные и заполнять список необходимо только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class IntCheckerException(Exception):

    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    go_trigger = 1

    int_list = []

    print("Заполним список числами! Введите 'stop' для окончания заполнения")

    while go_trigger:
        try:
            some_input_int = input("Введите числа для вашего списка: ")
            if some_input_int == "stop":
                print("Вот ваш сисок чисел:", int_list)
                go_trigger = 0
            else:
                if not some_input_int.isnumeric():
                    raise IntCheckerException("Это не число!")
                else:
                    int_list.append(int(some_input_int))
        except IntCheckerException as err:
            print(err)
