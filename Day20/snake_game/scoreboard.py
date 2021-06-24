from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0, 265)
        self.penup()
        self.refresh_score()
        self.hideturtle()

    def refresh_score(self):
        self.clear()
        text = f"Score: {self.score}"
        self.write(text, align=ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)