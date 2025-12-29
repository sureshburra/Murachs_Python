from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Triangle(Shape):
    def draw(self):
        return "Drawing a Triange"

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type):
        shapes = {
                'circle': Circle,
                'square': Square,
                'triangle': Triangle
        }
        shape_class = shapes.get(shape_type.lower())
        if shape_class:
            return shape_class()
        raise ValueError(f"Unknown shape type: {shape_type}")

# Usage
factory = ShapeFactory()
circle = factory.create_shape('circle')
print(circle.draw())
