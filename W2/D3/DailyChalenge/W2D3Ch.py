import math
import turtle
class Circle:
    def __init__(self, radius=None, diameter=None):
        self.radius, self.diameter = self.radius_diameter(radius, diameter)

    @staticmethod
    def radius_diameter(radius, diameter):
        return (radius, radius * 2) if radius else (diameter / 2, diameter)

    def __repr__(self):
        return f"{self.__dict__}"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def circle_area(self):
        return math.pi*self.radius**2

    def sort_list(self, *args):
        out_list = [self]
        for circles in args:
            out_list.append(circles)
        return sorted(out_list)


c1 = Circle(radius=5)
c2 = Circle(diameter=20)
# print(c1.diameter)
# print(c2.radius)
# print(c1.circle_area())
# print(c1)
# print(c1 + c2)
print(c1 == c2)
print(c1.sort_list(c2))
for each_circle in c1.sort_list(c2):
    turtle.circle(each_circle.diameter)