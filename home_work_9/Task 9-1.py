import time


class TrafficLight:
    __color = ""

    def running(self):
        self.__color = "Красный"
        print(self.__color)
        time.sleep(7)
        self.__color = "Жёлтый"
        print(self.__color)
        time.sleep(2)
        self.__color = "Зелёный"
        print(self.__color)
        time.sleep(5)


switching = TrafficLight()
switching.running()