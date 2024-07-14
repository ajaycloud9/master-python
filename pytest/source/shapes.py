import math

class Shape():
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self,len,breadth):
        self.len = len
        self.breadth= breadth

    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return self.len == other.len and self.breadth == other.breadth

    def perimeter(self):
        return (2 * self.len) + (2 * self.breadth)


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length
    