class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print(f"{self.color} {self.name} поехала")

    def stop(self):
        print(f"{self.color} {self.name} остановилась")

    def turn(self, direction):
        self.direction = direction
        print(f"{self.color} {self.name} повернула на {self.direction}")

    def show_speed(self):
        print(f"Скорость: {self.speed}")


class TownCar(Car):
     def __init__(self, speed, color, name):
         super().__init__(speed, color, name)

     def show_speed(self):
        print(f"Скорость: {self.speed}") if self.speed <= 60 else print("Превышена допустимая скорость")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f"Скорость: {self.speed}") if self.speed <= 40 else print("Превышена допустимая скорость")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


c, t, s, w, p = Car(40, "Белая","Audi"), TownCar(65, "Черная","BMW"), SportCar(40, "Красная","Ferrari"),\
                WorkCar(40, "Вишневая","Lada"), PoliceCar(40, "Серая","Skoda")

t.go(), t.turn("право"), t.stop()
t.show_speed()
print(f"Марка: {c.name}, Цвет: {c.color}, Скорость: {c.speed}, Полицейская: {c.is_police} \n")

