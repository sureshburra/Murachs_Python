from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class VehicleSpecs:
    color: str
    engine_type: str
    seats: int


class Vehicle(ABC):
    def __init__(self, specs: VehicleSpecs):
        self.specs = specs

    @abstractmethod
    def get_info(self):
        pass


class Car(Vehicle):
    def get_info(self):
        return f"Car: {self.specs.color}, \
    {self.specs.engine_type}, {self.specs.seats} seats"


class Motorcycle(Vehicle):
    def get_info(self):
        return f"Motorcycle: {self.specs.color}, \
    {self.specs.engine_type}, {self.specs.seats} seats"


class Truck(Vehicle):
    def get_info(self):
        return f"Truck: {self.specs.color}, \
    {self.specs.engine_type}, {self.specs.seats} seats"


class VehicleFactory:
    _vehicle_types = {
            'car': Car,
            'motorcycle': Motorcycle,
            'truck': Truck
    }

    @classmethod
    def create_vehicle(cls, vehicle_type, color, engine_type, seats):
        vehicle_class = cls._vehicle_types.get(vehicle_type.lower())
        if not vehicle_class:
            raise ValueError(f"Unkown vehicle type: {vehicle_type}")

        specs = VehicleSpecs(color, engine_type, seats)
        return vehicle_class(specs)


# Usage
car = VehicleFactory.create_vehicle('car', 'red', 'V6', 5)
print(car.get_info())

motorcycle = VehicleFactory.create_vehicle('motorcycle', 'black', 'V-twin', 2)
print(motorcycle.get_info())
