"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    def __init__(self, engine: Engine | None = None, *args, **kwargs):
        self.engine = engine
        super().__init__(*args, **kwargs)

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


