# Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght
    def area(self):
        return self.lenght ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
        
n = Shape()
print(n.area())
m = Square(3)
print(m.area())
k = Rectangle(3, 5)
print(k.area())