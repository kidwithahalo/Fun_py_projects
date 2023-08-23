from turtle import *
shape('turtle')
# speed(1) for slow printing
speed(0)
def triangle(length):
    for i in range(3):
        forward(length)
        right(120)
# just for sake of clarity, we always dea with external angles when working with
# turtle , so here we used 120 , to draw a traingle of 60 degreee

triangle(100)
