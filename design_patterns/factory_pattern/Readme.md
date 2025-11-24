# Factory Design Pattern in Python

## What is the Factory Pattern?
The **factory design pattern** is a *creational pattern* used to separate the creation of objects from their usage. Instead of instantiating classes directly (using `ClassName()`), you use a special factory method or function that decides which object type to return based on input or logic. This improves code flexibility and maintainability, especially when new classes or products are added.

### Why Use It?
- Decouples object creation logic from main application logic.
- Makes it easier to add or change product types without modifying client code.
- Centralizes object creation, following the "open/closed" principle—open for extension, closed for modification.

## Python Example #1: Translator Factory
Let's start simple with a translator/localizer example:
```python
class EnglishLocalizer:
    def localize(self, msg):
        return msg

class FrenchLocalizer:
    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette", "cycle": "cyclette"}
    def localize(self, msg):
        return self.translations.get(msg, msg)

class SpanishLocalizer:
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta", "cycle": "ciclo"}
    def localize(self, msg):
        return self.translations.get(msg, msg)

def Factory(language="English"):
    localizers = {
        "English": EnglishLocalizer,
        "French": FrenchLocalizer,
        "Spanish": SpanishLocalizer,
    }
    return localizers[language]()

# Usage:
french = Factory("French")
print(french.localize("car"))  # Output: voiture
```

## Python Example #2: Shape Creator
```python
class Circle:
    def draw(self):
        print("Drawing a circle!")

class Square:
    def draw(self):
        print("Drawing a square!")

class Rectangle:
    def draw(self):
        print("Drawing a rectangle!")

def shape_factory(shape_type):
    shapes = {
        "circle": Circle,
        "square": Square,
        "rectangle": Rectangle
    }
    if shape_type.lower() in shapes:
        return shapes[shape_type.lower()]()
    else:
        raise ValueError("Unknown shape type")

# Usage:
shape = shape_factory("square")
shape.draw()  # Output: Drawing a square!
```

## Python Example #3: Vehicle Factory
```python
class Car:
    def start(self):
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
        raise ValueError("Unknown vehicle type")

# Usage:
vehicle = vehicle_factory("truck")
vehicle.start()  # Output: Truck started!
```

***
**Quick Review:**
- Factory pattern lets you ask for an object, and the factory decides what class to instantiate based on input.
- This makes your code more modular, easier to maintain, and ready for new types.

Would you like to see a practice question, or want help implementing your own factory function?
If you tell me your course or grade level, I can make this even more tailored.

[1](https://realpython.com/factory-method-python/)
[2](https://refactoring.guru/design-patterns/factory-method/python/example)
[3](https://www.geeksforgeeks.org/python/factory-method-python-design-patterns/)
[4](https://www.youtube.com/watch?v=JIImCgkAQxY)
[5](https://dagster.io/blog/python-factory-patterns)
[6](https://dev.to/khushboo/factory-design-pattern-in-python-3p74)
[7](https://refactoring.guru/design-patterns/abstract-factory/python/example)
[8](https://stackabuse.com/the-factory-method-design-pattern-in-python/)
[9](https://www.youtube.com/watch?v=s_4ZrtQs8Do)
[10](https://www.reddit.com/r/learnpython/comments/1h77ex6/whats_the_point_of_factory_design_pattern/)