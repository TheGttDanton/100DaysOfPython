from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


def get_turtles(colors):
    turtles = []
    y = 90
    x = -240
    for color in colors:
        turtle = Turtle(shape="turtle")
        turtle.penup()
        turtle.color(color)
        turtle.setpos(x, y)
        y += -30
        turtles.append(turtle)
    return turtles


colors = ["red", "green", "purple", "blue", "skyblue", "cyan"]
turtles = get_turtles(colors)

race_on = True

while race_on:
    for turtle in turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)

        if turtle.xcor() > 230:
            print("race over")
            race_on = False
            break


screen.exitonclick()