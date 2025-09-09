from painter import Painter
p = Painter()

while(1):
    i = int(input("""
Enter 1 to draw square
Enter 2 to draw Rectangle
Enter 0 to save and quit
>>> 
    """))
    if(i == 0):
        p.save(input("Enter file name : "))
        print("File saved")
        break
    elif(i == 1):
        p.getSquare()
    elif(i == 2):
        p.getRectangle()
    else:
        print("BAD INPUT")
        continue


