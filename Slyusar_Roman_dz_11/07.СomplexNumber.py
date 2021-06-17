"""
Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное
число». Реализовать перегрузку методов сложения и умножения комплексных чисел.
Проверить работу проекта. Для этого создать экземпляры класса (комплексные числа),
выполнить сложение и умножение созданных экземпляров. Проверить корректность
полученного результата.
"""


class ComplexNumber:
    __real_part = 0
    __imaginary_part = 0
    __string_complex_number = ""

    def __init__(self, real_part: int, imaginary_part: int):
        self.check_complex_part(real_part, imaginary_part)
        self.__real_part = real_part
        self.__imaginary_part = imaginary_part
        self.parsing_complex_number()

    def __add__(self, other):
        # (a + bi) ± (c + di) = (a ± c) + (b ± d)i
        real_part = self.__real_part + other.__real_part
        imaginary_part = self.__imaginary_part + other.__imaginary_part
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other):
        # (a + bi) · (c + di) = (ac – bd) + (ad + bc)i
        real_part = (self.__real_part * other.__real_part) - (self.__imaginary_part * other.__imaginary_part)
        imaginary_part = (self.__real_part * other.__imaginary_part) - (self.__imaginary_part *
                                                                        other.__real_part)  # !!!
        return ComplexNumber(real_part, imaginary_part)

    def check_complex_part(self, real_part, imaginary_part):
        if not isinstance(real_part, int) or not isinstance(imaginary_part, int):
            message = "В класс {} передано не целое число!".format(self.__class__)
            raise ValueError(message)

    def parsing_complex_number_with_val(self, real_part, imaginary_part):
        if real_part < 0 and imaginary_part < 0:
            self.__string_complex_number = "{} - {}i".format(real_part, abs(imaginary_part))
        elif real_part < 0 and imaginary_part > 0:
            self.__string_complex_number = "{} + {}i".format(real_part, imaginary_part)
        elif real_part > 0 and imaginary_part > 0:
            self.__string_complex_number = "{} + {}i".format(real_part, imaginary_part)
        elif real_part > 0 and imaginary_part < 0:
            self.__string_complex_number = "{} - {}i".format(real_part, abs(imaginary_part))
        else:
            self.__string_complex_number = "{} - {}i".format(real_part, imaginary_part)
        return True

    def parsing_complex_number(self):
        real_part = self.__real_part
        imaginary_part = self.__imaginary_part
        self.parsing_complex_number_with_val(real_part, imaginary_part)
        return True

    def get_string_complex_number(self):
        return self.__string_complex_number


if __name__ == '__main__':
    complex_number_1 = ComplexNumber(-2, -2)
    complex_number_2 = ComplexNumber(-3, 3)
    complex_number_3 = ComplexNumber(+4, -4)
    complex_number_4 = ComplexNumber(2, 3)
    complex_number_5 = ComplexNumber(-1, 1)

    print(complex_number_1.get_string_complex_number())
    print(complex_number_2.get_string_complex_number())
    print(complex_number_3.get_string_complex_number())
    print(complex_number_4.get_string_complex_number())
    print(complex_number_5.get_string_complex_number())
    print("\n")

    add_complex_number = complex_number_1 + complex_number_2
    print("Сложение: ", add_complex_number.get_string_complex_number())
    mul_complex_number = complex_number_4 * complex_number_5
    print("Умножение: ", mul_complex_number.get_string_complex_number())
