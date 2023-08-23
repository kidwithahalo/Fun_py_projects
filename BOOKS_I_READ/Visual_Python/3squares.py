from turtle import *
shape('turtle')

speed(0)

def squares(l):
    for k in range(500):
        for i in range(4):
            forward(l)
            right(90)
        right(5)



squares(200)
