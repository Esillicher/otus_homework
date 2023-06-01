"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine = None

    def set_engine(self, eng: Engine):
        self.engine = eng
        return self.engine


# car = Car(1)
# print(car.engine)
# eng1 = Engine(1, 2)
# print(eng1)
# # car.engine = eng1
# # print(car.engine)
# print(car.set_engine(eng1))
# print(car.engine)


