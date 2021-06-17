"""
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого
числа деления клеток соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение
количества ячеек этих двух клеток.

Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Этот метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом
случае метод make_order() вернёт строку: *****\n*****\n**.
Или количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод
make_order() вернёт строку: *****\n*****\n*****.
"""


class Cell:
    __cell_cells = 0

    def __init__(self, cell_cells: int):
        self.__cell_cells = cell_cells
        if self.__cell_cells < 0:
            message = "Должно быть положительное колличество ячеек!"
            raise ValueError(message)

    def __add__(self, other):
        return Cell(self.__cell_cells + other.__cell_cells)

    def __sub__(self, other):
        some_cell_cells = self.__cell_cells - other.__cell_cells
        if some_cell_cells > 0:
            return Cell(some_cell_cells)
        else:
            message = "Мы не можем вычесть эти клетки! В первой не хватает ячеек."
            raise ValueError(message)

    def __mul__(self, other):
        return Cell(self.__cell_cells * other.__cell_cells)

    def __floordiv__(self, other):
        return Cell(self.__cell_cells // other.__cell_cells)

    def __truediv__(self, other):
        return Cell(self.__cell_cells // other.__cell_cells)

    @property
    def get_cell_cells(self):
        return self.__cell_cells

    def make_order(self, amount_in_line):
        marker = "*"
        count = 1
        row_of_cells = ""
        while count <= self.__cell_cells:
            if count % amount_in_line == 0:
                row_of_cells = row_of_cells + marker + "\\n"
            else:
                row_of_cells = row_of_cells + marker
            count += 1
        return row_of_cells


if __name__ == '__main__':
    cell_1 = Cell(10)
    cell_2 = Cell(20)

    add_cell = cell_1 + cell_2
    print(add_cell.get_cell_cells)

    sub_cell = cell_2 - cell_1
    print(sub_cell.get_cell_cells)

    mul_cell = cell_1 * cell_2
    print(mul_cell.get_cell_cells)

    truediv_cell = cell_2 / cell_1
    print(truediv_cell.get_cell_cells)

    floordiv_cell = cell_2 // cell_1
    print(floordiv_cell.get_cell_cells)

    cell_3 = Cell(12)

    print(cell_3.make_order(5))
