from abc import ABC
from homework_02 import exceptions
# import pytest


class Vehicle(ABC):
    def __init__(self, weight=1000, fuel=0, fuel_consumption=1.5):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    started: bool = False

    def __str__(self):
        return f"{type(self).__name__}(weight={self.weight!r}, fuel={self.fuel}," \
               f" fuel_consumption={self.fuel_consumption}, started={self.started})"

    def __repr__(self):
        return str(self)

    def start(self) -> bool:
        if self.started and self.fuel > 0:
            print('engine already started')
        else:
            if self.fuel == 0:
                self.started = False
                raise exceptions.LowFuelError(f"not enough fuel for start")
            else:
                print('successfully started')
                self.started = True

        return self.started

    def move(self, distance: int):
        needed_fuel = self.fuel_consumption * distance

        if self.fuel < needed_fuel:
            raise exceptions.NotEnoughFuel(f"not enough fuel for journey")
        else:
            print("let's go!")
            self.fuel -= needed_fuel

        return self.fuel



# print(scoopy.start())
# scoopy.started = True
# print(scoopy)
# print(scoopy.start())
# # #print(scoopy.move(0.1))
# # print(scoopy)
# # print(scoopy.move(1))
# assert scoopy.started is False
# scoopy.fuel = 0

# scoopy = Vehicle()
# scoopy.fuel = 0
# with pytest.raises(exceptions.LowFuelError):
#     scoopy.start()
#
# scoopy.fuel = 0.1
# with pytest.raises(exceptions.NotEnoughFuel):
#     scoopy.move(1)

# assert scoopy.started is False
# print(LowFuelError.mro())


