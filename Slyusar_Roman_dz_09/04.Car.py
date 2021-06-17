"""
Реализуйте базовый класс Car:
    ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
    также методы: go, stop, turn(direction), которые должны сообщать, что машина
    поехала, остановилась, повернула (куда);
    ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    ● добавьте в базовый класс метод show_speed, который должен показывать текущую
    скорость автомобиля;
    ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
    скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
    превышении скорости.
"""


class Car:
    speed = 0
    color = None
    name = None
    is_police = 0

    def __init__(self, speed, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return "Машина поехала"

    def stop(self):
        return "Машина остановилась"

    def turn(self, direction):
        return "Машина повернула {}".format(direction)

    def show_speed(self):
        return self.speed

    def check_police(self):
        return self.is_police

class TownCar(Car):
    speed_limit = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        pass

    def show_speed(self):
        return self.speed if self.speed < self.speed_limit else "Вы превысили разрешенную скорость {} " \
                                                                "км/ч".format(self.speed_limit)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        pass


class WorkCar(Car):
    speed_limit = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        pass

    def show_speed(self):
        return self.speed if self.speed < self.speed_limit else "Вы превысили разрешенную скорость {} " \
                                                                "км/ч".format(self.speed_limit)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True
        pass


town_car_1 = TownCar(59, "Red", "Kia Rio")
print(town_car_1.show_speed())
print(town_car_1.check_police())

town_car_2 = TownCar(100, "Red", "F1")
print(town_car_2.show_speed())

police_car = PoliceCar(100, "White", "Buchanka", )
print(police_car.go())
print(police_car.stop())
print(police_car.turn("right"))
print(police_car.check_police())
