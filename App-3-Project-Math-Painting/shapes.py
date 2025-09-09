class Rectangle:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
    def draw(self, canvas):
        canvas.img[ self.x:self.x+self.w , self.y:self.y+self.h ] = [self.color.r,self.color.g,self.color.b]


class Square:
    def __init__(self, x, y, s, color):
        self.x = x
        self.y = y
        self.s = s
        self.color = color
    def draw(self, canvas):
        canvas.img[ self.x:self.x+self.s , self.y:self.y+self.s ] = [self.color.r,self.color.g,self.color.b]




class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

