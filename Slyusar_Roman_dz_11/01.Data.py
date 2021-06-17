"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода.

Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число».

Второй — с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""


class Date:
    __date_string = ""

    def __init__(self, date_string):
        self.__date_string = date_string

    @classmethod
    def string_date_to_int(cls, date_string):
        date_list = date_string.split("-")
        return {"day": int(date_list[0]), "month": int(date_list[1]), "year": int(date_list[2])}

    @staticmethod
    def date_validate(date_string):
        date_list = date_string.split("-")
        if not (0 < int(date_list[0]) <= 31):
            message = "День за пределами допустимого значения: {}".format(int(date_list[0]))
            raise ValueError(message)
        if not (0 < int(date_list[1]) <= 12):
            message = "Месяц за пределами допустимого значения: {}".format(int(date_list[0]))
            raise ValueError(message)
        if not (0 < int(date_list[1])):
            message = "Год за пределами допустимого значения: {}".format(int(date_list[0]))
            raise ValueError(message)
        return True


if __name__ == '__main__':
    date = Date("24-05-2021")
    print(Date.date_validate("31-05-2021"))
    print(Date.string_date_to_int("24-05-2021"))
