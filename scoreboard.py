from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.high_score = 0
        self.score = 0
        self.refresh()

    def add_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.load_highscore()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_highscore()
        self.score = 0
        self.refresh()

    def save_highscore(self, filename="data.txt"):
        with open(filename, "w") as file:
            file.write(str(self.high_score))

    def load_highscore(self, filename="data.txt"):
        with open(filename, "r") as file:
            self.high_score = int(file.read())

