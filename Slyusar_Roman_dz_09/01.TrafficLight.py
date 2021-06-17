"""
Создать класс TrafficLight (светофор):
    ● определить у него один атрибут color (цвет) и метод running (запуск);
    ● атрибут реализовать как приватный;
    ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
    зелёный;
    ● продолжительность первого состояния (красный) составляет 7 секунд, второго
    (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
    ● переключение между режимами должно осуществляться только в указанном порядке
    (красный, жёлтый, зелёный);
    ● проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
"""

import time


class Color:
    __color = None
    __time = None

    def __init__(self):
        self.set_red()

    def set_red(self):
        self.__color = "red"
        self.__time = 7

    def set_yellow(self):
        self.__color = "yellow"
        self.__time = 2

    def set_green(self):
        self.__color = "green"
        self.__time = 10

    def get_traffic_info(self):
        print("Color {}, time {} \n".format(self.__color, self.__time))

    def get_time(self):
        return self.__time


class TrafficLight(Color):

    def running(self):
        self.get_traffic_info()
        time.sleep(self.get_time())
        self.set_yellow()
        self.get_traffic_info()
        time.sleep(self.get_time())
        self.set_green()
        self.get_traffic_info()
        time.sleep(self.get_time())


traffic_light = TrafficLight()

traffic_light.running()
