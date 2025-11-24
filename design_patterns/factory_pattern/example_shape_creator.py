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
        raise ValueError("unkown shape type")

shape = shape_factory("square")
shape.draw()  # Output: Drawing a square!

