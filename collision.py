import math

class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def __str__(self):
        return "x=" + str(self.x) + ", y=" + str(self.y)

class Line:
    def __init__(self, orig, term):
        self.orig = orig
        self.term = term

    def overlap(self, other):
        if other.orig <= self.orig <= other.term:
            return True
        if other.orig <= self.term <= other.term:
            return True
        if self.orig <= other.orig <= self.term:
            return True
        if self.orig <= other.term <= self.term:
            return True
        return False

class Rectangle:
    def __init__(self, initP, initW, initH):
        self.location = initP
        self.width = initW
        self.height = initH

    def contains(self, point):
        Xvals = self.location.x + self.width
        Yvals = self.location.y + self.height
        if point.x >= self.location.x and point.x < Xvals:
            if point.y >= self.location.y and point.y < Yvals:
                return True
        return False

    @property
    def x_span(self):
        return Line(self.location.x, self.location.x + self.width)

    @property
    def y_span(self):
        return Line(self.location.y, self.location.y + self.width)

    def collision(self, other):
        if self.x_span.overlap(other.x_span) and self.y_span.overlap(other.y_span):
            return True
        return False

locX = Point(0, 0)
locY = Point(1, 1)

x = Rectangle(locX, 2, 1)
y = Rectangle(locY, 2, 1)

locP = Point(0, 0)
locR = Point(5, 5)

p = Rectangle(locP, 1, 1)
r = Rectangle(locR, 1, 1)

print(x.collision(y))
print(p.collision(r))
