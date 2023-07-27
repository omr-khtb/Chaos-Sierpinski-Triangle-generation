from turtle import *
import random
import numpy as np

omar = Turtle()
#omar.speed(1)

#where to start
omar.penup()
omar.goto(0, 200) 

speed(1)
#triangle first dot
omar.dot()
pnt1 = (0, 200) 
#secound dot
omar.left(-120)
omar.forward(500)
omar.dot()
pnt2 = omar.position()
#third dot
omar.left(120)
omar.forward(500)
omar.dot()
pnt3 = omar.position()
print(pnt1,pnt2,pnt3)

#making array out of points to randomly choose from
points = [pnt1,pnt2,pnt3]
# picking random point in the triangle
omar.goto(2, 100) 

vec = np.array([2])

while True:
    index = random.randrange(0, 3, 1)
    omar.goto((omar.position()+points[index])/vec) 
    print(omar.position())
    omar.dot()
