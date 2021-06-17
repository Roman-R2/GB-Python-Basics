"""
Реализовать класс Stationery (канцелярская принадлежность):
    ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
    сообщение «Запуск отрисовки»;
    ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    ● в каждом классе реализовать переопределение метода draw. Для каждого класса
    метод должен выводить уникальное сообщение;
    ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
    экземпляра.
"""


class Stationery:
    title = None

    def __init__(self, title):
        self.title = title

    def draw(self):
        return print("«Запуск отрисовки»")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        pass

    def draw(self):
        return print("«Я класс {} должен выводить уникальное занчение»".format(self.__class__))


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        pass

    def draw(self):
        return print("«Я класс {} должен выводить уникальное занчение. Это точно другое»".format(
            self.__class__))


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        pass

    def draw(self):
        return print("«Я класс {} должен выводить уникальное занчение. Смотри, сзади Чак Норис!!!»".format(
            self.__class__))


pen = Pen("Reach")
pen.draw()

pencil = Pencil("Завод имени Ленина")
pencil.draw()

handle = Handle("Just handle")
handle.draw()
