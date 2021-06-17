"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
декоратора @property.

"""
from abc import ABC, abstractmethod


class AbstractClothes(ABC):

    @abstractmethod
    def tissue_consumption(self):  # расход ткани
        pass


class Coat(AbstractClothes):
    __size = 0

    def __init__(self, size):
        self.__size = size

    @property
    def tissue_consumption(self):
        return self.__size / 6.5 + 0.5


class Suit(AbstractClothes):
    __rise = 0

    def __init__(self, rise):
        self.__rise = rise

    @property
    def tissue_consumption(self):
        return 2 * self.__rise + 0.3


if __name__ == '__main__':
    coat = Coat(45)
    print(coat.tissue_consumption)

    suit = Suit(45)
    print(suit.tissue_consumption)
