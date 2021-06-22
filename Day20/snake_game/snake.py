from turtle import Turtle, Screen
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, screen):
        self.snake_body = []
        self.screen = screen
        self.create_initial_snake()
        self.head = self.snake_body[0]

    def create_initial_snake(self):
        for i in range(3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            xPos = -20 * i
            snake.goto(xPos, 0)
            self.snake_body.append(snake)

    def move(self):
        snake_length = len(self.snake_body) - 1
        for index in range(snake_length, 0, -1):
            self.snake_body[index].goto(self.snake_body[index - 1].xcor(), self.snake_body[index - 1].ycor())
        self.snake_body[0].forward(20)
        self.screen.update()

    def move_forward(self):
        self.move()
        self.snake_body[0].forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
