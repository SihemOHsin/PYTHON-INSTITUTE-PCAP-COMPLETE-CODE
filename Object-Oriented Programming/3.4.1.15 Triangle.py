﻿import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y=y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y


    def distance_from_xy(self, x, y):
        return math.hypot(abs(self.__x-x), abs(self.__y - y))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3

    def perimeter(self):
        side1 = self.vertice1.distance_from_point(self.vertice2)
        side2 = self.vertice2.distance_from_point(self.vertice3)
        side3 = self.vertice3.distance_from_point(self.vertice1)
        return side1 + side2 + side3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())