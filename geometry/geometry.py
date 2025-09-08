import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, lowerleft, upperright):
        if lowerleft[0] < self.x < upperright[0] and lowerleft[1] < self.y < upperright[1]:
            return True
        else:
            return False
    def distance(self, point):
        d = math.sqrt( ((point.x - self.x)**2) + ((point.y - self.y)**2))
        return d

p1 = Point(5,5)
p2 = Point(10,10)
print(p1.falls_in_rectangle((2,2), (10,10)))
print(p1.distance(p2))
