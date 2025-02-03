# Write the definition of a Point class. Objects from this class should have a
# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points
import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x}, {self.y})")
    def move(self, newx, newy):
        self.x = newx
        self.y = newy
    def dist(self, next):
        return math.sqrt((self.x - next.x) ** 2 + (self.y - next.y) ** 2)

p1 = Point(3, 4)
p2 = Point(6, 8)

p1.show()
p2.show()

print(p1.dist(p2))

p1.move(1, 2)
p1.show()