# Задание4
# Реализуйте базовый класс Car.у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

# Решение
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The {self.name} went.')

    def stop(self):
        print(f'\nThe {self.name} has stopped.')

    def turn(self, direction):
        print(f'\nThe {self.name} turned {direction}')

    def show_speed(self):
        print(f'\nvehicle speed: {self.speed}')


class TownCar(Car):
    def __init__(self, fuel_rate, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police=False)
        self.fuel_rate = fuel_rate

    def show_rate(self):
        print(f'Fuel rate town car: {self.fuel_rate}')

    def show_speed(self):
        if self.speed <= 60:
            print(f'{self.speed} traffic is allowed ')
        else:
            print(f'You exceeded the speed limit by {60 - self.speed}')


class SportCar(TownCar, Car):
    def __int__(self, fuel_rate, speed, color, name, is_police=False):
        super().__init__(fuel_rate, speed, color, name, is_police=False)

    def show_rate(self):
        print(f'Fuel rate town car: {self.fuel_rate}')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'\nspeeding on {self.speed - 40}')
        else:
            print(f'Speed of {self.name} is normal')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_police(self):
        if self.is_police:
            print(f"It's a police car")
        else:
            print(f'This is not a police car')


town = TownCar(8.5, 59, 'red', 'Astra')
town.show_rate()
town.show_speed()
town.turn('left')
town.turn('right')
town.stop()
print()

sport = SportCar(15, 170, 'red', 'Audi R8')
sport.go()
sport.show_speed()
sport.turn('left')
sport.stop()
print()

work = WorkCar(30, 'red', 'MAZ', False)
work.go()
work.show_speed()
work.turn('right')
work.stop()
print()

police = PoliceCar(100, 'yellow', 'Kia', True)
work.go()
work.show_speed()
work.turn('right')
work.stop()
print()
