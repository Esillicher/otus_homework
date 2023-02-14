"""
создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight=1000, fuel=0, fuel_consumption=1.5):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = None

    def __int__(self, cargo: float, max_cargo: float,  *args, **kwargs):
        self.cargo = cargo
        self.max_cargo = max_cargo
        super().__init__(*args, **kwargs)

    def load_cargo(self, added_cargo: float):
        if added_cargo + self.cargo < self.max_cargo:
            self.cargo += added_cargo
        else:
            raise CargoOverload(f"cargo overload")

        return self.cargo

    def remove_all_cargo(self, prev_cargo):
        prev_cargo = self.cargo
        self.cargo = 0
        return prev_cargo
