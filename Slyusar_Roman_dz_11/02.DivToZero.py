"""
Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class OwnClassZeroDiv(Exception):

    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    SOME_NUMBER = 100
    divider = input("Давай поделтм {} на число! Введите это число-делитель: ".format(SOME_NUMBER))

    try:
        print(SOME_NUMBER / int(divider))
    except OwnClassZeroDiv as err:
        print(err)
