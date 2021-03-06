"""
Реализовать класс Road (дорога).
    ● определить атрибуты: length (длина), width (ширина);
    ● значения атрибутов должны передаваться при создании экземпляра класса;
    ● атрибуты сделать защищёнными;
    ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
    ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
    дороги асфальтом, толщиной в 1 см*число см толщины полотна;
    ● проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""


class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass_of_asphalt(self, quantity_for_centimeter, thickness):
        return self._length * self._width * quantity_for_centimeter * thickness


road = Road(5000, 20)

print(road.get_mass_of_asphalt(25, 5))
