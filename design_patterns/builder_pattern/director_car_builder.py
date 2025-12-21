from abc import ABC, abstractmethod


class Car:
    def __init__(self):
        self.engine = None
        self.wheels = 4
        self.color = None
        self.sunroof = False

    def __repr__(self):
        return (
            f"Car(engine={self.engine}, wheels={self.wheels}, "
            f"color={self.color}, sunroof={self.sunroof})"
        )


class CarBuilder(ABC):
    def __init__(self):
        self._car = Car()

    @abstractmethod
    def set_engine(self): ...

    @abstractmethod
    def paint(self): ...

    @abstractmethod
    def add_extras(self): ...

    def get_result(self):
        return self._car


class SportsCarBuilder(CarBuilder):
    def set_engine(self):
        self._car.engine = "V8"

    def paint(self):
        self._car.color = "red"

    def add_extras(self):
        self._car.sunroof = True


class EconomyCarBuilder(CarBuilder):
    def set_engine(self):
        self._car.engine = "1.2L"

    def paint(self):
        self._car.color = "white"

    def add_extras(self):
        self._car.sunroof = False


class CarDirector:
    def __init__(self, builder: CarBuilder):
        self._builder = builder

    def construct_basic(self):
        self._builder.set_engine()
        self._builder.paint()
        self._builder.add_extras()
        return self._builder.get_result()


# Usage
sports_car = CarDirector(SportsCarBuilder()).construct_basic()
economy_car = CarDirector(EconomyCarBuilder()).construct_basic()

print(sports_car)
print(economy_car)
