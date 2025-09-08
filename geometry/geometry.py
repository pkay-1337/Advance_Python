import math
import turtle
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

class GuiRectangle(Rectangle):
    def draw(self, canvas):
        canvas.penup()
        canvas.goto(self.point1.x,self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)


print("Guess a point which lies in this Rectangle : ")
r = GuiRectangle(Point(r(0,400),r(0,400)), Point(r(10,400),r(10,400)))
print("Rectangle Coordinates : ", r.point1.x, r.point1.y, "and", r.point2.x, r.point2.y)

up = Point(float(input("Guess X : ")), float(input("Guess Y : ")))
res = 0
if up.falls_in_rectangle(r):
    print("You are right")
    res = 1
else:
    print("You are wrong")

canvas = turtle.Turtle()
r.draw(canvas)
canvas.penup()
canvas.goto(up.x, up.y)
canvas.pendown()
canvas.dot(10, 'green' if res else 'red') 

turtle.done()


