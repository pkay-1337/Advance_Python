class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def falls_in_rectangle(self, lowerleft, upperright):
        if lowerleft[0] < self.x < upperright[0] and lowerleft[1] < self.y < upperright[1]:
            return True
        else:
            return False
p1 = Point(5,5)
print(p1.falls_in_rectangle((2,2), (10,10)))
