""" import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.forward(200)

def message(input):
    print(input)
message("Hello Class")
message("aloha amigo")
message("i am inevitable")

def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)

def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200)

def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right()


def rectangle():
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
rectangle()

def equal():
    t.forward(90)
    t.left(120)
    t.forward(90)
    t.left(120)
    t.forward(90)
equal()

turtle.done() """


import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(100000)

""" def equal():
    for i in range(3):
        t.forward(90)
        t.left(120)
equal() """
def square():
    for i in range(6000):
        for i in range(4):
            t.forward(200)
            t.left(90)
        t.left(5)


square()

    

turtle.done()
