"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.

Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном
виде.

Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""


class Matrix:
    __matrix_in_list = []

    def __init__(self, matrix_in_list: list):
        self.__matrix_in_list = matrix_in_list
        self.matrix_check()

    def __str__(self):
        matrix = ""
        for line in self.__matrix_in_list:
            for element in line:
                matrix = matrix + "{}\t".format(element)
            matrix = matrix + "\n"
        return matrix

    def __add__(self, other):
        count = 0
        add_matrix = []
        for line in self.__matrix_in_list:
            add_line = [x + y for x, y in zip(line, other.__matrix_in_list[count])]
            count += 1
            add_matrix.append(add_line)
        return Matrix(add_matrix)

    def matrix_check(self):
        trigger = 0
        line_dimension = 0
        message = "Колличество элементов в строках матрицы не одинаковое"
        for val in self.__matrix_in_list:
            if trigger == 0:
                trigger = len(val)
            else:
                if len(val) != line_dimension:
                    raise ValueError(message)
            line_dimension = len(val)
        return True

    def get_matrix_in_list(self):
        return self.__matrix_in_list


if __name__ == '__main__':
    matrix_1 = [[1, 1], [2, 2], [3, 3]]
    matrix_2 = [[3, 3], [2, 2], [1, 1]]

    matrix_obj_1 = Matrix(matrix_1)
    print(matrix_obj_1.get_matrix_in_list())
    print(matrix_obj_1)

    matrix_obj_2 = Matrix(matrix_2)
    print(matrix_obj_2.get_matrix_in_list())
    print(matrix_obj_2)

    print(matrix_obj_1 + matrix_obj_2)
