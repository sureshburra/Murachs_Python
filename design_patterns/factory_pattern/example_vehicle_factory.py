class Car:
    def drive(self):
        print("Car started!")

class Bike:
    def start(self):
        print("Bike started!")

class Truck:
    def start(self):
        print("Truck started!")

def vehicle_factory(vehicle_type):
    vehicles = {
        "car": Car,
        "bike": Bike,
        "truck": Truck
    }
    cls = vehicles.get(vehicle_type.lower())
    if cls:
        return cls()
    else:
        raise ValueError("unknown vehicle type")

vehicle = vehicle_factory("truck")
vehicle.start()  # Output: Truck started!
