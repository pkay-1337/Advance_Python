import math
from random import randint as r
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, rec):
        if rec.point1.x < self.x < rec.point2.x and rec.point1.y < self.y < rec.point2.y:
            return True
        else:
            return False
    def distance(self, point):
        d = math.sqrt( ((point.x - self.x)**2) + ((point.y - self.y)**2))
        return d

class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

print("Guess a point which lies in this Rectangle : ")
r = Rectangle(Point(r(0,9),r(0,9)), Point(r(10,20),r(10,20)))
print("Rectangle Coordinates : ", r.point1.x, r.point1.y, "and", r.point2.x, r.point2.y)

up = Point(float(input("Guess X : ")), float(input("Guess Y : ")))

if up.falls_in_rectangle(r):
    print("You are right")
else:
    print("You are wrong")

