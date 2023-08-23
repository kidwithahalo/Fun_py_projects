from turtle import *
shape('turtle')
# speed(1) for slow printing

def pentagon(length):
    for i in range(6):
        forward(length)
        right(60)
# just for sake of clarity, we always dea with external angles when working with
# turtle , so here we used 120 , to draw a traingle of 60 degreee

pentagon(100)

# saving the image
getscreen()
getscreen().getcanvas().postscript(file="pentagon.eps")
