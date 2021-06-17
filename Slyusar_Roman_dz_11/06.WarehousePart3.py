"""
4. Начать работу над проектом «Склад оргтехники». Создать класс, описывающий склад. А также
класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
параметры, общие для приведённых типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

5. Продолжить работу над предыдущим заданием. Разработать методы, которые отвечают за
приём оргтехники на склад и передачу в определённое подразделение компании. Для:
хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над предыдущим заданием. Реализовать механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Warehouse:
    __warehouse_dict = {}

    def show_goods_in_warehouse(self):
        return self.__warehouse_dict

    def put_in_the_warehouse(self, goods_dict):
        self.__warehouse_dict.update({
            len(self.__warehouse_dict):
                goods_dict
        })
        return True

    def receive_from_the_warehouse(self, shelf_number):
        if not isinstance(shelf_number, int):
            message = "Номер полки является целым числом!"
            raise ValueError(message)
        return self.__warehouse_dict.pop(shelf_number)


class OfficeEquipment:
    weight = 0
    model = ""

    def __init__(self, weight, model):
        self.weight = weight
        self.model = model

    def get_equipment_data(self):
        return {"weight": self.weight, "model": self.model}


class Printer(OfficeEquipment):
    cartridge_model = ""

    def __init__(self, weight, model, cartridge_model):
        super().__init__(weight, model)
        self.cartridge_model = cartridge_model

    def get_equipment_data(self):
        return {"weight": self.weight, "model": self.model, "cartridge_model": self.cartridge_model}


class Scanner(OfficeEquipment):
    max_scan_size = ""

    def __init__(self, weight, model, max_scan_size):
        super().__init__(weight, model)
        self.max_scan_size = max_scan_size

    def get_equipment_data(self):
        return {"weight": self.weight, "model": self.model, "max_scan_size": self.max_scan_size}


if __name__ == '__main__':
    printer = Printer(5, "HP", "36B")
    print(printer.get_equipment_data())

    scanner = Scanner(2, "Kyocera", "A3")
    print(scanner.get_equipment_data())

    warehouse = Warehouse()
    print(warehouse.show_goods_in_warehouse())
    warehouse.put_in_the_warehouse(printer.get_equipment_data())
    print(warehouse.show_goods_in_warehouse())
    warehouse.put_in_the_warehouse(scanner.get_equipment_data())
    print(warehouse.show_goods_in_warehouse())
    print(warehouse.receive_from_the_warehouse(0))
    print(warehouse.show_goods_in_warehouse())
    print(warehouse.receive_from_the_warehouse(1))
    print(warehouse.show_goods_in_warehouse())
