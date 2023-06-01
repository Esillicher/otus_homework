"""
создайте класс `Plane`, наследник `Vehicle`
"""


from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight: float, fuel: float, fuel_consumption: float, max_cargo: float):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = 10
        self.cargo = 0

    # def __init__(self, cargo: float, max_cargo: float,  *args, **kwargs):
    #     self.cargo = cargo
    #     self.max_cargo = max_cargo
    #     super().__init__(*args, **kwargs)

    def load_cargo(self, added_cargo: float):
        if added_cargo + self.cargo < self.max_cargo:
            self.cargo += added_cargo
        else:
            raise CargoOverload(f"cargo overload")

        return self.cargo

    def remove_all_cargo(self):
        prev_cargo = self.cargo
        self.cargo = 0
        return prev_cargo


# plane = Plane(100,100,19,1)
# plane = Plane(weight=5375, fuel=3520, fuel_consumption=7151, started=False)

