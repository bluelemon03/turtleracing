import random
import turtle
t = turtle.Turtle()
t.shape('turtle')
i = number = random.randint(0,9)
while i >= 4:
    t.forward(20)
    i=random.randint(0,9)
    if i == 0:
        break
    

turtle.done()
