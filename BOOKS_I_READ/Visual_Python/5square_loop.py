from turtle import *
shape('turtle')

def square(length):
    for i in range(60):
        for j in range(4):
            forward(length)
            right(90)
        right(5)
        length += 5

square(5)
