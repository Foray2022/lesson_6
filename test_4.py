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
        Car.__init__(self, speed, color, name, is_police=False)
        self.fuel_rate = fuel_rate

    def show_rate(self):
        print(f'Fuel rate town car: {self.fuel_rate}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nYour speed is higher than allow! Your speed is {self.speed}'
        else:
            return f'Speed of {self.name} is normal'


class PoliceCar(Car):
    pass


town = TownCar('Audi', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('AudiRS', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('WAZ', 30, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Kia', 100, 'yellow', True)
print('4:\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

