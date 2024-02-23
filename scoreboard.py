from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=('Arial', 20, 'normal'))

    def add_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 20, 'normal'))
