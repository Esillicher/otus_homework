"""
создайте класс `Car`, наследник `Vehicle`
"""

import base
import engine as engine_module


class Car(base.Vehicle):
    engine: int
    # engine: engine_module.Engine = None

    def set_engine(self, eng: engine_module.Engine):
        self.engine = eng
        return self.engine


# car = Car()
# print(car)
# eng1 = engine_module.Engine(1, 2)
# print(eng1)
# # car.engine = eng1
# # print(car.engine)
# print(car.set_engine(engine_module.Engine))
# print(car.engine)


