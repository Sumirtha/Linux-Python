class Quadrilateral:
    def __init__(self, side1, side2, side3, side4):
        self.sides = [side1, side2, side3, side4]
class Square(Quadrilateral):
    def __init__(self, side):
        super().__init__(side, side, side, side)
        self.side = side

    def getArea(self):
        return self.side ** 2

class Rectangle(Quadrilateral):
    def __init__(self, length, breadth):
        super().__init__(length, breadth, length, breadth)
        self.length = length
        self.breadth = breadth

    def getArea(self):
        return self.length * self.breadth

sq = Square(25)
print("Square area:", sq.getArea())

rect = Rectangle(50, 30)
print("Rectangle area:", rect.getArea())