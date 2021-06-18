from turtle import Turtle, Screen

tim = Turtle()
tim.speed(1)

# Dashed
for _ in range(8):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()