from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def counter_clockwise():
    tim.left(2)


def clockwise():
    tim.right(2)


def clear():
    tim.clear()
    tim.reset()


screen = Screen()
screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=counter_clockwise, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
