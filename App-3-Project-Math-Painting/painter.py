from PIL import Image
import numpy as np
from shapes import Rectangle, Square, Color

class Canvas:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.img = np.zeros((rows, columns, 3), dtype=np.uint8)

    def save(self, name):
        Image.fromarray(self.img, "RGB").save(f"{name}.png")




class Painter:
    def __init__(self):
        self.canvas = Canvas(int(input("Enter canvas rows pixels : ")),\
                int(input("Enter canvas column pixels : ")))

    def getColor(self):
        return Color(\
                int(input("Enter R value : ")),\
                int(input("Enter G value : ")),\
                int(input("Enter B value : ")))

    def getSquare(self):
            Square(int(input("Enter x cordinate : ")),\
                    int(input("Enter y cordinate : ")),\
                    int(input("Enter side length : ")),\
                    self.getColor()).draw(self.canvas)

    def getRectangle(self):
            Rectangle(int(input("Enter x cordinate : ")),\
                    int(input("Enter y cordinate : ")),\
                    int(input("Enter widht length : ")),\
                    int(input("Enter height length : ")),\
                    self.getColor()).draw(self.canvas)
    def save(self, name):
        self.canvas.save(name)
