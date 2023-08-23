from turtle import *
shape('turtle')

speed(0)
def star(length):
    for k in range(60):
        for i in range(5):
            forward(length)
            right(144)
        right(5)
        length += 5

star(35)
