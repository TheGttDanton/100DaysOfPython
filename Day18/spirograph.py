from turtle import Turtle, Screen
import random

def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    return (r, g, b)

circle = Turtle()
circle.speed(0)
screen = Screen()
screen.colormode(255)

for i in range(120):
    circle.color((random_color()))
    circle.circle(100)
    circle.left(3)

screen.exitonclick()
