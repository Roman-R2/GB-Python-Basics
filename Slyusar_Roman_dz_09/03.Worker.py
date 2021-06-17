"""
Реализовать базовый класс Worker (работник):
    ● определить атрибуты: name, surname, position (должность), income (доход);
    ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
    элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
    ● создать класс Position (должность) на базе класса Worker;
    ● в классе Position реализовать методы получения полного имени сотрудника
    (get_full_name) и дохода с учётом премии (get_total_income);
    ● проверить работу примера на реальных данных: создать экземпляры класса Position,

передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""


class Worker:
    name = None
    surname = None
    position = None
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, worker_position):
        self.name = name
        self.surname = surname
        self.position = worker_position

    def set_income(self, wage, bonus):
        self._income.update({"wage": wage, "bonus": bonus})


class Position(Worker):
    def __init__(self, name, surname, worker_position):
        super().__init__(name, surname, worker_position)
        pass

    def get_full_name(self):
        return "Name: {}, Surname: {}\n".format(self.name, self.surname)

    def get_total_income(self):
        return "Total income (wage + bonus): {}\n".format(self._income.get("wage")+self._income.get("bonus"))


position = Position("Legolas", "Elf", "Archer")
position.set_income(1000, 100)

print(position.get_full_name())
print(position.get_total_income())
