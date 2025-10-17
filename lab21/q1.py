class Quadrilateral:
    def __init__(self, side1, side2, side3, side4):
        self.sides = [side1, side2, side3, side4]

    def isSquare(self):
        return len(set(self.sides)) == 1

    def isRectangle(self):
        return self.sides[0] == self.sides[2] and self.sides[1] == self.sides[3]

# (a) All sides different
quad1 = Quadrilateral(91, 288, 355, 40)
print("quad1 is Square:", quad1.isSquare())
print("quad1 is Rectangle:", quad1.isRectangle())
# (b) Opposite sides same
quad2 = Quadrilateral(29, 33, 29, 33)
print("quad2 is Square:", quad2.isSquare())
print("quad2 is Rectangle:", quad2.isRectangle())
# (c) All sides same
quad3 = Quadrilateral(41, 41, 41, 41)
print("quad3 is Square:", quad3.isSquare())
print("quad3 is Rectangle:", quad3.isRectangle())