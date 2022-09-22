# Задание
# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение
# метода draw. Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры
# классов и проверить, что выведет описанный метод для каждого экземпляра

# Решение
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'\nStarting rendering for {self.title} class')


class Pen(Stationary):
    def draw(self):
        print(f'\nStarting rendering for the {self.title} class\n')


class Pencil(Stationary):
    def draw(self):
        print(f'\nStarting rendering for the {self.title} class\n')


class Handle(Stationary):
    def draw(self):
        print(f'\nStarting rendering for the {self.title} class\n')


new_stationary = Stationary('Stationary')
new_stationary.draw()

new_pen = Pen('Pen')
new_pen.draw()

new_pencil = Pencil('Pencil')
new_pencil.draw()

new_handle = Handle('Handle')
new_handle.draw()
