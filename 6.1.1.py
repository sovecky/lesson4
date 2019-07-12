import  math

class Triangle:
    def __init__(self, A, B, C):
        def sideLen(point1, poitnt2):
            return math.sqrt((point1[0] - poitnt2[0]) ** 2
                             + (point1[1] - poitnt2[1]) ** 2)

        self.A = A
        self.B = B
        self.C = C
        self.AB = sideLen(self.A, self.B)
        self.BC = sideLen(self.B, self.C)
        self.CA = sideLen(self.C, self.A)

    def areaTriangle(self):
        perimeter = self.perimeterTriangle() / 2

        return math.sqrt(perimeter
                         * (perimeter - self.AB)
                         * (perimeter - self.BC)
                         * (perimeter - self.CA))
    def perimeterTriangle(self):
        return self.AB + self.BC + self.CA

    def heightTriangle(self):
        return self.areaTriangle() / (self.AB / 2)


treugolnik = Triangle((7, 2), (1, 7), (8, 55))

print('Площадь треугольника равна',treugolnik.areaTriangle())
print('Высота треугольника равна', treugolnik.heightTriangle())
print('Периметр треугольника равен', treugolnik.perimeterTriangle())


